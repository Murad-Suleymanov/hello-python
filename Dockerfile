# Python FastAPI Docker Image
FROM python:3.12-slim

WORKDIR /app

# Dependencies + application (tək layer — kiçik layer sayını azaldır)
COPY requirements.txt main.py ./
RUN pip install --no-cache-dir -r requirements.txt

# Port
EXPOSE 8000

# Run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
