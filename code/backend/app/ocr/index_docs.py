from pathlib import Path
from .rag.retriever import VectorStore
from .ocr.ocr import ocr_pdf


PLAIN_EXT = {".txt", ".md"}
PDF_EXT = {".pdf"}




def load_texts_from_dir(root: str) -> list[str]:
texts = []
for p in Path(root).rglob("*"):
if p.suffix.lower() in PLAIN_EXT:
texts.append(p.read_text(encoding="utf-8", errors="ignore"))
elif p.suffix.lower() in PDF_EXT:
texts.append(ocr_pdf(str(p)))
return texts


if __name__ == "__main__":
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--data_dir", required=True)
args = ap.parse_args()


vs = VectorStore()
docs = load_texts_from_dir(args.data_dir)
vs.build(docs)
print(f"Indexed {len(docs)} documents")
