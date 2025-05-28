from transformers import pipeline

# Load text
with open("full_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Load the question generation pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Sample questions (you can later automate this)
questions = [
    "What was the total revenue in 2023?",
    "What are the key business highlights?",
    "What is the net income reported?",
]

# Generate answers
for q in questions:
    result = qa_pipeline(question=q, context=text)
    print(f"Q: {q}")
    print(f"A: {result['answer']}\n")
