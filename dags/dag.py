from datetime import datetime, timedelta

import pipeline as p
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'taofeecoh',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 27),
    'email': ['adesanutaofeecoh@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '30 6,18,23 * * *',
}


dag = DAG(
    dag_id='the-guardian',
    description='dag that runs a pipeline at 6:30am, 6:30pm, and 11:30pm',
    default_args=default_args
    #schedule_interval='30 6,18,23 * * *',
    #dagrun_timeout=timedelta(minutes=5.0)
)

extract_data = PythonOperator(
    task_id = 'extract_data',
    python_callable=p.complete_etl,
    dag=dag
    )

extract_data