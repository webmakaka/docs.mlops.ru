---
layout: page
title: Курсы MLOPS
description: Курсы MLOPS
keywords: courses
permalink: /courses/
---

# Курсы MLOPS

<br/>

### [[Stepic] MLOps. Начало](/courses/stepik-mlops-beginning/)

https://stepik.org/course/181476/promo

<br/>

**На youtube:**

https://www.youtube.com/watch?v=skTh3tGksIQ&list=PLmA-1xX7IuzAixCe10sFhyTcyunSc5Zdi

<br/>

```
$ vi dags/mlops_dag_1.py
```

<br/>

```python
from datetime import timedelta
from typing import NoReturn
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

DEFAULT_ARGS = {
    "owner" : "Marley",
    "email" : "marley@example.com",
    "email_on_failure" : True,
    "email_on_retry" : False,
    "retry" : 3,
    "retry_delay" : timedelta(minutes=1)
}

dag = DAG(
    dag_id = "mlops_dag_1",
    schedule_interval = "0 1 * * *",
    start_date = days_ago(2),
    catchup = False,
    tags = ["mlops"],
    default_args = DEFAULT_ARGS
)

def init() -> NoReturn:
    print("Hello, World!")


task_init = PythonOperator(task_id = "init", python_callable = init, dag =  dag)

task_init
```

<br/>

```
$ airflow dags test mlops_dag_1
```

<br/>

### Загрузка данных в таблицу postgres
