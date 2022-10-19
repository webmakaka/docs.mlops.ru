---
layout: page
title: Chapter 8. Training Models with MLflow
description: Chapter 8. Training Models with MLflow
keywords: Chapter 8. Training Models with MLflow
permalink: /study/books/machine-learning-engineering-with-mlflow/training-models-with-mlflow/
---

# Chapter 8. Training Models with MLflow

<br/>

```
$ pip install mlflow
$ cd ~/tmp/Machine-Learning-Engineering-with-MLflow/Chapter09/gradflow/
$ export MLFLOW_TRACKING_URI=http://localhost:5000
$ mlflow db upgrade sqlite:///mlflow_db
$ make gradflow-light
```

<br/>

```
$ cd ~/tmp/Machine-Learning-Engineering-with-MLflow/Chapter08/psystock-training
```

<br/>

```
$ conda env create -f conda.yaml
$ conda activate pystock-data-features
```

<br/>

```
$ export MLFLOW_TRACKING_URI=http://localhost:5000
```

<br/>

```
$ mlflow run .
$ mlflow ui
```

<br/>

### Creating a Docker image for your training job

<br/>

```
$ cd ~/tmp/Machine-Learning-Engineering-with-MLflow/Chapter08/psystock-training-docker
```

<br/>

```
$ docker build -t psystock_docker_training_image .
```

<br/>

```
// $ export TRACKING_SERVER_URI=http://host.docker.internal:5000
$ export TRACKING_SERVER_URI=localhost:5000


// Ошибка
$ docker run -p 5000:5000 -e MLflow_TRACKING_SERVER=$TRACKING_SERVER_URI psystock_docker_training_image
```
