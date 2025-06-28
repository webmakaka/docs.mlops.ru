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

https://github.com/initcron/hprice-predictor  
https://github.com/gouravshah/hprice-predictor/

<br/>

**Делаю:**  
2025.06.24

<br/>

```
$ sudo apt install -y tree jq
```

<br/>

## 03. Use Case and Environment Setup

<br/>

### 06. Launching MLflow for Experiemnt Tracking

<br/>

```
$ mkdir -p ~/projects/courses/mlops
$ cd ~/projects/courses/mlops/
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
$ cd ~/projects/courses/mlops/
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

<br/>

## 04. From Data to Models - Understanding Data Science with Feature Engineering

<br/>

### 02. Learning Data Engineering

```bash
$ python src/data/run_processing.py \
  --input data/raw/house_data.csv \
  --output data/processed/cleaned_house_data.csv
```

<br/>

### 06. Preparing for Model Experimentation

```bash
$ python src/features/engineer.py \
  --input data/processed/cleaned_house_data.csv \
  --output data/processed/featured_house_data.csv \
  --preprocessor models/trained/preprocessor.pkl
```

<br/>

## 06. Packaging Model along with FastAPI Wrapper and Streamlit with Containers

<br/>

### 03. Running Feature Engineering and Preprocessing Jobs

```bash
$ python src/features/engineer.py \
  --input data/processed/cleaned_house_data.csv \
  --output data/processed/featured_house_data.csv \
  --preprocessor models/trained/preprocessor.pkl
```

<br/>

### 04. Building and Training Final Model with Configs from Data Scientists

```bash
$ python src/models/train_model.py \
  --config configs/model_config.yaml \
  --data data/processed/featured_house_data.csv \
  --models-dir models \
  --mlflow-tracking-uri http://localhost:5555
```

http://localhost:5555/#/models

В UI появилась зарегистрированная модель

<br/>

```
$ tree
```

<br/>

Появилась модель house_price_model.pkl

```
├── models
│   └── trained
│       ├── house_price_model.pkl
│       ├── preprocessor.pkl
│       └── README.md
```

<br/>

### 06. Writing Dockerfile to package Model with FastAPI Wrapper

Код из репо выше

<br/>

```
$ vi Dockerfile
```

<br/>

```
FROM python:3.11-slim

WORKDIR /app

COPY src/api/ .

RUN pip install -r requirements.txt

COPY models/trained/*.pkl models/trained/

EXPOSE 8000

CMD [ "uvicorn",  "main:app",  "--host",  "0.0.0.0",  "--port",  "8000" ]
```

<br/>

```
$ docker image build -t fastapi .
```

<br/>

### 07. Debugging and Fixing Image Failures, Launch and Validate FastAPI

<br/>

```
$ docker run --rm -it fastapi:latest bash
```

<br/>

```
# uvicorn main:app --host 0.0.0.0 --port 8000
INFO:     Started server process [7]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

<br/>

```
^C^D
```

<br/>

```
$ docker run -idtP fastapi:latest
```

<br/>

```
$ docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED         STATUS         PORTS                                           NAMES
7b7be31c8f03   fastapi:latest                 "uvicorn main:app --…"   5 seconds ago   Up 4 seconds   0.0.0.0:32768->8000/tcp, [::]:32768->8000/tcp   silly_dirac
```

<br/>

```
// OK!
// Открылся swagger
http://localhost:32768/docs
```

<br/>

```
$ curl -X POST "http://localhost:32768/predict" \
-H "Content-Type: application/json" \
-d '{
  "sqft": 1500,
  "bedrooms": 3,
  "bathrooms": 2,
  "location": "suburban",
  "year_built": 2000,
  "condition": "fair"
}' | jq
```

<br/>

**response:**

```json
{
  "predicted_price": 487238.4,
  "confidence_interval": [438514.56, 535962.24],
  "features_importance": {},
  "prediction_time": "2025-06-24T10:36:53.604637"
}
```

<br/>

### 08. Packaging and testing Streamlit App

```
$ cd streamlit_app
```

<br/>

```
$ vi Dockerfile
```

<br/>

```
FROM python:3.9-slim

WORKDIR /app

COPY  app.py requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD  [ "streamlit", "run", "app.py", "--server.address=0.0.0.0" ]
```

<br/>

```
$ docker image build -t webmakaka/streamlit:v1 .
$ docker login
$ docker push webmakaka/streamlit:v1
```

<br/>

### 09. Packaging and Model Serving Infra with Docker Compose

<br/>

```
$ vi docker-compose.yaml
```

<br/>

```
services:
  fastapi:
    image: docker.io/webmakaka/fastapi:dev
    build:
      context: "./"
      dockerfile: "Dockerfile"
    ports:
      - "8000:8000"

  streamlit:
    image: docker.io/webmakaka/streamlit:dev
    build:
      context: "streamlit_app/"
      dockerfile: "Dockerfile"
    ports:
      - "8501:8501"
    environment:
      API_URL: "http://fastapi:8000"
```

<br/>

```
$ docker compose build
$ docker compose up -d
```

<br/>

```
// OK!
http://localhost:8501/
```

<br/>

```
$ docker push docker.io/webmakaka/fastapi:dev
$ docker push docker.io/webmakaka/streamlit:dev
```

<br/>

```
$ docker compose stop
```

<br/>

## 07. Setting up MLOps CI Workflow with GitHub Actions

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

<br/>

## 08. Building Scalable Prod Inference Infrastructure with Kubernetes

<br/>

### 04. Simplest way to build a 3 Node Kubernetes Cluster with KIND

<br/>

Инсталляция и создание kubernetes кластера [kind](//gitops.ru/tools/containers/kubernetes/kind/)

<br/>

### 06. Deploying Streamlit Frontent App with Kubernetes

```
$ kubectl create deployment streamlit --image=webmakaka/streamlit:latest --port=8501
```

### 07. Exposing the Streamlit App with Kubernetes NodePort Service

<br/>

```
$ kubectl create service nodeport streamlit --tcp=8501 --node-port=30000
```

<br/>

### 08. Creating Deployment Service for the Model wrapped in FastAPI

```
$ kubectl create deployment model --image=webmakaka/house-price-model:latest --port=8000
```

<br/>

```
$ kubectl create service nodeport model --tcp=8000 --node-port=30100
```

```
// OK!
http://localhost:30100/docs
http://localhost:30000
```
