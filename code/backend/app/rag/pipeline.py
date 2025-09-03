from .retriever import VectorStore
from .llm import generate


SYS_PROMPT = (
"You are a helpful financial analysis assistant. "
"Use the provided CONTEXT to answer the USER question accurately. "
"If unsure, say you don't know and suggest where to look."
)


def build_prompt(question: str, contexts: list[str]) -> str:
ctx_block = "\n---\n".join(contexts[:5])
return f"<|system|>\n{SYS_PROMPT}\n<|user|>\nCONTEXT:\n{ctx_block}\n\nQUESTION: {question}\n<|assistant|>"


def rag_answer(query: str, top_k: int = 5, max_tokens: int = 512):
vs = VectorStore()
hits = vs.search(query, k=top_k)
contexts = [t for t, _ in hits]
prompt = build_prompt(query, contexts)
out = generate(prompt, max_new_tokens=max_tokens)
# For chatty models the output may include the prompt; trim after assistant tag
if "<|assistant|>" in out:
out = out.split("<|assistant|>")[-1].strip()
return out, contexts
