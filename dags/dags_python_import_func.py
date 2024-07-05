from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp

with DAG(
    dag_id='dags_python_import_func',
    schedule='30 6 * * *',
    start_date=pendulum.datetime(2024, 7, 4, tz="Asia/Seoul"),
    catchup=False
    #dagrun_timeout=datetime.timedelta(minutes=60), ##60분 이상 수행 시 에러
    #tags=['example', 'example2'],
    #params={"example_key": "example_value"},
) as dag:
    
    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable=get_sftp
    )

    py_t1