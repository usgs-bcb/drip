# Data Processing Pipeline

This data pipeline is setup with apache airflow. The purpose of this pipeline inputs a GeoDeepDive export, performs additional natural language processing, ETL and produces a csv representing the data in a pandas dataframe.

### Configuration

Re-name the config-example.yaml file to config.yaml, then and add your full paths for nlp models and files (the airflow bashoperator seems to require this from where it executes)

__NOTE__ -- the config file sometimes produces failures when running, so within each task explicitly define the path. For simplicity I saved this in my default airflow directory.

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

