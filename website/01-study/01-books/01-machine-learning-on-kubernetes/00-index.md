---
layout: page
title: Machine Learning on Kubernetes
description: Machine Learning on Kubernetes
keywords: Machine Learning on Kubernetes
permalink: /study/books/machine-learning-on-kubernetes/
---

# [Book] [Faisal Masood, Ross Brigoli] Machine Learning on Kubernetes [ENG, 2022]

<br/>

## Part 1: The Challenges of Adopting ML and Understanding MLOps (What and Why)

### 01. Challenges in Machine Learning

### 02. Understanding MLOps

### 03. Exploring Kubernetes

<br/>

#### Installing Operator Lifecycle Manager (OLM)

<br/>

```
$ kubectl apply -f https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.19.1/crds.yaml
```

<br/>

```
$ kubectl apply -f https://github.com/operator-framework/operator-lifecycle-manager/releases/download/v0.19.1/olm.yaml
```

<br/>

```
$ kubectl get pods -n olm
```

<br/>

```
NAME                               READY   STATUS    RESTARTS   AGE
catalog-operator-fc7fb45b5-mq9cw   1/1     Running   0          94s
olm-operator-765c45d458-f6rx2      1/1     Running   0          94s
operatorhubio-catalog-phnbt        1/1     Running   0          84s
packageserver-7bf4799ddf-7j99f     1/1     Running   0          84s
packageserver-7bf4799ddf-cfsdx     1/1     Running   0          84s
```

<br/>

```
$ kubectl get catalogsource -n olm
NAME                    DISPLAY               TYPE   PUBLISHER        AGE
operatorhubio-catalog   Community Operators   grpc   OperatorHub.io   91s
```

<br/>

## Part 2: The Building Blocks of an MLOps Platform and How to Build One on Kubernetes

<br/>

### [Chapter 4. The Anatomy of a Machine Learning Platform](/study/books/machine-learning-on-kubernetes/the-anatomy-of-a-machine-learning-platform/)

### Chapter 5. Data Engineering

### Chapter 6. Machine Learning Engineering

### Chapter 7. Model Deployment and Automation

<br/>

```
$ docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:19.0.1 start-dev
```

<br/>

```
// admin / admin
http://localhost:8080/admin
```

<br/>
