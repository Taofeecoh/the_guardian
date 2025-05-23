import pipeline as p
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id='the-guardian',
    description='the guardian pipeline'
)

extract_data = PythonOperator(
    task_id = 'extract_data',
    python_callable=p.complete_etl,
    dag=dag
    )

extract_data