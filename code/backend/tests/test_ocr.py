import pytest
from code.backend import ocr


def test_extract_text_from_pdf(sample_pdf_bytes):
    text = ocr.extract_text_from_pdf(sample_pdf_bytes)
    assert isinstance(text, str)
    # We can’t guarantee exact OCR, but check non-empty
    assert len(text) > 0


# Fixture: create a tiny sample PDF
@pytest.fixture
def sample_pdf_bytes(tmp_path):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    pdf_path = tmp_path / "sample.pdf"
    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    c.drawString(100, 750, "Revenue increased in 2023")
    c.save()

    with open(pdf_path, "rb") as f:
        return f.read()
