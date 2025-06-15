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

**Делаю:**  
2025.06.15

<br/>

## 03. Use Case and Environment Setup

<br/>

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

### 08. Setting up Python Virtual Environment with UV

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

### 09. Working with Jupyter Notebooks

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

<br/>

## 04. From Data to Models - Understanding Data Science with Feature Engineering

<br/>

### 02. Learning Data Engineering

```bash
$ python src/data/run_processing.py   --input data/raw/house_data.csv   --output data/processed/cleaned_house_data.csv
```

<br/>

### 06. Preparing for Model Experimentation

```bash
$ python src/features/engineer.py   --input data/processed/cleaned_house_data.csv   --output data/processed/featured_house_data.csv   --preprocessor models/trained/preprocessor.pkl
```
