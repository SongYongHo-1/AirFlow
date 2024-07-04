import datetime
import pendulum
import random
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='dags_python_operator',
    schedule='30 6 * * *',
    start_date=pendulum.datetime(2024, 7, 4, tz="Asia/Seoul"),
    catchup=False
    #dagrun_timeout=datetime.timedelta(minutes=60), ##60분 이상 수행 시 에러
    #tags=['example', 'example2'],
    #params={"example_key": "example_value"},
) as dag:
    
    def select_fruit():
        furit = ['APPLE','BANANA','ORANGE','ABOACADO']
        rand_int = random.randint(0,3)
        print(furit[rand_int])

    py_t1 = PythonOperator(
        task_id = 'py_t1',
        python_callable=select_fruit
    )

    py_t1