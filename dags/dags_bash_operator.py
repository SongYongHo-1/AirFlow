import datetime
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='dags_bash_operator',
    schedule='0 0 * * *',
    start_date=pendulum.datetime(2024, 7, 4, tz="Asis/Seoul"),
    catchup=False
    #dagrun_timeout=datetime.timedelta(minutes=60), ##60분 이상 수행 시 에러
    #tags=['example', 'example2'],
    #params={"example_key": "example_value"},
) as dag:
    
    # [START howto_operator_bash]
    bash_t1 = BashOperator( #Task명
        task_id='bash_t1', 
        bash_command='echo whoami',
    )
    # [END howto_operator_bash]

    # [START howto_operator_bash]
    bash_t2 = BashOperator( #Task명
        task_id='bash_t2', 
        bash_command='echo $HOSTNAME',
    )
    # [END howto_operator_bash]    

    bash_t1 >> bash_t2 #Task 수행 순서