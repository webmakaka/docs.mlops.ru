---
layout: page
title: Machine Learning on Kubernetes - Chapter 4. The Anatomy of a Machine Learning Platform
description: Machine Learning on Kubernetes - Chapter 4. The Anatomy of a Machine Learning Platform
keywords: Machine Learning on Kubernetes - Chapter 4. The Anatomy of a Machine Learning Platform
permalink: /study/books/machine-learning-on-kubernetes/the-anatomy-of-a-machine-learning-platform/
---

# Chapter 4. The Anatomy of a Machine Learning Platform

<br/>

### Installing the Open Data Hub (ODH) operator on Kubernetes

<br/>

```
$ cd ~/tmp/
$ git clone git@github.com:webmakaka/Machine-Learning-on-Kubernetes.git
$ cd Machine-Learning-on-Kubernetes/
```

<br/>

```
$ kubectl create -f Chapter04/catalog-source.yaml
$ kubectl create -f Chapter04/odh-subscription.yaml
```

<br/>

```
// Нужно ждать пару минут
$ watch kubectl get pods --namespace operators
NAME                                   READY   STATUS    RESTARTS   AGE
opendatahub-operator-b5f4c5757-d9td2   1/1     Running   0          15s
```

<br/>

```
$ kubectl get packagemanifests -o wide --namespace olm | grep -I opendatahub
opendatahub-operator                        Community Operators Red Hat   52s
```

<br/>

### Installing Keycloak on Kubernetes

<br/>

```
$ kubectl create ns keycloak
$ kubectl create -f ./Chapter04/postgresdb/ --namespace keycloak
$ kubectl create -f Chapter04/keycloak.yaml --namespace keycloak
```

<br/>

```
$ watch kubectl get pods --namespace keycloak
```

<br/>

```
$ minikube ip --profile ${PROFILE}
192.168.49.2
```

<br/>

```
$ export MINIKUBE_IP_ADDR=192.168.49.2
```

<br/>

```
// Check
// $ envsubst < Chapter04/keycloak-ingress.yaml
```

<br/>

```
$ envsubst < Chapter04/keycloak-ingress.yaml | kubectl create -f - --namespace keycloak
```

<br/>

```
$ kubectl get ingress --namespace keycloak
NAME       CLASS   HOSTS                          ADDRESS        PORTS     AGE
keycloak   nginx   keycloak.192.168.49.2.nip.io   192.168.49.2   80, 443   4m8s
```

<br/>

https://keycloak.192.168.49.2.nip.io/auth/

<br/>

Administration Console

admin/admin
