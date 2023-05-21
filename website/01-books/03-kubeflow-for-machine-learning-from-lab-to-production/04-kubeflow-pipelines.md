---
layout: page
title: Kubeflow for Machine Learning From Lab to Production - Kubeflow Pipelines
description: Kubeflow for Machine Learning From Lab to Production - Kubeflow Pipelines
keywords: Kubeflow for Machine Learning From Lab to Production - Kubeflow Pipelines
permalink: /books/kubeflow-for-machine-learning-from-lab-to-production/kubeflow-pipelines/
---

# Chapter 04. Kubeflow Pipelines

<br/>

```
$ cd ~
$ source kfvenv/bin/activate
```

<br/>

У нас 3 pipeline, которые нужно запустить:

<br/>

1. LightweightPipeline.py
2. RecommenderPipeline.py
3. ConditionalPipeline.py

<br/>

```
$ cd ~/tmp/Kubeflow-for-Machine-Learning-From-Lab-to-Production/ch04/
```

<br/>

```
$ vi RecommenderPipeline.py
```

<br/>

```
// Наверное
# exp = client.create_experiment(name='mdupdate')
exp = client.get_experiment(experiment_name='mdupdate')
```

<br/>

```
$ pip install numpy kubernetes kfp
$ dsl-compile --py LightweightPipeline.py --output LightweightPipeline.yaml

$ dsl-compile --py RecommenderPipeline.py --output RecommenderPipeline.yaml

$ wget https://github.com/kubeflow/pipelines/archive/0.2.5.tar.gz
$ tar -xvf 0.2.5.tar.gz

$ dsl-compile --py ConditionalPipeline.py --output ConditionalPipeline.yaml
```

<br/>

localhost:7777

<br/>

<!-- ```

argo submit training-sk-mnist-workflow.yaml -n kubeflow
argo submit serving-sk-mnist-workflow.yaml -n kubeflow -p deploy-model=true
``` -->

```
$ argo submit LightweightPipeline.yaml -n kubeflow -p deploy-model=true
$ argo submit RecommenderPipeline.yaml -n kubeflow -p deploy-model=true
$ argo submit ConditionalPipeline.yaml -n kubeflow -p deploy-model=true
```

<br/>

Или

<br/>

```
// OK!
RUN -> Pipeline -> LightweightPipeline -> Запускается контейнер: calculation-pipeline

// FAIL! Error reading file recommender/directory.txt from bucket data
RUN -> Pipeline -> RecommenderPipeline -> Запускается recommender-model-update

// OK!
RUN -> Pipeline -> LightweightPipeline -> Запускается conditional-execution-pipeline
```

<br/>

### (???) Storing Data Between Steps

<br/>

```
$ cd data-extraction/python-notebook
$ dsl-compile --py MailingListDataPrep.py --output MailingListDataPrep.yaml
```
