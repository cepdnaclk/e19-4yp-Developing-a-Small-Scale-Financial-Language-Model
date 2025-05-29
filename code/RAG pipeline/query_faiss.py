from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Step 1: Load the same model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 2: Load your document texts
import os
import json

folder_path = "/home/kasuni/uploads"
docs = []

for fname in os.listdir(folder_path):
    if fname.endswith(".txt"):
        with open(os.path.join(folder_path, fname), "r", encoding="utf-8") as file:
            content = file.read().strip()
            docs.append({"filename": fname, "content": content})

# Step 3: Create embeddings again (must match the FAISS index order!)
texts = [doc["content"] for doc in docs]
embeddings = model.encode(texts)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Step 4: Get a query from the user
query = input("Enter your financial query: ")
query_embedding = model.encode([query])

# Step 5: Search the index
k = 1  # Top 1 result
D, I = index.search(np.array(query_embedding), k)

# Step 6: Show result
print("\nTop result:")
top_idx = I[0][0]
print(f"File: {docs[top_idx]['filename']}")
print("Excerpt:\n", docs[top_idx]["content"][:1000])  # Print first 1000 chars
