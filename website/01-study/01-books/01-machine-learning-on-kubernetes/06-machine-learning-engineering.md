---
layout: page
title: Machine Learning on Kubernetes - Chapter 6. Machine Learning Engineering
description: Machine Learning on Kubernetes - Chapter 6. Machine Learning Engineering
keywords: Machine Learning on Kubernetes - Chapter 6. Machine Learning Engineering
permalink: /study/books/machine-learning-on-kubernetes/machine-learning-engineering/
---

# Chapter 6. Machine Learning Engineering

<br/>

```
// minio / minio123
https://minio.192.168.49.2.nip.io
```

<br/>

```
// mluser / mluser
https://mlflow.192.168.49.2.nip.io
```

<br/>

```
// ??? mluser / mluser
https://jupyterhub.192.168.49.2.nip.io/hub/spawn
```

<br/>

```
Scikit v1.10 - Elyra Notebook Image.

Container size: Small

Environment variables

Custom variable


Variable name: AWS_SECRET_ACCESS_KEY
Variable value: minio123

Start server
```

<br/>

Chapter06/hellomlflow.ipynb

<br/>

### Демонстрация создания своего image

```
$ docker build -t scikit-notebook:v1.1.0 -f chapter6/CustomNotebookDockerfile ./chapter6/.
```

<br/>

```
$ docker tag scikit-notebook:v1.1.0 quay.io/ml-on-k8s/scikit-notebook:v1.1.0
```

<br/>

```
$ docker push quay.io/ml-on-k8s/scikit-notebook:v1.1.0
```

<br/>

```
$ vi manifests/jupyterhub-images/base/customnotebook-imagestream.yaml
```

<br/>

### MLFLOW

<br/>

```
$ kubectl get ingress -n ml-workshop
```

<br/>

// minio / minio123
https://minio.192.168.49.2.nip.io

mluser / mluser
https://mlflow.192.168.49.2.nip.io

<br/>

JupyterHub SciKit v.10 Elyra

Scikit v1.10 - Elyra Notebook Image.

chapter6/hellomlflow.ipynb

run all

mluser / mluser
https://mlflow.192.168.49.2.nip.io

HelloMLFlow

chapter6/hellomlflow-custom.ipynb
