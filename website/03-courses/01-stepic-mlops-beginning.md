---
layout: page
title: Курсы MLOPS
description: Курсы MLOPS
keywords: courses
permalink: /courses/stepik-mlops-beginning/
---

# Курсы MLOPS

<br/>

### [Stepic] MLOps. Начало

https://stepik.org/course/181476/promo

<br/>

**На youtube:**

https://www.youtube.com/watch?v=skTh3tGksIQ&list=PLmA-1xX7IuzAixCe10sFhyTcyunSc5Zdi

<br/>

### [Postgres](//gitops.ru/tools/containers/docker/db/postgresql/)

### [Airflow](/tools/airflow/)

### [MinIO](/tools/minio/)

<br/>

### 4. AirFlow

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

### Часть 3. Создать новый юпитер-ноутбук и в нём выполнить код ниже.

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
engine = create_engine('postgresql://postgres:yourpass@localhost:5432/postgres')

# Сохраним датасет в базу данных
dataset.to_sql('california_housing', engine)

# Для проверки можно сделать:
pd.read_sql_query("SELECT * FROM california_housing", engine)
```

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
