---
layout: page
title: Chapter 9. Deployment and Inference with MLflow
description: Chapter 9. Deployment and Inference with MLflow
keywords: Chapter 9. Deployment and Inference with MLflow
permalink: /books/machine-learning-engineering-with-mlflow/deployment-and-inference-with-mlflow/
---

# Chapter 9. Deployment and Inference with MLflow

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
$ cd ~/tmp/Machine-Learning-Engineering-with-MLflow/Chapter09/psystock-inference-batch/

Нужно заменить localhost на ip host

$ docker build . -t pystock-inference-batch
$ docker run -i pystock-inference-batch
```

<br/>

```
$ cd ~/tmp/Machine-Learning-Engineering-with-MLflow/Chapter09/psystock-inference-api/
$ docker build . -t pystock-inference-api
$ docker run -i pystock-inference-api -p 6000:6000
```
