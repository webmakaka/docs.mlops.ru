---
layout: page
title: Big Data on Kubernetes
description: Big Data on Kubernetes
keywords: Big Data on Kubernetes
permalink: /books/big-data-on-kubernetes/
---

<br/>

# [Book][BooNeylson Crepaldek] Big Data on Kubernetes [ENG, 2024]

<br/>

https://github.com/webmakaka/Bigdata-on-Kubernetes

<br/>

## Part 2: Big Data Stack

### 04. The Modern Data Stack

### 05. Big Data Processing with Apache Spark

<br/>

Делаю:  
2025.04.12

<br/>

```
$ java --version
openjdk 11.0.26 2025-01-21
```

<br/>

```
$ vi /etc/hosts
127.0.0.1 postgres
```

<br/>

```
$ export PYTHON_VERSION=3.8.12
$ export PROJECT_NAME=big_data
```

<br/>

```
$ pip install pyspark
$ spark-submit --version
```

<br/>

```
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.5
      /_/
Using Scala version 2.12.18, OpenJDK 64-Bit Server VM, 11.0.26
```

<br/>

```
$ git clone git@github.com:webmakaka/Bigdata-on-Kubernetes.git
```

<br/>

```
$ pip install jupyterlab
$ jupyter lab
```

<br/>

```
$ cd Bigdata-on-Kubernetes/Chapter05/
```

<br/>

```
$ pip install jupyterlab
$ pip install requests
```

<br/>

```
$ cd Bigdata-on-Kubernetes/Chapter05/\
$ python get_titanic_data.py
$ python get_imdb_data.py
```

<br/>

```
$ jupyter lab
```

<br/>

```
run -> read_titanic_dataset.ipynb
run -> analyzing_imdb_data.ipynb
```

<br/>

http://localhost:4040/jobs/

<br/>

### 06. Building Pipelines with Apache Airflow

Install the Astro CLI

https://docs.astronomer.io/astro/cli/install-cli

<br/>

```
$ curl -sSL install.astronomer.io | sudo bash -s
```

<br/>

```
$ mkdir airflow
$ cd airflow/

$ astro dev init
$ astro dev start
```

<br/>

```
// admin / admin
http://localhost:8080
```

<br/>

```
$ astro dev kill
```

<br/>

```
$ cd Chapter06/dags
$ cp ./* airflow/dags/
$ astro dev start
```

Имеет 2 DAG

1. Демо
2. Записывает данные в базу postgres и в облако AWS (если у вас есть такая возможность)

<br/>

При старте ошибка DAG, нужно Airflow -> Admin -> Variables. Добавить переменные см. по коду какие нужны.

<br/>

При старте airflow поднимается база postgres, к которой можно подключиться

// postgres / postgres
// localhost

<br/>

Airflow -> Admin -> Connections

<br/>

```
$ astro dev kill
```

<br/>

### 07. Apache Kafka for Real-Time Events and Data Ingestion

```
$ cd Chapter07/multinode
```

<br/>

```
$ docker-compose up -d
```

<br/>

```
$ docker ps
CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS         PORTS     NAMES
9d154c46ff2e   confluentinc/cp-kafka:7.6.0       "/etc/confluent/dock…"   2 minutes ago   Up 2 minutes             multinode-kafka-1-1
eeb748d35702   confluentinc/cp-kafka:7.6.0       "/etc/confluent/dock…"   2 minutes ago   Up 2 minutes             multinode-kafka-3-1
d949e54e0ecc   confluentinc/cp-kafka:7.6.0       "/etc/confluent/dock…"   2 minutes ago   Up 2 minutes             multinode-kafka-2-1
7151f56d6d40   confluentinc/cp-zookeeper:7.6.0   "/etc/confluent/dock…"   2 minutes ago   Up 2 minutes             multinode-zookeeper-2-1
d1ab8513b73d   confluentinc/cp-zookeeper:7.6.0   "/etc/confluent/dock…"   2 minutes ago   Up 2 minutes             multinode-zookeeper-3-1
f2936115277b   confluentinc/cp-zookeeper:7.6.0   "/etc/confluent/dock…"   2 minutes ago   Up 2 minutes             multinode-zookeeper-1-1
```

<br/>

```
$ docker logs multinode-kafka-1-1
```

<br/>

```
$ CONTAINER_NAME=multinode-kafka-1-1
$ docker exec -it $CONTAINER_NAME bash
```

<br/>

```
$ BOOTSTRAP_SERVER=localhost:19092
$ TOPIC=mytopic
$ GROUP=mygroup
```

<br/>

```
$ kafka-topics --create --bootstrap-server $BOOTSTRAP_SERVER --replication-factor 3 --partitions 3 --topic $TOPIC
```

<br/>

```
$ kafka-topics --list --bootstrap-server $BOOTSTRAP_SERVER
```

<br/>

```
$ kafka-topics --bootstrap-server $BOOTSTRAP_SERVER --describe --topic $TOPIC
```

<br/>

```
Topic: mytopic	TopicId: FDSRMlR1SGaDzIhi5x2fEQ	PartitionCount: 3	ReplicationFactor: 3	Configs:
	Topic: mytopic	Partition: 0	Leader: 3	Replicas: 3,1,2	Isr: 3,1,2
	Topic: mytopic	Partition: 1	Leader: 1	Replicas: 1,2,3	Isr: 1,2,3
	Topic: mytopic	Partition: 2	Leader: 2	Replicas: 2,3,1	Isr: 2,3,1
```

<br/>

```
$ kafka-console-producer --broker-list $BOOTSTRAP_SERVER --topic $TOPIC
```

<br/>

**+1 Terminal**

```
$ CONTAINER_NAME=multinode-kafka-1-1
$ docker exec -it $CONTAINER_NAME bash
```

<br/>

```
$ BOOTSTRAP_SERVER=localhost:19092
$ TOPIC=mytopic
```

<br/>

```
$ kafka-console-consumer --bootstrap-server $BOOTSTRAP_SERVER --topic $TOPIC --from-beginning
```

<br/>

```
$ docker-compose down
```

<br/>

**Streaming from a database with Kafka Connect**

```
$ cd Chapter07/connect/kafka-connect-custom-image
$ cd kafka-connect-custom-image
$ docker build -t connect-custom:1.0.0 .
$ cd ../
```

<br/>

```
$ vi .env_kafka_connect
```

<br/>

```
$ docker-compose up -d
```

<br/>

```
$ export PROJECT_NAME=big_data
$ source ${PYENV_ROOT}/versions/${PROJECT_NAME}-env/bin/activate
```

<br/>

```
// Добавить данные в базу postgres
$ cd simulations
$ pip install -r ./simulations/requirements.txt
$ python simulations/make_fake_data.py

// Завершить спустя какое-то количество
$ ^C
```

<br/>

```
// OK! Данные добавляются
SQL> SELECT * FROM "public"."customers"
```

<br/>

```
// Создаем топик json-customers
$ docker-compose exec broker kafka-topics --create --bootstrap-server localhost:9092 --partitions 2 --replication-factor 1 --topic json-customers
```

<br/>

```
// register the connectors
$ curl -X POST -H "Content-Type: application/json" --data @connectors/connect_jdbc_pg_json.config localhost:8083/connectors | jq


// Пропустим пока AWS
// $ curl -X POST -H "Content-Type: application/json" --data @connectors/connect_s3_sink.config localhost:8083/connectors
```

<br/>

```json
{
  "name": "pg-connector-json",
  "config": {
    "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable": "true",
    "tasks.max": "1",
    "connection.url": "jdbc:postgresql://postgres:5432/postgres",
    "connection.user": "postgres",
    "connection.password": "postgres",
    "mode": "timestamp",
    "timestamp.column.name": "dt_update",
    "table.whitelist": "public.customers",
    "topic.prefix": "json-",
    "validate.non.null": "false",
    "poll.interval.ms": "500",
    "name": "pg-connector-json"
  },
  "tasks": [],
  "type": "source"
}
```

<br/>

```
$ curl -s localhost:8083/connectors | jq
```

<br/>

```
[
  "pg-connector-json"
]
```

<br/>

```
$ docker logs connect
```

<br/>

```
// Прверка
// You should see the messages in JSON format printed on the screen
$ docker exec -it broker bash
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic json-customers --from-beginning
```

<br/>

```
Ничего не появилось!
```

<br/>

**Real-time data processing with Kafka and Spark**

<br/>

```
$ spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 processing/consume_from_kafka.py
```

<br/>

```
// Open another terminal and run more simulations by running the following command
$ python simulations/make_fake_data.py
```

<br/>

```
Ничего не отработало!
```

<br/>

```
$ docker-compose down
```
