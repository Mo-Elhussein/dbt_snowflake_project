from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from typing import List, Dict  # ✅ Added for backward-compatible type hints

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 25),  # Change as needed
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'dbt_snowflake_workflow',
    default_args=default_args,
    description='Run dbt models using dbt Core',
    schedule_interval='@daily',  # Run daily
    catchup=False,
)

# Define the path to your dbt project
DBT_PROJECT_DIR = "E:\\DBT_Project_Snowflake"  # ✅ Removed extra space, fixed path

# Task 1: Run dbt models
dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command=f'cd "{DBT_PROJECT_DIR}" && dbt run',
    dag=dag,
)

# Task 2: Run dbt tests after models are built
dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command=f'cd "{DBT_PROJECT_DIR}" && dbt test',
    dag=dag,
)

# Define task dependencies
dbt_run >> dbt_test  # dbt_run must finish before dbt_test starts
