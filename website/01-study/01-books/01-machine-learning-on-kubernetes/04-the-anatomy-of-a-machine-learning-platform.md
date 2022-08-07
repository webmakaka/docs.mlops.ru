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
$ kubectl get packagemanifests -o wide -n olm | grep -I opendatahub
opendatahub-operator                        Community Operators Red Hat   52s
```

<br/>

```
$ kubectl get pods -n operators
NAME                                   READY   STATUS    RESTARTS   AGE
opendatahub-operator-b5f4c5757-d9td2   1/1     Running   0          15s
```

<br/>

### Installing Keycloak on Kubernetes

<br/>

```
$ kubectl create ns keycloak
$ kubectl create -f /Chapter04/postgresdb/* --namespace keycloak
$ kubectl create -f Chapter04/keycloak.yaml --namespace keycloak
```

<br/>

```
// It may take a while to start
$ kubectl get pods -n keycloak
```

<br/>

```
//
$ kubectl logs keycloak-ffb6b445c-dg2bz -n keycloak
```

<br/>

```
$ minikube ip --profile ${PROFILE}
192.168.49.2
```

<br/>

```
Open the chapter4/keycloak-ingress.yaml file and replace the KEYCLOAK_HOST string with the keycloak.<THE_IP_ADDRESS_OF_YOUR_MINIKUBE>.
nip.io string. So, if the IP address of your minikube is 192.168.49.2, then the string value would be keycloak.192.168.49.2.nip.io.
```

<br/>

```
$ vi Chapter04/keycloak-ingress.yaml
```

<br/>

```
$ kubectl create -f Chapter04/keycloak-ingress.yaml --namespace keycloak
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
