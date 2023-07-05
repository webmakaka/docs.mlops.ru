---
layout: page
title: Chapter 7. Data and Feature Management
description: Chapter 7. Data and Feature Management
keywords: Chapter 7. Data and Feature Management
permalink: /books/machine-learning-engineering-with-mlflow/data-and-feature-management/
---

# Chapter 7. Data and Feature Management

<br/>

### Running your end-to-end pipeline

<br/>

```
$ cd ~/tmp/Machine-Learning-Engineering-with-MLflow/Chapter07/psystock-data-features-main/
```

<br/>

```
$ conda env create -f conda.yaml
$ conda activate pystock-data-features
$ mlflow run . --experiment-name=psystock_data_pipelines
$ mlflow ui
```

<br/>

```
http://localhost:5000
```

```
// Пришлось сделать
$ pip uninstall mlflow
$ pip install mlflow
```

<br/>

### [???] Using a feature store

<br/>

**Issues:**

https://github.com/PacktPublishing/Machine-Learning-Engineering-with-MLflow/issues/8

<br/>

```
$ cd ~/tmp/Machine-Learning-Engineering-with-MLflow/Chapter07/psystock_feature_store

$ pip install feast==0.10 protobuf==3.20.*
$ protobuf package to 3.20.x
$ feast init

????

$ feast apply
```
