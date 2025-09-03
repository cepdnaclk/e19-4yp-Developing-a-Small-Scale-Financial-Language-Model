import os
import argparse
import glob
import logging

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from ocr import extract_text_from_pdf
from logging_conf import logger


DATA_DIR = "data/corpus"
INDEX_DIR = "vectorstore"


def load_documents(data_dir: str):
    """
    Load and OCR documents from the given folder.
    Supports PDFs and TXT files.
    """
    documents = []

    for filepath in glob.glob(os.path.join(data_dir, "**/*"), recursive=True):
        if filepath.endswith(".pdf"):
            logger.info(f"OCR extracting from PDF: {filepath}")
            with open(filepath, "rb") as f:
                pdf_bytes = f.read()
                text = extract_text_from_pdf(pdf_bytes)
                documents.append((filepath, text))
        elif filepath.endswith(".txt"):
            logger.info(f"Loading TXT file: {filepath}")
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
                documents.append((filepath, text))
        else:
            logger.warning(f"Skipping unsupported file: {filepath}")

    return documents


def chunk_texts(documents):
    """
    Split documents into smaller chunks for embedding.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50, length_function=len
    )

    all_chunks = []
    for filepath, text in documents:
        chunks = splitter.split_text(text)
        logger.info(f"Chunked {filepath} into {len(chunks)} parts")
        all_chunks.extend(chunks)

    return all_chunks


def build_faiss_index(chunks, index_dir: str):
    """
    Build or update FAISS index with document chunks.
    """
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    if os.path.exists(index_dir):
        logger.info("Loading existing FAISS index...")
        vectorstore = FAISS.load_local(index_dir, embeddings)
        vectorstore.add_texts(chunks)
    else:
        logger.info("Creating new FAISS index...")
        vectorstore = FAISS.from_texts(chunks, embeddings)

    vectorstore.save_local(index_dir)
    logger.info(f"Index saved at {index_dir}")


def main(data_dir: str = DATA_DIR, index_dir: str = INDEX_DIR):
    logger.info("Starting document indexing...")
    documents = load_documents(data_dir)
    if not documents:
        logger.warning("No documents found!")
        return

    chunks = chunk_texts(documents)
    build_faiss_index(chunks, index_dir)
    logger.info("Indexing complete ✅")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Index financial documents into FAISS")
    parser.add_argument("--data_dir", type=str, default=DATA_DIR, help="Path to corpus folder")
    parser.add_argument("--index_dir", type=str, default=INDEX_DIR, help="Path to save FAISS index")
    args = parser.parse_args()

    main(args.data_dir, args.index_dir)
