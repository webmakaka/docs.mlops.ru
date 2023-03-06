---
layout: page
title: Установка Kubeflow в Minikube
description: Установка Kubeflow в Minikube
keywords: minikube, kubeflow, setup
permalink: /tools/kubernetes/kubeflow/setup/
---

# Установка Kubeflow в Minikube

<br/>

Делаю:  
06.03.2023

**Не работает!**  
Раньше работало!!!

<br/>

**Основано на реальных записях:**  
https://www.youtube.com/watch?v=Zk9T85JWrVk

<br/>

**Требуется kustomize [Версии 4.5.7](//gitops.ru/tools/containers/kubernetes/tools/kustomize/)**

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
// 4 ядер мало! Notebook с трудом запустился!
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

```
// При необходимости можно будет удалить профиль и все созданное в профиле следующей командой
// $ minikube --profile ${PROFILE} stop && minikube --profile ${PROFILE} delete

// Стартовать остановленный minikube
// $ minikube --profile ${PROFILE} start
```

<br/>

<!--
https://github.com/kubeflow/manifests/blob/v1.0-branch/kfdef/kfctl_k8s_istio.yaml
-->

<br/>

```
$ mkdir -p ~/tmp/kubeflow-manifests

// Если нужно использовать какой-то специфичный бранч
// $ git -C ~/tmp/kubeflow-manifests clone https://github.com/kubeflow/manifests.git --branch v1.5-branch --single-branch

// коммит f7dc14e359fb8ab07b5493cf2d6f1f8583d56f7f
$ git -C ~/tmp/kubeflow-manifests clone https://github.com/kubeflow/manifests.git

$ cd ~/tmp/kubeflow-manifests/manifests
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

<br/>

### Для информации

```
$ kubectl get pods -n kubeflow
NAME                                                   READY   STATUS    RESTARTS   AGE
admission-webhook-deployment-67896ddc56-thspc          1/1     Running   0          18m
cache-server-6bc8754779-tf8d8                          2/2     Running   0          18m
centraldashboard-8d454bdc7-l5v5v                       2/2     Running   0          18m
jupyter-web-app-deployment-97464dc44-wpsh2             2/2     Running   0          18m
katib-controller-5b8489cc88-mwfvj                      1/1     Running   0          18m
katib-db-manager-59c849bd4f-lh28c                      1/1     Running   0          18m
katib-mysql-5bf95ddfcc-56p4k                           1/1     Running   0          18m
katib-ui-86f769c6b-wpf76                               2/2     Running   1          18m
kserve-controller-manager-5ff79ddf9-8q8lv              2/2     Running   1          18m
kserve-models-web-app-65496dbbd5-jw29g                 2/2     Running   0          18m
kubeflow-pipelines-profile-controller-94bf4544-r2f8c   1/1     Running   0          18m
metacontroller-0                                       1/1     Running   0          18m
metadata-envoy-deployment-685dd64f86-fjndz             1/1     Running   0          18m
metadata-grpc-deployment-f8d68f687-tgvzl               2/2     Running   1          18m
metadata-writer-667cc55985-znjk7                       2/2     Running   0          18m
minio-5b65df66c9-gl7bh                                 2/2     Running   0          18m
ml-pipeline-55c75c949b-dsjkt                           2/2     Running   0          18m
ml-pipeline-persistenceagent-6fb49cfd95-kt92s          2/2     Running   0          18m
ml-pipeline-scheduledworkflow-5655bc7b8-spknf          2/2     Running   0          18m
ml-pipeline-ui-7d49f8648f-lskn5                        2/2     Running   0          18m
ml-pipeline-viewer-crd-6b895dbd4f-ff7sj                2/2     Running   1          18m
ml-pipeline-visualizationserver-55b75588bb-nvd2p       2/2     Running   0          18m
mysql-6667c59778-f6c59                                 2/2     Running   0          18m
notebook-controller-deployment-6568d55d99-k9hfw        2/2     Running   2          18m
profiles-deployment-7d86c4f9db-jd4fk                   3/3     Running   1          18m
tensorboard-controller-deployment-7fd976787b-d4jqn     3/3     Running   1          18m
tensorboards-web-app-deployment-998bbdbf7-vsk2p        2/2     Running   0          18m
training-operator-7954979fd4-zlntj                     1/1     Running   0          18m
volumes-web-app-deployment-5cddf6cd78-hf6gq            2/2     Running   0          18m
workflow-controller-6b9b6c5b46-mnb6n                   2/2     Running   1          18m
```
