---
layout: page
title: Machine Learning on Kubernetes - Chapter 9. Building Your Data Pipeline
description: Machine Learning on Kubernetes - Chapter 9. Building Your Data Pipeline
keywords: Machine Learning on Kubernetes - Chapter 9. Building Your Data Pipeline
permalink: /study/books/machine-learning-on-kubernetes/building-your-data-pipeline/
---

# Chapter 9. Building Your Data Pipeline

<br/>

Пересоздал environment c 0.

<br/>

### Подготавливаем данные в базе

```
$ kubectl create -f Chapter09/deployment-pg-flights-data.yaml -n ml-workshop
```

<br/>

```
$ kubectl create -f Chapter09/service-pg-flights-data.yaml -n ml-workshop
```

<br/>

```
$ POD_NAME=$(kubectl get pods -n ml-workshop -l app=pg-flights-data -o jsonpath="{.items[0].metadata.name}")
```

<br/>

```
$ echo ${POD_NAME}
```

<br/>

```
$ kubectl exec -it $POD_NAME -n ml-workshop -- bash
```

<br/>

```
# psql -U postgres
```

<br/>

```
postgres=# select count(1) from flights;
```

<br/>

```
  count
---------
 5819079
(1 row)
```

<br/>

### Подготавливаем данные в minio

<br/>

```
// minio / minio123
https://minio.192.168.49.2.nip.io
```

<br/>

```
Buckets -> Create Bucket

Name: airport-data

Create Bucket
```

<br/>

Загрузить 2 файла из Chapter09/data/

<br/>

- airlines.csv
- airports.csv

<br/>

### Пробуем загрузить данные в jupyterhub

<br/>

```
// mluser / mluser
https://jupyterhub.192.168.49.2.nip.io/hub/spawn
```

<br/>

```
Elyra Notebook Image with Spark

// Large не стартовал
Container size: Medium

Start server
```

<br/>

Clone: https://github.com/webmakaka/Machine-Learning-on-Kubernetes.git

<br/>

Chapter09/explore_data.ipynb

<br/>

Последний блок завершился ошибкой. М.б. из-за того, что не Large

<br/>

### Designing and building the pipeline

<!--
Replicationcontrollers
-->
