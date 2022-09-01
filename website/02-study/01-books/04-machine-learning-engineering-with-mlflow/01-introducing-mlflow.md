---
layout: page
title: Chapter 1. Introducing MLflow]
description: Chapter 1. Introducing MLflow]
keywords: Chapter 1. Introducing MLflow]
permalink: /study/books/machine-learning-engineering-with-mlflow/introducing-mlflow/
---

# Chapter 1. Introducing MLflow]

<br/>

### Getting started with MLflow

<br/>

```
$ chmod +x ./run.sh
$ ./run.sh
```

<br/>

http://localhost:8888

<br/>

### Developing your first end-to-end pipeline in MLflow

<br/>

```
$ cd ~/tmp
$ source stockpred_env/bin/activate
$ pip install mlflow==1.28.*
```

<br/>

```
$ cd ~/tmp/Machine-Learning-Engineering-with-MLflow/Chapter01/stockpred/
```

<br/>

```
$ docker build . -t stockpred
$ mlflow run .
$ mlflow ui
```

<br/>

https://docs.conda.io/en/latest/miniconda.html

<br/>

```
// Устанавливаю Miniconda3
$ chmod +x ./Miniconda3-latest-Linux-x86_64.sh
$ ./Miniconda3-latest-Linux-x86_64.sh
$ conda update -n base -c defaults conda
```

<br/>

```
$ pip install sklearn
```

<br/>

```
$ mlflow models serve -m ./mlruns/0/b181d1d1b6c04496be50891ce01a0d08/artifacts/model_random_forest/
```

<br/>

```
$ curl http://127.0.0.1:5000/invocations -H 'Content-Type:application/json' -d '{"data":[[1,1,1,1,0,1,1,1,0,1,1,1,0,0]]}'
```

<br/>

**response:**

```
[1]
```
