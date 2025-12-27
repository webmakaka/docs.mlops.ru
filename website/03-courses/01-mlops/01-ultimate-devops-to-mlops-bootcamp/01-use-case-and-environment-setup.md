---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
keywords: courses, devops to mlops bootcamp
permalink: /courses/mlops/ultimate-devops-to-mlops-bootcamp/use-case-and-environment-setup/
---

# [Course][Udemy][Gourav Shah] Ultimate DevOps to MLOps Bootcamp - Build ML CI-CD Pipelines [ENG, 2025] : 03. Use Case and Environment Setup

<br/>

**Делаю:**  
2025.12.26

<br/>

```
$ sudo apt install -y tree jq
```

<br/>

```
$ mkdir -p ~/projects/courses/mlops
$ cd ~/projects/courses/mlops/
```

<br/>

```
$ git clone git@github.com:webmakaka/house-price-predictor.git
```

<br/>

```
// Run MLFLOW
$ cd house-price-predictor/deployment/mlflow/
$ docker compose up
```

<br/>

```
// OK!
http://localhost:5555
```

<br/>

```
// Setting up Python Virtual Environment with UV
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

<br/>

```
$ cd ~/projects/courses/mlops/house-price-predictor/
$ uv venv --python python3.11
$ source .venv/bin/activate
$ uv pip install -r requirements.txt
```

```
$ code .
```

<br/>

```
CTRL^P
```

<br/>

```
ext install ms-python.python
ext install ms-toolsai.jupyter
```

<br/>

```
В vscode

Run All -> notebooks\*.ipynb
```

<br/>

В результате в MlFlow должны появиться эксперименты.
