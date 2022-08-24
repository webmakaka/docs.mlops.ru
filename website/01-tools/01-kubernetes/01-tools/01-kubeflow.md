---
layout: page
title: Kubeflow
description: Kubeflow
keywords: Kubeflow
permalink: /tools/kubernetes/tools/kubeflow/
---

# Kubeflow

<br/>

Делаю:  
24.08.2022

<br/>

**Основано на реальных записях:**  
https://www.youtube.com/watch?v=Zk9T85JWrVk

<br/>

### Инсталляция KFCTL

```
// v1.2.0
$ LATEST_KFCTL_VERSION=$(curl -s https://api.github.com/repos/kubeflow/kfctl/releases/latest | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')

// v1.2.0
$ echo ${LATEST_KFCTL_VERSION}

$ wget  -qO- https://github.com/kubeflow/kfctl/releases/download/${LATEST_KFCTL_VERSION}/kfctl_v1.2.0-0-gbc038f9_linux.tar.gz | tar zxvf -  -C /tmp/
$ sudo mv /tmp/kfctl /usr/local/bin
```

<br/>

```
$ kfctl version
kfctl v1.2.0-0-gbc038f9
```

<br/>

### Запуск minikube

<br/>

// Нужна какая-то старая версия kubernetes.
// Потом нужно будет проапгрейдить!

<br/>

```
$ export \
    PROFILE=marley-minikube \
    CPUS=8 \
    MEMORY=30G \
    HDD=80G \
    DRIVER=docker \
    KUBERNETES_VERSION=v1.16.0
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

<!--
https://github.com/kubeflow/manifests/blob/v1.0-branch/kfdef/kfctl_k8s_istio.yaml
-->

<br/>

###

```
$ export \
    KF_NAME="marley-kubeflow" \
    BASE_DIR=~/kubeflow \
    KF_DIR=${BASE_DIR}/${KF_NAME} \
    CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.1.yaml \
    CONFIG_URI=https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.1.yaml
```

<br/>

```
$ mkdir -p ${KF_DIR}
$ cd ${KF_DIR}
$ kfctl build -V -f ${CONFIG_URI}
$ kfctl apply -V -f ${CONFIG_FILE}
```

<br/>

```
$ kubectl -n kubeflow get pods
$ kubectl -n kubeflow get svc
```

<br/>

```
$ kubectl -n kubeflow port-forward -n istio-system svc/istio-ingressgateway 8080:80
```

<br/>

http://localhost:8080/

<br/>

Namespace: holee
