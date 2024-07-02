---
layout: page
title: Stepic MLOps. Начало
description: Stepic MLOps. Начало
keywords: courses, stepic, mlops
permalink: /courses/stepik-mlops-beginning/
---

# [Stepic] MLOps. Начало [RUS, 2023]

<br/>

**Материалы на stepic**  
https://stepik.org/course/181476/promo

<br/>

**На youtube:**  
https://www.youtube.com/watch?v=skTh3tGksIQ&list=PLmA-1xX7IuzAixCe10sFhyTcyunSc5Zdi

<br/>

Медленно продолжаем изучать материал. Если есть предложения по улучшению, принимаются!

<br/>

## Используемые программы:

<br/>

### [Postgres](//gitops.ru/tools/containers/docker/db/postgresql/)

### [Airflow](/tools/airflow/)

### [MinIO](/tools/minio/)

<br/>

## 4. AirFlow

<br/>

### 01. DAG Hello World

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
    print("Hello, World")


task_init = PythonOperator(task_id = "init", python_callable = init, dag =  dag)

task_init
```

<br/>

```
$ airflow dags test mlops_dag_1
```

<br/>

### 02. Загрузка данных в таблицу postgres

<br/>

```
$ pip install numpy==1.26.4 pandas==2.1.4 scikit-learn==1.5.0 sqlalchemy==0.28.2 psycopg2-binary==2.9.9
```

<br/>

```
$ cd /home/marley/projects/dev/mlops
$ vi load-data.py
```

<br/>

```python
import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sqlalchemy import create_engine


# Получим датасет California housing
data = fetch_california_housing()

# Объединим фичи и таргет в один np.array
dataset = np.concatenate([data['data'], data['target'].reshape([data['target'].shape[0],1])],axis=1)

# Преобразуем в dataframe.
dataset = pd.DataFrame(dataset, columns = data['feature_names']+data['target_names'])

# Создадим подключение к базе данных postgres. Поменяйте на свой пароль yourpass
# engine = create_engine('postgresql://postgres:yourpass@localhost:5432/postgres')

engine = create_engine('postgresql://admin1:pA55w0rd123@postgres:5432/postgresdb')

# Сохраним датасет в базу данных
dataset.to_sql('california_housing', engine)

# Для проверки можно сделать:
pd.read_sql_query("SELECT * FROM california_housing", engine)
```

<br/>

```
$ python load-data.py
```

<br/>

```
// OK!
$ PGPASSWORD=pA55w0rd123 psql --host=localhost --username=admin1 --port=5432 --dbname=postgresdb -c 'SELECT * FROM california_housing'
```

<br/>

### 03. Train DAG

<br>

```python
import io
import json
import logging
import numpy as np
import pandas as pd
import pickle

from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, median_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler

from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


DEFAULT_ARGS = {
    #TO-DO: прописать аргументы
}

dag = DAG(#TO-DO: прописать аргументы)


_LOG = logging.getLogger()
_LOG.addHandler(logging.StreamHandler())

BUCKET = #TO-DO: your bucket
DATA_PATH = #TO-DO: your path
FEATURES = ["MedInc", "HouseAge", "AveRooms", "AveBedrms",
            "Population", "AveOccup", "Latitude", "Longitude"]
TARGET = "MedHouseVal"


def init() -> None:
    _LOG.info("Train pipeline started.")

def get_data_from_postgres() -> None:
   #TO-DO: Заполнить все шаги

    # Использовать созданный ранее PG connection

    # Прочитать все данные из таблицы california_housing

    # Использовать созданный ранее S3 connection

    # Сохранить файл в формате pkl на S3



def prepare_data() -> None:
    #TO-DO: Заполнить все шаги

    # Использовать созданный ранее S3 connection

    # Сделать препроцессинг
    # Разделить на фичи и таргет

    # Разделить данные на обучение и тест

    # Обучить стандартизатор на train

    # Сохранить готовые данные на S3

def train_model() -> None:
    #TO-DO: Заполнить все шаги

    # Использовать созданный ранее S3 connection

    # Загрузить готовые данные с S3

    # Обучить модель

    # Посчитать метрики

    # Сохранить результат на S3


def save_results() -> None:
    _LOG.info("Success.")


task_init = #TO-DO: написать оператор

task_get_data = #TO-DO: написать оператор

task_prepare_data = #TO-DO: написать оператор

task_train_model = #TO-DO: написать оператор

task_save_results = #TO-DO: написать оператор

#TO-DO: Архитектура DAG'а
```
