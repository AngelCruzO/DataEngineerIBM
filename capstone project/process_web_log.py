#import the libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#DAG arguments
default_args = {
    'owner': 'Cruz Olvera Angel',
    'start_date': days_ago(0),
    'email': ['angelcp@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

#DAG definition
dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='Dag for web log',
    schedule_interval=timedelta(days=1),
)

#Extract IP
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -f1,14 accesslog.txt > /home/project/airflow/dags/capstone/extracted_data.txt',
    dag=dag,
)

#Transform data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v "198.46.149.143" home/project/airflow/dags/capstone/extracted_data.txt > home/project/airflow/dags/capstone/transformed_data.txt',
    dag=dag,
)

#load data
load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -cf weblog.tar transformed_data.txt',
    dag=dag,
)

#Pipeline
extract_data >> transform_data >> load_data