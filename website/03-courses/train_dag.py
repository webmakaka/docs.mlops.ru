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
    "owner" : "Marley",
    "email" : "marley@example.com",
    "email_on_failure" : True,
    "email_on_retry" : False,
    "retry" : 3,
    "retry_delay" : timedelta(minutes=1)
}

dag = DAG(
    dag_id = "mlops_train",
    schedule_interval = "0 1 * * *",
    start_date = days_ago(2),
    catchup = False,
    tags = ["mlops"],
    default_args = DEFAULT_ARGS
)

_LOG = logging.getLogger()
_LOG.addHandler(logging.StreamHandler())

BUCKET = "mlops-bucket-marley"
DATA_PATH = "datasets/california_housing.pkl"
FEATURES = ["MedInc", "HouseAge", "AveRooms", "AveBedrms",
            "Population", "AveOccup", "Latitude", "Longitude"]
TARGET = "MedHouseVal"

def init() -> None:
    _LOG.info("[LOG] Train pipeline started!")

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
    pickle_byte_obj = pickle.dumps(data)
    resource.Object(BUCKET, DATA_PATH).put(Body=pickle_byte_obj)

    _LOG.info("[LOG] Data download finished!")


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


    _LOG.info("[LOG] Data download finished!")


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

    _LOG.info("[LOG] Model training finished!")


def save_results() -> None:
    _LOG.info("[LOG] Success!")

task_init = PythonOperator(task_id="init", python_callable=init, dag=dag)
task_get_data = PythonOperator(task_id="get_data", python_callable=get_data_from_postgres, dag=dag)
task_prepare_data = PythonOperator(task_id="prepare_data", python_callable=prepare_data, dag=dag)
task_train_model = PythonOperator(task_id="train_model", python_callable=train_model, dag=dag)
task_save_results = PythonOperator(task_id="save_results", python_callable=save_results, dag=dag)

task_init >> task_get_data >> task_prepare_data >> task_train_model >> task_save_results
