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
https://github.com/webmakaka/Kubeflow-for-Machine-Learning-From-Lab-to-Production.git

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

<br/>

```
$ {
  export KUBEFLOW_PROJECT_NAME=marley-kubeflow \
  export KUBEFLOW_HOME=~/kubeflow/${KUBEFLOW_PROJECT_NAME}
  mkdir -p ${KUBEFLOW_HOME} && cd ${KUBEFLOW_HOME}
}
```

<br/>

```
// This deployment process can take up to 30 minutes.
$ kfctl apply -V -f https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.1.yaml


// Не заработало
// Большое количество ошибок
// $ kfctl apply -V -f https://raw.githubusercontent.com/kubeflow/manifests/v1.2-branch/kfdef/kfctl_k8s_istio.v1.2.0.yaml
```

<br/>

```
$ cd ~/tmp/
$ git clone https://github.com/intro-to-ml-with-kubeflow/intro-to-ml-with-kubeflow-examples.git
$ cd ~/tmp/intro-to-ml-with-kubeflow-examples/ch2_seldon_examples/
```

<br/>

```
$ kubectl apply -f ./pipeline_role.yaml
$ kubectl apply -f ./pipeline_rolebinding.yaml
```

<br/>

```
$ kubectl get pods -n kubeflow
NAME                                                          READY   STATUS             RESTARTS   AGE
admission-webhook-bootstrap-stateful-set-0                    1/1     Running            0          36m
admission-webhook-deployment-59bc556b94-6spfv                 0/1     Terminating        0          36m
admission-webhook-deployment-59bc556b94-vnjbn                 1/1     Running            0          35m
application-controller-stateful-set-0                         1/1     Running            0          39m
argo-ui-5f845464d7-fqrzf                                      1/1     Running            0          36m
centraldashboard-d5c6d6bf-drsz5                               1/1     Running            0          36m
jupyter-web-app-deployment-544b7d5684-sbbsd                   1/1     Running            0          36m
katib-controller-6b87947df8-twhf9                             1/1     Running            1          36m
katib-db-manager-54b64f99b-2mk5v                              1/1     Running            1          36m
katib-mysql-74747879d7-z2hgs                                  1/1     Running            0          36m
katib-ui-76f84754b6-twtlr                                     1/1     Running            0          36m
kfserving-controller-manager-0                                1/2     ImagePullBackOff   0          9m45s
metacontroller-0                                              1/1     Running            0          36m
metadata-db-79d6cf9d94-2c8fb                                  1/1     Running            0          36m
metadata-deployment-5dd4c9d4cf-6lcmb                          1/1     Running            0          36m
metadata-envoy-deployment-5b9f9466d9-wkgsg                    1/1     Running            0          36m
metadata-grpc-deployment-66cf7949ff-62kdl                     1/1     Running            3          36m
metadata-ui-8968fc7d9-9cwgm                                   1/1     Running            0          36m
minio-5dc88dd55c-tgxlt                                        1/1     Running            0          36m
ml-pipeline-55b669bf4d-qwcvh                                  1/1     Running            0          36m
ml-pipeline-ml-pipeline-visualizationserver-c489f5dd8-wkgx8   1/1     Running            0          36m
ml-pipeline-persistenceagent-f54b4dcf5-fhrkg                  1/1     Running            1          36m
ml-pipeline-scheduledworkflow-7f5d9d967b-hnmm9                1/1     Running            0          36m
ml-pipeline-ui-7bb97bf8d8-5kpbc                               1/1     Running            0          36m
ml-pipeline-viewer-controller-deployment-584cd7674b-ddb6l     1/1     Running            0          36m
mysql-66c5c7bf56-d6g9b                                        1/1     Running            0          36m
notebook-controller-deployment-576589db9d-6gfvw               1/1     Running            0          36m
profiles-deployment-874649f89-4wv27                           2/2     Running            0          36m
pytorch-operator-666dd4cd49-b6zgf                             1/1     Running            0          36m
seldon-controller-manager-5d96986d47-m5sjv                    1/1     Running            0          36m
spark-operatorcrd-cleanup-qgbj8                               0/2     Completed          0          36m
spark-operatorsparkoperator-7c484c6859-6hsvm                  1/1     Running            0          36m
spartakus-volunteer-7465bcbdc-4vcxl                           1/1     Running            0          36m
tensorboard-6549cd78c9-zxh42                                  1/1     Running            0          36m
tf-job-operator-7574b968b5-vr4kt                              1/1     Running            0          36m
workflow-controller-6db95548dd-7mtks                          1/1     Running
```

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
$ cd ~/tmp/intro-to-ml-with-kubeflow-examples/ch2_seldon_examples/
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

???

<br/>

https://github.com/intro-to-ml-with-kubeflow/intro-to-ml-with-kubeflow-examples/blob/master/ch2/query-endpoint.py

<br/>

### MINio

```
$ kubectl port-forward -n kubeflow svc/minio-service 9000:9000
```

<br/>

## 04. Kubeflow Pipelines

<br/>

```
$ cd ~/tmp/intro-to-ml-with-kubeflow-examples/ch04/code
$ mv Lightweight\ Pipeline.py LightweightPipeline.py
```

<br/>

```
$ pip install numpy
$ dsl-compile --py LightweightPipeline.py --output LightweightPipeline.yaml
```

```
https://github.com/intro-to-ml-with-kubeflow/intro-to-ml-with-kubeflow-examples/blob/master/ch04/code/Lightweight%20Pipeline.ipynb
```
