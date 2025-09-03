from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
import os


SECRET_KEY = os.getenv("JWT_SECRET", "dev-secret")
ALGO = "HS256"
ACCESS_MIN = int(os.getenv("JWT_MINUTES", "120"))


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


USERS = {
"admin": {"password": pwd_context.hash("admin123"), "role": "admin"},
"analyst": {"password": pwd_context.hash("analyst123"), "role": "analyst"},
"viewer": {"password": pwd_context.hash("viewer123"), "role": "viewer"},
}


class TokenData(BaseModel):
username: str
role: str


def authenticate(username: str, password: str) -> Optional[TokenData]:
user = USERS.get(username)
if not user or not pwd_context.verify(password, user["password"]):
return None
return TokenData(username=username, role=user["role"])


def create_token(data: TokenData) -> str:
to_encode = {"sub": data.username, "role": data.role, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_MIN)}
return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGO)


def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
try:
payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGO])
return TokenData(username=payload.get("sub"), role=payload.get("role"))
except JWTError:
raise HTTPException(status_code=401, detail="Invalid token")


def require_role(*roles: str):
def _inner(user: TokenData = Depends(get_current_user)):
if user.role not in roles:
raise HTTPException(status_code=403, detail="Forbidden")
return user
return _inner
