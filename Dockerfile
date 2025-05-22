FROM apache/airflow:2.11.0 AS builder
WORKDIR /theguardian
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# apache-airflow==${2.11.0}

# # ---------- Stage 1: Builder ----------
# FROM python:3.12-slim AS builder

# WORKDIR /build

# # Install system build dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential gcc && \
#     rm -rf /var/lib/apt/lists/*

# # Copy requirements and install packages to a temp folder
# COPY requirements.txt .
# RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# # ---------- Stage 2: Final Airflow Image ----------
# FROM apache/airflow:2.11.0

# # Switch to root to install copied files
# USER root

# # Copy installed Python packages from builder
# COPY --from=builder /install /usr/local

# # Set working directory for your app
# WORKDIR /theguardian

# # Switch back to airflow user for security
# USER airflow
