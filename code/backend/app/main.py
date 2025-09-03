# code/backend/main.py

import os
import logging
from datetime import timedelta, datetime
from typing import List

from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from pydantic import BaseModel
from passlib.context import CryptContext

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA

import pytesseract
from pdf2image import convert_from_bytes
from transformers import pipeline

# =========================
# CONFIG
# =========================
SECRET_KEY = "" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("finance-rag")

# Fake users DB (replace with DB)
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("admin123"),
        "role": "admin",
    },
    "analyst": {
        "username": "analyst",
        "hashed_password": pwd_context.hash("analyst123"),
        "role": "analyst",
    },
    "viewer": {
        "username": "viewer",
        "hashed_password": pwd_context.hash("viewer123"),
        "role": "viewer",
    },
}

# =========================
# SCHEMAS
# =========================
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    role: str | None = None


class User(BaseModel):
    username: str
    role: str


# =========================
# AUTH HELPERS
# =========================
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(OAuth2PasswordRequestForm)):
    credentials_exception = HTTPException(
        status_code=401, detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token.password, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None:
            raise credentials_exception
        return User(username=username, role=role)
    except JWTError:
        raise credentials_exception


def role_required(roles: List[str]):
    def checker(user: User = Depends(get_current_user)):
        if user.role not in roles:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        return user

    return checker


# =========================
# OCR
# =========================
def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    images = convert_from_bytes(pdf_bytes)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img) + "\n"
    return text.strip()


# =========================
# RAG PIPELINE
# =========================
def load_rag_pipeline():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    if not os.path.exists("vectorstore"):
        os.makedirs("vectorstore")
        vectorstore = FAISS.from_texts(["Finance seed text"], embedding_model)
        vectorstore.save_local("vectorstore")
    else:
        vectorstore = FAISS.load_local("vectorstore", embedding_model)

    generator = HuggingFacePipeline(
        pipeline=pipeline(
            "text-generation",
            model="your-finetuned-llama3",
            max_new_tokens=256,
            temperature=0.2,
            device=-1,
        )
    )

    return RetrievalQA.from_chain_type(
        llm=generator,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff",
    )


qa = load_rag_pipeline()

# =========================
# FASTAPI
# =========================
app = FastAPI(title="Finance RAG + Fine-tuned LLaMA3")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(
        data={"sub": user["username"], "role": user["role"]}, expires_delta=access_token_expires
    )
    return {"access_token": token, "token_type": "bearer"}


@app.post("/ocr-extract")
def ocr_extract(file: UploadFile = File(...), user: User = Depends(role_required(["admin", "analyst"]))):
    pdf_bytes = file.file.read()
    text = extract_text_from_pdf(pdf_bytes)
    return {"filename": file.filename, "extracted_text": text}


@app.post("/ask")
def ask_question(query: str, user: User = Depends(role_required(["admin", "analyst", "viewer"]))):
    logger.info(f"User {user.username} ({user.role}) asked: {query}")
    answer = qa.run(query)
    return {"query": query, "answer": answer}
