import datetime
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='dags_conn_test',
    schedule='0 0 * * *',
    start_date=pendulum.datetime(2024, 7, 4, tz="Asia/Seoul"),
    catchup=False
    #dagrun_timeout=datetime.timedelta(minutes=60), ##60분 이상 수행 시 에러
    #tags=['example', 'example2'],
    #params={"example_key": "example_value"},
) as dag:
    
    t1 = EmptyOperator( task_id = "t1")
    t2 = EmptyOperator( task_id = "t2")
    t3 = EmptyOperator( task_id = "t3")
    t4 = EmptyOperator( task_id = "t4")
    t5 = EmptyOperator( task_id = "t5")
    t6 = EmptyOperator( task_id = "t6")
    t7 = EmptyOperator( task_id = "t7")
    t8 = EmptyOperator( task_id = "t8")

    t1 >> [t2,t3] >> t4
    t5 >> t4
    [t4,t7] >> t6 >> t8
