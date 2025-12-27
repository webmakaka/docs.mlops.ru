---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
keywords: courses, devops to mlops bootcamp
permalink: /courses/mlops/ultimate-devops-to-mlops-bootcamp/setting-up-mlops-ci-workflow-with-github-actions/
---

# [Course][Udemy][Gourav Shah] Ultimate DevOps to MLOps Bootcamp - Build ML CI-CD Pipelines [ENG, 2025] : 07. Setting up MLOps CI Workflow with GitHub Actions

<br/>

**Делаю:**  
2025.\*\*\*\*

<br/>

### 04. Writing an executung out first GitHub Actions Workflow

<br/>

https://github.com/gouravshah/house-price-predictor3/tree/main/.github/workflows

<br/>

hub.docker.com -> Login -> Account Settings -> Personal access tokens -> Generate new token

<br/>

```
Description: github-webmakaka
Expiration date: none
Optional: Read & Write
```

Generate, Скопировать токен.

<br/>

Github -> Repo -> house-price-predictor -> Settings -> Secrets and variables -> Actions -> Variables -> Repostitory variables -> New repository variable

```
DOCKERHUB_USERNAME
```

Secrets -> New repository secret

```
DOCKERHUB_TOKEN
```

<br/>

```
$ vi .github/workflows/mlops-pipeline.yml
```

https://github.com/webmakaka/house-price-predictor/blob/main/.github/workflows/mlops-pipeline.yml

<br/>

```
$ vi .github/workflows/streamlit-ci.yaml
```

https://github.com/webmakaka/house-price-predictor/blob/main/.github/workflows/streamlit-ci.yaml
