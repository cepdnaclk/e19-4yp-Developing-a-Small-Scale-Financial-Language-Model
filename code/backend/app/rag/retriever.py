import faiss, os, numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Tuple
import pickle


EMB_MODEL = os.getenv("EMB_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
INDEX_PATH = os.getenv("INDEX_PATH", "./data/index/faiss.index")
STORE_PATH = os.getenv("STORE_PATH", "./data/index/store.pkl")


class VectorStore:
def __init__(self):
self.model = SentenceTransformer(EMB_MODEL)
self.index = None
self.texts: List[str] = []


def _emb(self, texts: List[str]) -> np.ndarray:
return np.array(self.model.encode(texts, normalize_embeddings=True))


def build(self, texts: List[str]):
self.texts = texts
X = self._emb(texts).astype('float32')
self.index = faiss.IndexFlatIP(X.shape[1])
self.index.add(X)
os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
faiss.write_index(self.index, INDEX_PATH)
with open(STORE_PATH, 'wb') as f:
pickle.dump(self.texts, f)


def load(self):
self.index = faiss.read_index(INDEX_PATH)
with open(STORE_PATH, 'rb') as f:
self.texts = pickle.load(f)


def search(self, query: str, k: int = 5) -> List[Tuple[str, float]]:
if self.index is None:
self.load()
q = self._emb([query]).astype('float32')
D, I = self.index.search(q, k)
return [(self.texts[i], float(D[0][j])) for j, i in enumerate(I[0]) if i != -1]
