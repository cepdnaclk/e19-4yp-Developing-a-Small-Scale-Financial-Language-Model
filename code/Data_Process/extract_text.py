import fitz  # PyMuPDF

doc = fitz.open("Financial Statement 2023-2024.pdf")
full_text = ""

for page in doc:
    full_text += page.get_text()

with open("full_text.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Text extracted and saved to full_text.txt")
