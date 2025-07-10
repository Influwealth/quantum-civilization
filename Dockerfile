FROM python:3.11-bullseye

WORKDIR /app

# Install build toolchain
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Disable pip isolation and cache — bypass wheel build
ENV PIP_NO_BUILD_ISOLATION=1
ENV PIP_NO_USE_PEER_DEPENDENCIES=1

ENV CXX="g++"
ENV CC="gcc"
ENV CFLAGS="-O2"
ENV CXXFLAGS="-O2 -std=c++11"
ENV LDFLAGS="-lm"

# Core Python build packages
RUN pip install --upgrade pip setuptools wheel \
    && pip install "cython<3.0" \
    && pip install --no-build-isolation --no-cache-dir "pyyaml==6.0.1"

# Confirm contents before pip install
COPY requirements.txt .
RUN echo "🔍 Requirements.txt:" && cat requirements.txt
RUN pip install --no-deps --no-cache-dir -r requirements.txt || true

# Inject precompiled hnswlib module manually
COPY wheels/hnswlib/hnswlib.cpython-311-x86_64-linux-gnu.so /usr/local/lib/python3.11/site-packages/hnswlib/
COPY wheels/hnswlib/hnswlib-0.8.0.dist-info /usr/local/lib/python3.11/site-packages/hnswlib-0.8.0.dist-info/

# Copy app source
COPY . .

# Run FastAPI cockpit HUD
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
