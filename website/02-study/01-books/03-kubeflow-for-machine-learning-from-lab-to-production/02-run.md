---
layout: page
title: Kubeflow for Machine Learning From Lab to Production
description: Kubeflow for Machine Learning From Lab to Production
keywords: Kubeflow for Machine Learning From Lab to Production
permalink: /study/books/kubeflow-for-machine-learning-from-lab-to-production/run/
---

# Kubeflow for Machine Learning From Lab to Production

<br/>

Делаю:  
24.08.2022

<br/>

### Setting Up Your Kubeflow Development Environment

<br/>

```
$ cd ~
$ virtualenv kfvenv --python python3
$ source kfvenv/bin/activate
```

<!--

<br/>

```
$ cd ~/tmp/intro-to-ml-with-kubeflow-examples/
```

<br/>

```
// $ chmod +x ./dev-setup/install-kf-pipeline-sdk.sh
// $ ./dev-setup/install-kf-pipeline-sdk.sh
```

-->

<br/>

```
$ pip install https://storage.googleapis.com/ml-pipeline/release/latest/kfp.tar.gz --upgrade
```

<br/>

```
$ mkdir -p ~/repos
$ git -C ~/repos clone --single-branch --branch google-cloud-pipeline-components-0.3.0 https://github.com/kubeflow/pipelines.git
```

<br/>

```
// ???
$ git clone https://github.com/kubeflow/example-seldon
```

<br/>

### Training and Monitoring Progress

<br/>

```
$ cd ~/tmp/Kubeflow-for-Machine-Learning-From-Lab-to-Production/ch02_seldon_examples/
$ dsl-compile --py TrainPipeline.py --output TrainPipeline.yaml
```

<br/>

localhost:7777

<br/>

Pipelines -> Upload -> TrainPipeline.yaml

Run

```
// Не знаю как победить
This step is in Failed state with this message: error: error when creating "/tmp/manifest.yaml": Post https://10.96.0.1:443/apis/machinelearning.seldon.io/v1alpha2/namespaces/kubeflow/seldondeployments: stream error: stream ID 123; INTERNAL_ERROR
```

<br/>

### Test Query

???

<br/>

https://github.com/intro-to-ml-with-kubeflow/intro-to-ml-with-kubeflow-examples/blob/master/ch2/query-endpoint.py
