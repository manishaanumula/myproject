from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
from scripts.validate import validate_data


default_args = {
    'owner': 'Manisha',
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}


dag = DAG(
    dag_id='etl_snowflake_pipeline',
    default_args=default_args,
    schedule=None,
    catchup=False,
    description='End to End ETL using Airflow and Snowflake'
)


def extract_task():
    extract_data()


def transform_task():
    df = extract_data()
    transform_data(df)


def load_task():
    load_data()


def validate_task():
    validate_data()


extract = PythonOperator(
    task_id='extract_data',
    python_callable=extract_task,
    dag=dag
)

transform = PythonOperator(
    task_id='transform_data',
    python_callable=transform_task,
    dag=dag
)

load = PythonOperator(
    task_id='load_to_snowflake',
    python_callable=load_task,
    dag=dag
)

validate = PythonOperator(
    task_id='validate_data',
    python_callable=validate_task,
    dag=dag
)

extract >> transform >> load >> validate
