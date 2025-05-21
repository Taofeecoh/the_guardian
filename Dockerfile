FROM apache/airflow:2.10.0
WORKDIR /theguardian/
COPY requirements.txt .
RUN pip install -r requirements.txt
