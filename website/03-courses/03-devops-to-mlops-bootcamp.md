---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
keywords: courses, devops to mlops bootcamp
permalink: /courses/devops-to-mlops-bootcamp/
---

# [Course][Udemy][Gourav Shah] DevOps to MLOps Bootcamp: Build & Deploy ML Systems End-to-End [ENG, 2025]

<br/>

**Git**  
https://github.com/mlopsbootcamp/house-price-predictor

<br/>

Делаю:  
2025.04.12

<br/>

## 03. Use Case and Environment Setup

### 06. Launching MLflow for Experiemnt Tracking

<br/>

```
$ mkdir -p ~/projects/courses/mlops
$ cd ~/projects/courses/mlops/house-price-predictor/
```

<br/>

```
$ git clone git@github.com:webmakaka/house-price-predictor.git
$ cd house-price-predictor/deployment/mlflow/
$ docker compose up
```

<br/>

```
// OK!
http://localhost:5555
```

<br/>

### 8. Setting up Python Virtual Environment with UV

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
$ uv venv --python python3.11
$ source .venv/bin/activate
```

<br/>

```
$ uv pip install -r requirements.txt
```

<br/>

### 9. Working with Jupyter Notebooks

```
$ code .
```

<br/>

```
^P
```

<br/>

```
ext install ms-toolsai.jupyter
```
