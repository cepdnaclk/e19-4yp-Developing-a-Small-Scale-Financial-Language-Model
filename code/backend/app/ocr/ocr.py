import fitz # PyMuPDF
import pytesseract
from PIL import Image
import io
from typing import List

def pdf_to_images(pdf_path: str, dpi: int = 300) -> List[Image.Image]:
doc = fitz.open(pdf_path)
imgs = []
for page in doc:
pix = page.get_pixmap(dpi=dpi)
img = Image.open(io.BytesIO(pix.tobytes("png")))
imgs.append(img)
return imgs


def ocr_image(img: Image.Image, lang: str = "eng") -> str:
return pytesseract.image_to_string(img, lang=lang)


def ocr_pdf(pdf_path: str, lang: str = "eng") -> str:
texts = []
for img in pdf_to_images(pdf_path):
texts.append(ocr_image(img, lang=lang))
return "\n".join(texts)
