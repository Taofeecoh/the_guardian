FROM apache/airflow:2.11.0 AS builder
WORKDIR /theguardian
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

