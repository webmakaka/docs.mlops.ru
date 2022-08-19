---
layout: page
title: Machine Learning on Kubernetes - Инсталляция Open Data Hub (ODH)
description: Machine Learning on Kubernetes - Инсталляция Open Data Hub (ODH)
keywords: Machine Learning on Kubernetes - Инсталляция Open Data Hub (ODH)
permalink: /study/books/machine-learning-on-kubernetes/environment/installing-open-data-hub/
---

# Инсталляция Open Data Hub (ODH)

<br/>

```
$ kubectl create ns ml-workshop
```

<br/>

```
$ minikube ip --profile ${PROFILE}
```

<br/>

```
$ export MINIKUBE_IP_ADDR=192.168.49.2
```

<br/>

```
// Check
// $ envsubst < manifests/kfdef/ml-platform.yaml
```

<br/>

```
$ envsubst < manifests/kfdef/ml-platform.yaml | kubectl create -f - -n ml-workshop
```

<br/>

```
// Минут 15 ждать
$ watch kubectl get pods -n ml-workshop
```

<br/>

```
NAME                                                   READY   STATUS             RESTARTS        AGE
app-aflow-airflow-scheduler-6f9c44866d-km4fp           2/2     Running            0               11m
app-aflow-airflow-web-686b66f886-5bqvj                 2/2     Running            0               11m
app-aflow-airflow-web-6d9587698-lhrq9                  1/2     CrashLoopBackOff   4 (34s ago)     3m24s
app-aflow-airflow-worker-0                             2/2     Running            0               11m
app-aflow-postgresql-0                                 1/1     Running            0               11m
app-aflow-redis-master-0                               1/1     Running            0               11m
flightsdatadb-0                                        1/1     Running            0               8m47s
grafana-56594fd448-2ccnc                               1/1     Running            0               11m
jupyterhub-6cff7d6cc5-m7ww7                            1/1     Running            0               11m
jupyterhub-db-0                                        1/1     Running            0               11m
minio-ml-workshop-7fcc5dfd8-7p6df                      1/1     Running            0               11m
minio-ml-workshop-kxwst                                0/1     Completed          2               11m
mlflow-5fb4cb5d5d-mxxt4                                2/2     Running            0               11m
mlflow-db-0                                            1/1     Running            1 (9m53s ago)   11m
ocp-deploy.01026fe0d07d4955bc73a8652e0675e5            0/1     Error              0               92s
ocp-deploy.090131ec340e4bdaa951e273081bdfcd            0/1     Error              0               21s
ocp-deploy.0d55450446f64a359ee56ea4106cfb3a            0/1     Error              0               2m36s
ocp-deploy.1068ef4553e040378cbd69475c8817ef            0/1     Error              0               2m37s
ocp-deploy.1445e1add9b24c65a845aaf988295893            0/1     Error              0               22s
ocp-deploy.16444de519a541039265a8ec9038920b            0/1     Error              0               2m36s
ocp-deploy.1d03c0cb51064d24af2d12c62f9901b0            0/1     Error              0               25s
ocp-deploy.23967c4ff07746e9b314607f75eca93b            0/1     Error              0               2m36s
ocp-deploy.286e89755cca4617adc22b7d1ec4c0a9            0/1     Error              0               32s
ocp-deploy.43cecdec4d294b57813d33a0027b8b44            0/1     Error              0               29s
ocp-deploy.4696cdadc3e04d39b37eb4a8432f86b8            0/1     Error              0               2m36s
ocp-deploy.4de46a6345ea40c2b18c0487c519e61c            0/1     Error              0               40s
ocp-deploy.4e3f125dc47a4103b6ae7cdae5560901            0/1     Error              0               2m36s
ocp-deploy.4fe062d6c51b43a0817f9ee628c8bfcf            0/1     Error              0               82s
ocp-deploy.5b78a6988dc5473ebedd65781402a477            0/1     Error              0               82s
ocp-deploy.61705a4c203d4c4c9cc93a3b2349bac6            0/1     Error              0               16s
ocp-deploy.74d0e740a9fc4d3f941cf7ecc60c4ccb            0/1     Error              0               87s
ocp-deploy.8697d1fbe7cd41c7a139d687ba37d82d            0/1     Error              0               77s
ocp-deploy.8c471bc9308a48ffb1d62a35deb3766a            0/1     Error              0               24s
ocp-deploy.90fa468b78e945f3984f3ce92fbe7989            0/1     Error              0               38s
ocp-deploy.9282596e8cf44f348995729ea26d70a7            0/1     Error              0               2m36s
ocp-deploy.93be9c3d5d5c4f95a5aec59c6cc06f14            0/1     Error              0               38s
ocp-deploy.9fd209473a2e47eb9dcade35172fa802            0/1     Error              0               79s
ocp-deploy.a0f32dd8c9e548fab940fea23944f417            0/1     Error              0               2m37s
ocp-deploy.a14c0241bc994c43958886f5163af32f            0/1     Error              0               88s
ocp-deploy.bd1fad0c6a5e432587fd07e9c9f0e656            0/1     Error              0               2m37s
ocp-deploy.c3253adc6d3f4ffc91f869b36f3367df            0/1     Error              0               101s
ocp-deploy.c786759a255f491fbaed004773044622            0/1     Error              0               95s
ocp-deploy.d9cbf9e1d1c74c3bb8de8b560feb67de            0/1     Error              0               19s
ocp-deploy.df39ca5b261c4cc2bfbf30c580488500            0/1     Error              0               2m37s
ocp-deploy.e278d4a2681942d7b3423a9b72f4c651            0/1     Error              0               97s
ocp-deploy.e7fa8a0b0b724d489be16ff4b059ef3f            0/1     Error              0               26s
ocp-deploy.e9e1516abdae47dc843994da99788608            0/1     Error              0               26s
ocp-deploy.f20d6e53bd2c478a9fb053bf18ac7fa9            0/1     Error              0               19s
ocp-deploy.f2485d3496ef430a876eb0fdd6bea2ce            0/1     Error              0               30s
ocp-deploy.f6bdb4babc3443bf9b97ca79d4049e7a            0/1     Error              0               2m36s
prometheus-odh-monitoring-0                            2/2     Running            0               6m53s
prometheus-operator-7869664bcc-2qhdz                   1/1     Running            0               8m53s
seldon-controller-manager-c5f59c56d-zl6lr              1/1     Running            0               11m
spark-operator-6bc4f8f5f8-v44xp                        1/1     Running            0               11m
start-spark-cluster.00fac27ba8714a2f84dac067f298bf4d   0/1     Error              0               62s
start-spark-cluster.18c858eb34bf45a3883da9333abc7630   0/1     Error              0               46s
start-spark-cluster.2234155fbada403097d0c941a157396c   0/1     Error              0               46s
start-spark-cluster.30862e2931c24fcfa87533d776cab966   0/1     Error              0               2m36s
start-spark-cluster.4065f59845914c138aa1e82779757dbe   0/1     Error              0               47s
start-spark-cluster.4107277e2dad43c8993299c48326157c   0/1     Error              0               77s
start-spark-cluster.4361921b06544feb99f6eade2b7d25df   0/1     Error              0               47s
start-spark-cluster.437f317f24874ebb9c202a4286b545b9   0/1     Error              0               2m36s
start-spark-cluster.4f636af3eb6042ff97bfc0c3f53cb3a0   0/1     Error              0               51s
start-spark-cluster.51d42eeb3156478698a7fc92902477dd   0/1     Error              0               64s
start-spark-cluster.6f778660252e4540840653db8aaaa667   0/1     Error              0               72s
start-spark-cluster.6fca26239c64440798cfcc0c53257d97   0/1     Error              0               53s
start-spark-cluster.7aa90f7284e84de69e06956e4e06b749   0/1     Error              0               102s
start-spark-cluster.86f57615ee904e55a565246b9f1ae5f3   0/1     Error              0               49s
start-spark-cluster.89aa03b068a549fbbeda0ccbeb9f66ce   0/1     Error              0               75s
start-spark-cluster.a7855fc6b693425ca4b0504b68a8a6d6   0/1     Error              0               64s
start-spark-cluster.ab381d2f5f91405bba46c91cc5db44c0   0/1     Error              0               73s
start-spark-cluster.ae1326a8ae5e4ac98b399306ea1eccfe   0/1     Error              0               65s
start-spark-cluster.bc611ce2248f427086faf11e3e980575   0/1     Error              0               79s
start-spark-cluster.d1a79c83580f4b70a1b8e69ea9d98b6f   0/1     Error              0               2m36s
start-spark-cluster.d59577ad42a0468e91b5a2bac4dc5959   0/1     Error              0               2m36s
start-spark-cluster.e0135911b788400aaac740576a8a9426   0/1     Error              0               48s
start-spark-cluster.efa82071ac2e4c76abe3d02da6256cb7   0/1     Error              0               45s
start-spark-cluster.f158946606c9475899df532e6c83bc9b   0/1     Error              0               2m36s
start-spark-cluster.f7049b7890324f5cbc9a4f692cd63534   0/1     Error              0               72s
start-spark-cluster.fc6536234d1341c4bdeae0813eaed46c   0/1     Error              0               46s

```

<br/>

```
$ kubectl get all -n ml-workshop
```

<br/>

```
***
NAME                                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)              AGE
service/app-aflow-airflow                   ClusterIP   10.106.233.18    <none>        8080/TCP             11m
service/app-aflow-airflow-worker-headless   ClusterIP   None             <none>        8793/TCP             11m
service/app-aflow-postgresql                ClusterIP   10.104.154.83    <none>        5432/TCP             11m
service/app-aflow-postgresql-headless       ClusterIP   None             <none>        5432/TCP             11m
service/app-aflow-redis-headless            ClusterIP   None             <none>        6379/TCP             11m
service/app-aflow-redis-master              ClusterIP   10.99.0.186      <none>        6379/TCP             11m
service/flightsdatadb                       ClusterIP   10.103.152.170   <none>        5432/TCP             9m17s
service/grafana                             ClusterIP   10.105.49.130    <none>        3000/TCP             11m
service/jupyterhub                          ClusterIP   10.110.27.45     <none>        8080/TCP,8081/TCP    12m
service/jupyterhub-db                       ClusterIP   10.105.3.90      <none>        5432/TCP             12m
service/minio-ml-workshop                   ClusterIP   10.101.161.251   <none>        9000/TCP,33933/TCP   11m
service/mlflow                              ClusterIP   10.104.199.112   <none>        5000/TCP,5500/TCP    11m
service/mlflow-db                           ClusterIP   10.97.125.116    <none>        5432/TCP             11m
service/prometheus-operated                 ClusterIP   None             <none>        9090/TCP             7m23s
service/seldon-webhook-service              ClusterIP   10.99.208.129    <none>        443/TCP              10m

NAME                                          READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/app-aflow-airflow-scheduler   1/1     1            1           11m
deployment.apps/app-aflow-airflow-web         1/1     1            1           11m
deployment.apps/grafana                       1/1     1            1           11m
deployment.apps/jupyterhub                    1/1     1            1           12m
deployment.apps/minio-ml-workshop             1/1     1            1           11m
deployment.apps/mlflow                        1/1     1            1           11m
deployment.apps/prometheus-operator           1/1     1            1           9m23s
deployment.apps/seldon-controller-manager     1/1     1            1           11m
deployment.apps/spark-operator                1/1     1            1           11m

NAME                                                     DESIRED   CURRENT   READY   AGE
replicaset.apps/app-aflow-airflow-scheduler-6f9c44866d   1         1         1       11m
replicaset.apps/app-aflow-airflow-web-686b66f886         1         1         1       11m
replicaset.apps/app-aflow-airflow-web-6d9587698          1         1         0       3m54s
replicaset.apps/grafana-56594fd448                       1         1         1       11m
replicaset.apps/jupyterhub-6cff7d6cc5                    1         1         1       12m
replicaset.apps/minio-ml-workshop-7fcc5dfd8              1         1         1       11m
replicaset.apps/mlflow-5fb4cb5d5d                        1         1         1       11m
replicaset.apps/prometheus-operator-7869664bcc           1         1         1       9m23s
replicaset.apps/seldon-controller-manager-c5f59c56d      1         1         1       11m
replicaset.apps/spark-operator-6bc4f8f5f8                1         1         1       11m

NAME                                         READY   AGE
statefulset.apps/app-aflow-airflow-worker    1/1     11m
statefulset.apps/app-aflow-postgresql        1/1     11m
statefulset.apps/app-aflow-redis-master      1/1     11m
statefulset.apps/flightsdatadb               1/1     9m17s
statefulset.apps/jupyterhub-db               1/1     12m
statefulset.apps/mlflow-db                   1/1     11m
statefulset.apps/prometheus-odh-monitoring   1/1     7m23s

NAME                          COMPLETIONS   DURATION   AGE
job.batch/minio-ml-workshop   1/1           94s        11m

```
