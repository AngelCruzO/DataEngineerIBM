# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Ramesh Sannareddy',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'ETL_Server_Access_Log_Processing',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(days=1),
)

# define the tasks

#define the task named extract_transform_and_load to call the shell script
#calling the shell script
extract_transform_and_load = BashOperator(
    task_id="extract_transform_and_load",
    bash_command="/home/project/airflow/dags/ETL_Server_Access_Log_Processing.sh ",
    dag=dag,
)

# task pipeline

extract_transform_and_load

'''
cp  ETL_Server_Access_Log_Processing.py $AIRFLOW_HOME/dags
cp  ETL_Server_Access_Log_Processing.sh $AIRFLOW_HOME/dags
cd airflow/dags
chmod 777 ETL_Server_Access_Log_Processing.sh
airflow dags list|grep "ETL_Server_Access_Log_Processing"
airflow tasks list ETL_Server_Access_Log_Processing
'''