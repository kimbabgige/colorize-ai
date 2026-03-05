FROM python:3.11-slim

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install fastapi uvicorn python-multipart pillow opencv-python-headless

COPY . /app
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
