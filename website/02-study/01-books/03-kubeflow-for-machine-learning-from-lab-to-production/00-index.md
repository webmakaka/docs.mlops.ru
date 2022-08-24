---
layout: page
title: Kubeflow for Machine Learning From Lab to Production
description: Kubeflow for Machine Learning From Lab to Production
keywords: Kubeflow for Machine Learning From Lab to Production
permalink: /study/books/kubeflow-for-machine-learning-from-lab-to-production/
---

# Kubeflow for Machine Learning From Lab to Production

<br/>

Делаю:  
24.08.2022

<br/>

**GitHub:**  
https://github.com/intro-to-ml-with-kubeflow/intro-to-ml-with-kubeflow-examples

<br/>

### [Инсталляция KFCTL](/tools/kubernetes/tools/kubeflow/)

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

### Setting Up Your Kubeflow Development Environment

<br/>

```
$ cd ~/tmp/
$ git clone https://github.com/intro-to-ml-with-kubeflow/intro-to-ml-with-kubeflow-examples.git
$ cd intro-to-ml-with-kubeflow-examples/
```

<br/>

```
// $ chmod +x ./dev-setup/install-kf-pipeline-sdk.sh
// $ ./dev-setup/install-kf-pipeline-sdk.sh
```

<br/>

```
$ cd ~
$ virtualenv kfvenv --python python3
$ source kfvenv/bin/activate
```

<br/>

```
$ URL=https://storage.googleapis.com/ml-pipeline/release/latest/kfp.tar.gz
$ pip install "${URL}" --upgrade
```

<br/>

```
$ mkdir -p ~/repos
$ git -C ~/repos clone --single-branch --branch google-cloud-pipeline-components-0.3.0 https://github.com/kubeflow/pipelines.git
```

<br/>

### Creating Our First Kubeflow Project

<br/>

```
// $ ./ch2_seldon_examples/setup_example.sh
```

<br/>

```
$ {
  export KUBEFLOW_PROJECT_NAME=marley-kubeflow \
  export KUBEFLOW_HOME=~/kubeflow/${KUBEFLOW_PROJECT_NAME}
}
```

<br/>

```
$ mkdir -p ${KUBEFLOW_HOME}
$ cd ${KUBEFLOW_HOME}
```

<br/>

```
// This deployment process can take up to 30 minutes.
$ kfctl apply -V -f https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.1.yaml
```

<br/>

```
$ git clone https://github.com/kubeflow/example-seldon
```

<br/>

### Training and Monitoring Progress

<br/>

```
$ cd ~/tmp/intro-to-ml-with-kubeflow-examples/ch2_seldon_examples/
```

<br/>

```
$ kubectl apply -f ./pipeline_role.yaml
$ kubectl apply -f ./pipeline_rolebinding.yaml
```

<br/>

```
$ dsl-compile --py train_pipeline.py --output job.yaml
```

<br/>

```
$ kubectl port-forward svc/istio-ingressgateway -n istio-system 7777:80
```

<br/>

localhost:7777

<br/>

Pipelines -> Upload -> job.yaml

Run

```
// Не знаю как победить
This step is in Failed state with this message: error: error when creating "/tmp/manifest.yaml": Post https://10.96.0.1:443/apis/machinelearning.seldon.io/v1alpha2/namespaces/kubeflow/seldondeployments: stream error: stream ID 123; INTERNAL_ERROR
```

<br/>

### Test Query

https://github.com/intro-to-ml-with-kubeflow/intro-to-ml-with-kubeflow-examples/blob/master/ch2/query-endpoint.py
