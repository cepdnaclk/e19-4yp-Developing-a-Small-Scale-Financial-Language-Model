# Use official Python slim image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install system dependencies for OCR (Tesseract, poppler)
RUN apt-get update && \
    apt-get install -y tesseract-ocr poppler-utils && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY ../backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY ../backend /app

# Expose FastAPI port
EXPOSE 8000

# Default command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
