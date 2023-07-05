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
05.07.2023

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
    MEMORY=12G \
    HDD=20G \
    DRIVER=docker \
    KUBERNETES_VERSION=v1.27.3
```

<br/>

[Как запускать](//gitops.ru/tools/containers/kubernetes/minikube/setup/)

<br/>

**По инструкции:**  
https://www.kubeflow.org/docs/components/pipelines/v1/installation/localcluster-deployment/#deploying-kubeflow-pipelines

**Для версии v2:**  
https://www.kubeflow.org/docs/components/pipelines/v2/installation/quickstart/

<br/>

```
$ export PIPELINE_VERSION=2.0.0

$ kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"

$ kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io

$ kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
```

<br/>

```
$ k9s -n kubeflow
```

<br/>

```
kubectl get pods -n kubeflow
NAME                                              READY   STATUS    RESTARTS        AGE
cache-deployer-deployment-64dc947fc7-7w6fs        1/1     Running   0               11m
cache-server-7f7d6bfb55-fbb85                     1/1     Running   0               11m
metadata-envoy-deployment-6dcd4ddcb8-bpq2l        1/1     Running   0               11m
metadata-grpc-deployment-5644fb9768-zwwdc         1/1     Running   4 (119s ago)    11m
metadata-writer-9c4488669-62h2q                   1/1     Running   1 (105s ago)    11m
minio-55464b6ddb-8m2dl                            1/1     Running   0               11m
ml-pipeline-5b8b594744-sj9xj                      1/1     Running   1 (3m12s ago)   11m
ml-pipeline-persistenceagent-545d5c6786-w8s4v     1/1     Running   1 (2m19s ago)   11m
ml-pipeline-scheduledworkflow-8f9b7654d-hv4sk     1/1     Running   0               11m
ml-pipeline-ui-7c4cf85598-b29kr                   1/1     Running   0               11m
ml-pipeline-viewer-crd-589c6c6569-qn9br           1/1     Running   0               11m
ml-pipeline-visualizationserver-9fcfbd447-qwmv5   1/1     Running   0               11m
mysql-7d8b8ff4f4-bm7gl                            1/1     Running   0               11m
workflow-controller-589ff7c479-tfsg5              1/1     Running   0               11m
```

<br/>

```
$ kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```

<br/>

```
http://localhost:8080
```

<!--

<br/>

```
$ mkdir -p ~/tmp/kubeflow-manifests
$ cd ~/tmp/kubeflow-manifests

// Если нужно использовать какой-то специфичный бранч
// $ git -C ~/tmp/kubeflow-manifests clone https://github.com/kubeflow/manifests.git --branch v1.5-branch --single-branch


$ git -C ~/tmp/kubeflow-manifests clone https://github.com/kubeflow/manifests.git

$ git reset --hard f7dc14e359fb8ab07b5493cf2d6f1f8583d56f7f

$ cd ~/tmp/kubeflow-manifests/manifests
```


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

-->
