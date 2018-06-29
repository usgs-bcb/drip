import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    "owner": "Brandon",
    "start_date": dt.datetime(2018, 6, 1),
    "retries": 2,
    "retry_delay": dt.timedelta(minutes=2),
}


with DAG(
    "drip_preprocessing",
    default_args=default_args,
    schedule_interval="0 0 * * 0"  #"@weekly",
) as dag:

    task_spacy_en = BashOperator(
        task_id="task_spacy_en",
        bash_command="python spacy_english.py",
        retries=1,
    )

    task_spacy_dam = BashOperator(
        task_id="task_spacy_dam",
        bash_command="python spacy_dam.py",
        retries=1,
    )

    task_removal_terms = BashOperator(
        task_id="task_removal_terms",
        bash_command="python removal_terms.py",
        retries=1,
    )

    task_filter_output = BashOperator(
        task_id="task_filter_output",
        bash_command="python filter_process.py",
        retries=1,
    )


task_spacy_en >> task_spacy_dam >> task_removal_terms >> task_filter_output
