import pytest
from code.backend import index_docs
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


@pytest.fixture
def sample_docs(tmp_path):
    # Create a sample text file
    test_file = tmp_path / "sample.txt"
    test_file.write_text("This is a financial report. Revenue increased in 2023.")
    return str(tmp_path)


def test_load_documents_txt(sample_docs):
    docs = index_docs.load_documents(sample_docs)
    assert len(docs) == 1
    assert "financial report" in docs[0][1]


def test_chunk_texts():
    docs = [("file1.txt", "This is a test. " * 50)]
    chunks = index_docs.chunk_texts(docs)
    assert len(chunks) > 1


def test_build_faiss_index(tmp_path):
    chunks = ["Bank profits grew by 10%", "Inflation rose in 2023"]
    index_dir = tmp_path / "vectorstore"
    index_docs.build_faiss_index(chunks, str(index_dir))

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    store = FAISS.load_local(str(index_dir), embeddings)
    results = store.similarity_search("profits")
    assert len(results) > 0
