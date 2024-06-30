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
2023.07.07

<br/>

https://github.com/apache/airflow

<br/>

```
$ pip install 'apache-airflow==2.6.2' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.2/constraints-3.8.txt"
```

<br/>

```
$ export AIRFLOW_HOME=/home/marley/projects/dev/python/airflow
```

<br/>

```
// sqlite
$ airflow db init
```

<br/>

```
 $ airflow users create \
          --username admin \
          --firstname admin \
          --lastname admin \
          --role Admin \
          --email admin@example.org
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

<br/>

### Running Airflow in Docker

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
