---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - GitOps Based Deployments for MLLLM Apps
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - GitOps Based Deployments for MLLLM Apps
keywords: courses, devops to mlops bootcamp, GitOps Based Deployments for MLLLM Apps
permalink: /courses/mlops/ultimate-devops-to-mlops-bootcamp/gitops-based-deployments-for-mlllm-apps/
---

# [Course][Udemy][Gourav Shah] Ultimate DevOps to MLOps Bootcamp - Build ML CI-CD Pipelines [ENG, 2025] : 10. GitOps Based Deployments for MLLLM Apps

<br/>

**Делаю:**  
2025.12.30

<br/>

### [Инсталляция ArgoCD в kind](//docs.gitops.ru//tools/containers/kubernetes/utils/ci-cd/argo/argo-cd/setup/kind/helm/)

<br/>

```
$ kubectl delete deploy,svc model streamlit
deployment.apps "model" deleted
deployment.apps "streamlit" deleted
service "model" deleted
service "streamlit" deleted
```

<br/>

```
http://argocd.k8s.local/applications

New App

Application Name: house-price-predictor
Project Name: default
Sync Policy: Automatic

+ Enable Auto Sync
+ Prune Resources
+ Self Heal

Repository URL: https://github.com/gouravshah/house-price-predictor.git
Revison: release
Path: deployment/kubernetes

Cluster URL: https://kubernetes.default.svc
Namespace: default

+ kustomize


CREATE
```

<br/>

```
$ kubectl get application -A
NAMESPACE   NAME                    SYNC STATUS   HEALTH STATUS
argocd      house-price-predictor   OutOfSync     Healthy
```

<br/>

```
$ kubectl describe applications house-price-predictor -n argocd
```
