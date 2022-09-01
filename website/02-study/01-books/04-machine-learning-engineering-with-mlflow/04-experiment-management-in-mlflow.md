---
layout: page
title: Chapter 4. Experiment Management in MLflow
description: Chapter 4. Experiment Management in MLflow
keywords: Chapter 4. Experiment Management in MLflow
permalink: /study/books/machine-learning-engineering-with-mlflow/experiment-management-in-mlflow/
---

# Chapter 4. Experiment Management in MLflow

<br/>

```
$ cd ~/tmp
$ source stockpred_env/bin/activate
```

<br/>

```
$ cd ~/tmp/Machine-Learning-Engineering-with-MLflow/Chapter04/gradflow/
$ make
```

<br/>

```
$ docker ps
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS          PORTS                                       NAMES
3d65aa200d03   gradflow/workbench/jupyter:0.1.0    "tini -g -- start-no…"   19 seconds ago   Up 17 seconds   0.0.0.0:8888->8888/tcp, :::8888->8888/tcp   gradflow-jupyter-1
0ba4627c9518   gradflow/workbench/mlflow:0.1.0     "/bin/sh -c './wait-…"   19 seconds ago   Up 18 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   gradflow-mlflow-1
fed2e90e166f   gradflow/workbench/postgres:0.1.0   "docker-entrypoint.s…"   20 seconds ago   Up 18 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   gradflow-postgres-1
```

<br/>

```
http://localhost:5000
```

<br/>

```
http://localhost:8888
```

Chapter04/gradflow/notebooks/retrieve_training_data.ipynb

<br/>

### Будем запускать эксперименты

• Logistic Classifier (Chapter04/gradflow/notebooks/mlflow_run_logistic_regression.ipynb)
• Xgboost (Chapter04/gradflow/notebooks/mlflow_run_xgboost.ipynb)
• Keras (Chapter04/gradflow/notebooks/mlflow_run_keras.ipynb)

<br/>

Chapter04/gradflow/notebooks/hyperopt_optimization_logistic_regression_mlflow.ipynb
