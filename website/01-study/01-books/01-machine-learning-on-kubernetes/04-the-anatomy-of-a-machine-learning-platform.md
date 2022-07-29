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
$ git clone git@github.com:PacktPublishing/Machine-Learning-on-Kubernetes.git
$ cd Machine-Learning-on-Kubernetes/
```

<br/>

```
$ kubectl create -f Chapter04/catalog-source.yaml
$ kubectl create -f Chapter04/odh-subscription.yaml
```

<br/>

```
$ kubectl get packagemanifests -o wide -n olm | grep -I opendatahub
opendatahub-operator                        Community Operators Red Hat   34m
```

<br/>

```
$ kubectl get pods -n operators
NAME                                    READY   STATUS    RESTARTS   AGE
opendatahub-operator-6496657bf6-hllqr   1/1     Running   0          25s
```

<br/>

### Installing Keycloak on Kubernetes

<br/>

```
$ kubectl create ns keycloak
$ kubectl create -f Chapter04/keycloak.yaml --namespace keycloak
```

<br/>

```
// It may take a while to start
$ kubectl get pods -n keycloak
```

<br/>

```
$ minikube ip
```

<br/>

```
Open the chapter4/keycloak-ingress.yaml file and replace the KEYCLOAK_HOST string with the keycloak.<THE_IP_ADDRESS_OF_YOUR_MINIKUBE>.
nip.io string. So, if the IP address of your minikube is 192.168.61.72 , then
the string value would be keycloak.192.168.61.72.nip.io.
```

<br/>

```
$ kubectl create -f chapter4/keycloak-ingress.yaml --namespace keycloak
```

<br/>

```
$ kubectl get ingress --namespace keycloak
```

<br/>

https://keycloak.192.168.61.72.nip.io/auth/

<br/>

Administration Console

admin/admin
