import os

folder_path = "/home/kasuni/uploads"
docs = []

for fname in os.listdir(folder_path):
    if fname.endswith(".txt"):
        with open(os.path.join(folder_path, fname), "r", encoding="utf-8") as file:
            content = file.read().strip()
            docs.append({"filename": fname, "content": content})

# Print preview
for doc in docs:
    print(doc["filename"], "->", len(doc["content"]), "chars")
