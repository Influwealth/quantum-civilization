# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Preinstall build tools
RUN pip install --upgrade pip setuptools wheel \
    && pip install "cython<3.0" \
    && pip install --no-build-isolation "pyyaml==6.0.1"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
