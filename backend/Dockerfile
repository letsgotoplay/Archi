# Dockerfile for Backend Service of InnerSource Hub PoC
# This Dockerfile sets up the Python environment and installs dependencies.

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
