---
layout: page
title: Установка MLFlow
description: Установка MLFlow
keywords: mlflow, postgres, setup
permalink: /tools/mlflow/
---

# Установка MLFlow

<br/>

Делаю (по памяти, требуется проверка):  
\*.2023

<br/>

# Установка MLFlow с подключением к Postgres

<br/>

Создайте и активируйте виртуальное окружение для сервиса:

<br/>

```
$ export PYTHON_VERSION=3.8.12
$ export PROJECT_NAME=mlflow
$ pyenv virtualenv ${PYTHON_VERSION} ${PROJECT_NAME}-env
$ source /root/.pyenv/versions/${PROJECT_NAME}-env/bin/activate
```

<br/>

Инсталлируйте необходимые библиотеки

```
$ pip install mlflow==1.22.* psycopg2-binary==2.8.* protobuf==3.20.*
```

<br/>

Cоздайте файл service-start.sh с содержимым:

<br/>

```bash
#!/bin/sh

export PYTHON_VERSION=3.8.12
export PROJECT_NAME=mlflow

source /root/.pyenv/versions/${PROJECT_NAME}-env/bin/activate

# DB_HOST="${DB_HOST}"
# DB_DATABASE="${DB_DATABASE}"
# DB_SCHEMA="${DB_SCHEMA}"
# DB_LOGIN="${DB_LOGIN}"
# DB_PASSWORD="${DB_PASSWORD}"
# DEFAULT_ARTIFACT_ROOT="${DEFAULT_ARTIFACT_ROOT}"

DB_HOST="localhost"
DB_DATABASE="mydb"
DB_SCHEMA="mlflow"
DB_LOGIN="postgres"
DB_PASSWORD="postgres"
DEFAULT_ARTIFACT_ROOT="ftp://username:password@host/"

printf "Env\n"
printf "\n"
printf "DB_HOST"
printf "\n"
printf "$DB_HOST"
printf "\n"
printf "\n"
printf "DB_DATABASE"
printf "\n"
printf "$DB_DATABASE"
printf "\n"
printf "\n"
printf "DB_SCHEMA"
printf "\n"
printf "$DB_SCHEMA"
printf "\n"
printf "\n"
printf "DB_LOGIN"
printf "\n"
printf "$DB_LOGIN"
printf "\n"
printf "\n"
printf "DB_PASSWORD"
printf "\n"
printf "$DB_PASSWORD"
printf "\n"
printf "\n"
printf "DEFAULT_ARTIFACT_ROOT"
printf "\n"
printf "$DEFAULT_ARTIFACT_ROOT"
printf "\n"

cd /opt/services/mlflow

cmd="mlflow server --backend-store-uri postgresql://$DB_LOGIN:$DB_PASSWORD@$DB_HOST:5432/$DB_DATABASE?options=-csearch_path%3D$DB_SCHEMA --default-artifact-root $DEFAULT_ARTIFACT_ROOT --host 0.0.0.0 > /opt/services/logs/mlflow.log &"

printf "\n"
printf "cmd"
printf "\n"
echo "$cmd"
printf "\n"

printf "\n"
printf "RUN"
printf "\n"

eval $cmd

deactivate
```

<br/>

Cоздайте файл service-stop.sh с содержимым:

```bash
#!/bin/sh

cd /opt/services/mlflow
pkill -9 -f mlflow
```

<br/>

Установите для скриптов права для выполнения

```
$ chmod +x ./service-start.sh
$ chmod +x ./service-stop.sh
```
