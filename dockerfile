FROM python:3.11-slim
RUN pip install fastapi==0.104.1 uvicorn[standard]==0.24.0 python-multipart==0.0.6
COPY . /app
WORKDIR /app
EXPOSE 10000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]