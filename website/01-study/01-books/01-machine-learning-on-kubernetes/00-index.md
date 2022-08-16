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

### Technical requirements

<br/>

• A central processing unit (CPU) with at least four cores; eight are recommended
• Memory of at least 16 gigabytes (GB); 32 GB is recommended
• Disk with available space of at least 60 GB

<br/>

### Поднимаем

```
$ export \
    PROFILE=marley-minikube \
    CPUS=8 \
    MEMORY=30G \
    HDD=80G \
    DRIVER=docker \
    KUBERNETES_VERSION=v1.24.3
```

<br/>

```
$ {
    minikube --profile ${PROFILE} config set memory ${MEMORY}
    minikube --profile ${PROFILE} config set cpus ${CPUS}
    minikube --profile ${PROFILE} config set disk-size ${HDD}

    minikube --profile ${PROFILE} config set driver ${DRIVER}

    minikube --profile ${PROFILE} config set kubernetes-version ${KUBERNETES_VERSION}
    minikube start --profile ${PROFILE} --embed-certs

    // Enable ingress
    minikube addons --profile ${PROFILE} enable ingress

    // Enable registry
    // minikube addons --profile ${PROFILE} enable registry
}
```

<br/>

    // При необходимости можно будет удалить профиль и все созданное в профиле следующей командой
    // $ minikube --profile ${PROFILE} stop && minikube --profile ${PROFILE} delete

    // Стартовать остановленный minikube
    // $ minikube --profile ${PROFILE} start

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
$ watch kubectl get pods -n olm
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

### [Chapter 5. Data Engineering](/study/books/machine-learning-on-kubernetes/data-engineering/)

### [Chapter 6. Machine Learning Engineering](/study/books/machine-learning-on-kubernetes/machine-learning-engineering/)

### [Chapter 7. Model Deployment and Automation](/study/books/machine-learning-on-kubernetes/model-deployment-and-automation/)

<br/>

## Part 3: How to Use the MLOps Platform and Build a Full End-to-End Project Using the New Platform

<br/>

• Chapter 8, Building a Complete ML Project Using the Platform
• Chapter 9, Building Your Data Pipeline
• Chapter 10, Building, Deploying, and Monitoring Your Model
• Chapter 11, Machine Learning on Kubernetes

<!--

TMP

```
$ kubectl delete svc keycloak -n keycloak

$ kubectl expose deployment keycloak --type=NodePort --port=8080 -n keycloak

$ sudo vi /etc/nginx/nginx.conf

 server {
      listen 192.168.1.101:60000;
      proxy_pass 192.168.49.2:30830;
  }




$ sudo systemctl restart nginx

$ curl 192.168.1.101:60000
```


-->
