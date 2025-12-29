---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
keywords: courses, devops to mlops bootcamp
permalink: /courses/mlops/ultimate-devops-to-mlops-bootcamp/building-scalable-prod-inference-infrastructure-with-kubernetes/
---

# [Course][Udemy][Gourav Shah] Ultimate DevOps to MLOps Bootcamp - Build ML CI-CD Pipelines [ENG, 2025] : 08. Building Scalable Prod Inference Infrastructure with Kubernetes

<br/>

**Делаю:**  
2025.12.29

<br/>

### 04. Simplest way to build a 3 Node Kubernetes Cluster with KIND

<br/>

Инсталляция и создание kubernetes кластера [kind](//docs.k8s.ru/tools/containers/kubernetes/kind/)

<br/>

### 06. Deploying Streamlit Frontent App with Kubernetes

```
$ kubectl create deployment streamlit --image=webmakaka/streamlit:latest --port=8501
```

### 07. Exposing the Streamlit App with Kubernetes NodePort Service

<br/>

```
$ kubectl create service nodeport streamlit --tcp=8501 --node-port=30000
```

<br/>

### 08. Creating Deployment Service for the Model wrapped in FastAPI

```
$ kubectl create deployment model --image=webmakaka/house-price-model:latest --port=8000
```

<br/>

```
$ kubectl create service nodeport model --tcp=8000 --node-port=30100
```

<br/>

```
$ kubectl get pods
NAME                        READY   STATUS    RESTARTS   AGE
model-54fb689844-fvj4z      1/1     Running   0          88s
streamlit-94fb5b648-pt57q   1/1     Running   0          103s
```

<br/>

```
// OK!
http://localhost:30100/docs
http://localhost:30000
```
