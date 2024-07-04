---
layout: page
title: Установка AirFlow
description: Установка AirFlow
keywords: linux, airflow, setup
permalink: /tools/airflow/
---

# Установка AirFlow

<br/>

Делаю:  
2023.06.30

<br/>

https://github.com/apache/airflow

<br/>

```
$ sudo vi /etc/profile.d/airflow.sh
```

<br/>

```
#### AIRFLOW ########################

export AIRFLOW_HOME=/home/marley/projects/dev/mlops/airflow
export AIRFLOW_CONFIG=${AIRFLOW_HOME}/airflow.cfg

#### AIRFLOW ########################
```

<br/>

```
$ sudo chmod +x /etc/profile.d/airflow.sh
$ source /etc/profile.d/airflow.sh
```

<br/>

```
$ pip install 'apache-airflow==2.9.2' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.8.txt"
```

<br/>

```
// sqlite
$ airflow db init
```

<br/>

```
// admin / admin
$ airflow users create \
        --username admin \
        --firstname admin \
        --lastname admin \
        --role Admin \
        --email admin@example.org
```

<br/>

```
$ mkdir -p /home/marley/projects/dev/mlops/airflow/dags
```

<br/>

```
$ vi ${AIRFLOW_HOME}/dags/mlops_dag_1.py
```

<br/>

```python
from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator

def print_hello():
    print("Hello World")

with DAG(
    dag_id="hello_world",
    start_date=datetime(2023,1,1),
    schedule_interval="@once",
    catchup=False) as dag:

    hello_task = PythonOperator(
        task_id="hello_operator",
        python_callable=print_hello
    )

    hello_task
```

<br/>

```
$ airflow config get-value core DAGS_FOLDER
/home/marley/projects/dev/mlops/airflow/dags
```

<br/>

```
$ airflow dags list
```

<br/>

```
$ cd /home/marley/.local/lib/python3.10/site-packages/airflow/example_dags
$ rm -rf *
```

<br/>

```
$ airflow scheduler
```

<br/>

```
$ airflow dags list
```

<br/>

```
$ airflow dags test hello_world
```

<br/>

```
$ airflow webserver -p 8080
```

<br/>

```
// admin / admin
http://localhost:8080/
```

<!--
```
$ airflow config get-value scheduler scheduler_health_check_threshold
$ airflow config get-value scheduler scheduler_heartbeat_sec
``` -->

<br/>

### Если нужно включить test_connection

```
$ vi $AIRFLOW_HOME/airflow.cfg
```

<br/>

```
test_connection = Disabled
меняю на
test_connection = Enabled
```

<br/>

### Running Airflow in Docker

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
