# Data Processing Pipeline

In efforts for creating reproducible and have long running sequential tasks this pipeline is setup using Apache Airflow. 

### Configuration

Edit the config.yaml file to direct resources

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

