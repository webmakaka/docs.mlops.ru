---
layout: page
title: Machine Learning on Kubernetes - Chapter 5. Data Engineering
description: Machine Learning on Kubernetes - Chapter 5. Data Engineering
keywords: Machine Learning on Kubernetes - Chapter 5. Data Engineering
permalink: /study/books/machine-learning-on-kubernetes/data-engineering/
---

# Chapter 5. Data Engineering

<br/>

### Importing the Keycloak configuration for the ODH components

keycloak -> import -> Chapter05/realm-export.json -> If a resource exists - Skip -> Import

<br/>

### Creating a Keycloak user

Users -> Add user ->

Username: mluser
Email: mluser@example.com
First Name: mluser
Last Name: mluser

User Enabled: ON
Email Verified: ON

Groups: ml-group

SAVE

<br/>

Credentials:

Password: mluser
Password Confirmation: mluser

Temporary: OFF

Set Password

<br/>

### Installing ODH

```
$ kubectl create ns ml-workshop
```

<br/>

```
$ minikube ip --profile ${PROFILE}
```

<br/>

```
$ export MINIKUBE_IP_ADDR=192.168.49.2
```

<br/>

```
// Check
// $ envsubst < manifests/kfdef/ml-platform.yaml
```

<br/>

```
$ envsubst < manifests/kfdef/ml-platform.yaml | kubectl create -f - --namespace ml-workshop
```

<br/>

```
$ watch kubectl get pods --namespace ml-workshop
```

<!--

<br/>

Убрал prometheus и grafana. Т.к. ресурсов не хватает.




- Statefulsets
* Daemonsets

-->

<br/>

```
NAME                                           READY   STATUS      RESTARTS        AGE
app-aflow-airflow-scheduler-6f9c44866d-ppzcj   2/2     Running     0               14m
app-aflow-airflow-web-6d9587698-w2786          2/2     Running     0               4m56s
app-aflow-airflow-worker-0                     2/2     Running     3 (3m47s ago)   14m
app-aflow-postgresql-0                         1/1     Running     0               14m
app-aflow-redis-master-0                       1/1     Running     0               14m
flightsdatadb-0                                1/1     Running     0               10m
jupyterhub-6cff7d6cc5-t5cjw                    1/1     Running     0               14m
jupyterhub-db-0                                1/1     Running     0               14m
minio-ml-workshop-6fknp                        0/1     Completed   2               14m
minio-ml-workshop-7fcc5dfd8-lq8br              1/1     Running     0               14m
mlflow-5fb4cb5d5d-66qmm                        2/2     Running     0               14m
mlflow-db-0                                    1/1     Running     1 (11m ago)     14m
prometheus-odh-monitoring-0                    2/2     Running     0               6m
seldon-controller-manager-c5f59c56d-wh652      1/1     Running     0               14m
spark-operator-6bc4f8f5f8-xblrp                1/1     Running     0               14m
```

<br/>

```
$ kubectl get all --namespace ml-workshop
```

<br/>

### Validating the JupyterHub installation

<br/>

```
$ kubectl get ingress --namespace ml-workshop
NAME                   CLASS   HOSTS                            ADDRESS        PORTS     AGE
ap-airflow2            nginx   airflow.192.168.49.2.nip.io      192.168.49.2   80, 443   3m36s
grafana                nginx   grafana.192.168.49.2.nip.io      192.168.49.2   80, 443   3m36s
jupyterhub             nginx   jupyterhub.192.168.49.2.nip.io   192.168.49.2   80, 443   3m39s
minio-ml-workshop-ui   nginx   minio.192.168.49.2.nip.io        192.168.49.2   80, 443   3m36s
mlflow                 nginx   mlflow.192.168.49.2.nip.io       192.168.49.2   80, 443   3m36s
```

<br/>

```
// mluser / mluser
https://jupyterhub.192.168.49.2.nip.io
```

Select Base Elyra Notebook Image and the Default container size and hit Start server.

<br/>

```
// Посмотреть, что запустился еще 1 контейнер
$ kubectl get pods -n ml-workshop | grep mluser
```

<br/>

### Creating a Spark cluster

<br/>

```
$ kubectl get pods -n ml-workshop | grep spark-operator
spark-operator-6bc4f8f5f8-6x5t6                1/1     Running     0             80m
```

<br/>

```
$ kubectl create -f Chapter05/simple-spark-cluster.yaml --namespace ml-workshop
```

<br/>

```
$ kubectl get pods --namespace ml-workshop | grep simple-spark
```

<br/>

Select the Elyra Notebook Image with Spark image and the Small container size.

<br/>

```
https://spark-cluster-mluser.192.168.49.2.nip.io
```
