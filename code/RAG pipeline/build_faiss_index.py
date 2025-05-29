from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# Step 1: Read all text files into docs
folder_path = "/home/kasuni/uploads"
docs = []

for fname in os.listdir(folder_path):
    if fname.endswith(".txt"):
        with open(os.path.join(folder_path, fname), "r", encoding="utf-8") as file:
            content = file.read().strip()
            docs.append({"filename": fname, "content": content})

# Step 2: Prepare texts for embeddings
texts = [doc["content"] for doc in docs]

# Step 3: Load sentence transformer model and encode
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts)

# Step 4: Create FAISS index and add embeddings
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

print(f"FAISS index created with {index.ntotal} vectors")
