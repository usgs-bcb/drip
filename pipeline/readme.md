# Data Processing Pipeline

This data pipeline is setup with apache airflow. 

### Configuration

Change the config-example.yaml file to config.yaml and add your direct resources (paths, models ,etc)

### Workflow

task_spacy_en >> task_spacy_dam >> task_removal_terms >> filter

### Running

```
export AIRFLOW_HOME=~/airflow

# install from pypi using pip
pip install apache-airflow

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 9000

airflow scheduler
```

### UI

http://localhost:9000/admin/airflow/

