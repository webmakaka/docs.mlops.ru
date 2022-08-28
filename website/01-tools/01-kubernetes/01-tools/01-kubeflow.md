---
layout: page
title: Kubeflow
description: Kubeflow
keywords: Kubeflow
permalink: /tools/kubernetes/tools/kubeflow/
---

# Kubeflow

https://github.com/kubeflow/kfctl

https://github.com/kubeflow/manifests

https://github.com/kubeflow/pipelines

https://github.com/kubeflow/example-seldon

<br/>

Делаю:  
28.08.2022

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

```
$ export \
    PROFILE=marley-minikube \
    CPUS=4 \
    MEMORY=15G \
    HDD=20G \
    DRIVER=docker \
    KUBERNETES_VERSION=v1.21.0
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

```
$ mkdir -p ~/tmp/kubeflow-manifests
$ git -C ~/tmp/kubeflow-manifests clone https://github.com/kubeflow/manifests.git --branch v1.5-branch --single-branch

$ cd /home/marley/tmp/kubeflow-manifests/manifests
```

<!--

```
$ git checkout v1.5.1 -b release-1.5.1
```

-->

<br/>

```
$ while ! kustomize build example | kubectl apply -f -; do echo "Retrying to apply resources"; sleep 10; done
```

<br/>

```
$ kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
```

<br/>

```
// user@example.com / 12341234
http://localhost:8080
```
