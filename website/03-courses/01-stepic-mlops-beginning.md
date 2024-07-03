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

```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.4 LTS
Release:	22.04
Codename:	jammy

$ python --version
Python 3.10.12
```

<br/>

### [Postgres](//gitops.ru/tools/containers/docker/db/postgresql/)

### [Airflow](/tools/airflow/)

### [MinIO](/tools/minio/)

<br/>

## 4. AirFlow

<br/>

Делаю:  
2024.07.03

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


task_init = PythonOperator(task_id = "init", python_callable = init, dag = dag)

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
// pandas 2.1.0
// sqlalchemy==1.4.36
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

```
Airflow -> Admin -> Connections

Connection id: pg_connection
Connection Type: Postgres
Host: localhost
Schema: postgresdb
Login admin1
Password: pA55w0rd123
Port: 5432
```

<br>

```
$ pip install apache-airflow-providers-postgres
$ pip install apache-airflow-providers-amazon
```

<br/>

```
$ vi dags/train_dag.py
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
    "owner" : "Ryabukhin Alex",
    "email" : "santolyich@gmail.com",
    "email_on_failure" : True,
    "email_on_retry" : False,
    "retry" : 3,
    "retry_delay" : timedelta(minutes=1)
}

dag = DAG(
    dag_id = "train",
    schedule_interval = "0 1 * * *",
    start_date = days_ago(2),
    catchup = False,
    tags = ["mlops"],
    default_args = DEFAULT_ARGS
)

_LOG = logging.getLogger()
_LOG.addHandler(logging.StreamHandler())

BUCKET = "mlops-bucket"
DATA_PATH = "datasets/california_housing.pkl"
FEATURES = ["MedInc", "HouseAge", "AveRooms", "AveBedrms",
            "Population", "AveOccup", "Latitude", "Longitude"]
TARGET = "MedHouseVal"

def init() -> None:
    _LOG.info("Train pipeline started!")

def get_data_from_postgres() -> None:

    # Использовать созданный ранее PG connection
    pg_hook = PostgresHook("pg_connection")
    conn = pg_hook.get_conn()

    # Прочитать все данные из таблицы california_housing
    data = pd.read_sql_query("SELECT * FROM california_housing", conn)

    # Использовать созданный ранее S3 connection
    s3_hook = S3Hook("s3_connection")
    session = s3_hook.get_session("ru-central")
    resource = session.resource("s3")

    # Сохранить файл в формате pkl на S3
    pickle_byte_obj = pickle.dumps(date)
    resource.Object(BUCKET, DATA_PATH).put(Body=pickle_byte_obj)

    _LOG.info("Data download finished!")


def prepare_data() -> None:
    # Использовать созданный ранее S3 connection
    s3_hook = S3Hook("s3_connection")

    # Сделать препроцессинг
    file = s3_hook.download_file(key = DATA_PATH, bucket_name = BUCKET)
    data = pd.read_pickle(file)

    # Разделить на фичи и таргет
    X, y = data[FEATURES], data[TARGET]

    # Разделить данные на обучение и тест
    X_train, X_text, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

    # Обучить стандартизатор на train
    scaler = StandardScaler()
    X_train_fitted = scalar.fit_transform(X_train)
    X_test_fitted = scaler.transform(X_test)

    # Сохранить готовые данные на S3
    session = s3_hook.get_session("ru-central")
    resource = session.resource("s3")

    for name, data in (zip(["X_train", "X_test", "y_train", "y_test"],
                           ["X_train_fitted, X_test_fitted, y_train, y_test"])):
        pickle_byte_obj = pickle.dumps(data)
        resource.Object(BUCKET, f"dataset/{name}.pkl").put(Body=pickle_byte_obj)


    _LOG.info("Data download finished!")



def train_model() -> None:
    # Использовать созданный ранее S3 connection
    s3_hook = S3Hook("s3_connection")

    # Загрузить готовые данные с S3
    data = {}
    for name in ["X_train", "X_test", "y_train", "y_test"]:
        file = s3_hook.download_file(key = f"dataset/{name}.pkl", bucket_name = BUCKET)
        data[name] = pd.read_pickle(file)

    # Обучить модель
    modle = RandomForestRegressor()
    modle.fit(data["X_train"], data["y_train"])
    predicton = model.predict(data["X_test"])

    # Посчитать метрики
    result = {}
    result["r2_score"] = r2_score(data["y_test"], prdictoin)
    result["rmse"] = mean_squared_error(data["y_test"], pridiction)**0.5
    result["mse"] = median_absolute_error(data["y_test"], pridiction)

    # Сохранить результат на S3
    data = datetime.now().strftime("%Y_%m_%d_%H")
    session = s3_hook.get_session("ru-central")
    resource = session.resource("s3")
    json_byte_object = json.dumps(result)
    resource.Object(BUCKET, f"results/{date}.json").put(Body=json_byte_object)

    _LOG.info("Model training finished!")


def save_results() -> None:
    _LOG.info("Success!")


task_init = PythonOperator(task_id="init", python_callable=init, dag=dag)
task_get_data = PythonOperator(task_id="get_data", python_callable=get_data_from_postgres, dag=dag)
task_prepare_data = PythonOperator(task_id="prepare_data", python_callable=prepare_data, dag=dag)
task_train_model = PythonOperator(task_id="train_model", python_callable=train_model, dag=dag)
task_save_results = PythonOperator(task_id="save_results", python_callable=save_results, dag=dag)
```
