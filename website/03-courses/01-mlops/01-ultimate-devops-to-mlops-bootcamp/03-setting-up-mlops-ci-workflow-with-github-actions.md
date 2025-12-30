---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - Setting up MLOps CI Workflow with GitHub Actions
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - Setting up MLOps CI Workflow with GitHub Actions
keywords: courses, devops to mlops bootcamp, Setting up MLOps CI Workflow with GitHub Actions
permalink: /courses/mlops/ultimate-devops-to-mlops-bootcamp/setting-up-mlops-ci-workflow-with-github-actions/
---

# [Course][Udemy][Gourav Shah] Ultimate DevOps to MLOps Bootcamp - Build ML CI-CD Pipelines [ENG, 2025] : 07. Setting up MLOps CI Workflow with GitHub Actions

<br/>

**Делаю:**  
2025.12.29

<!-- <br/>

https://github.com/gouravshah/house-price-predictor3/tree/main/.github/workflows -->

<br/>

### 04. Writing an executung out first GitHub Actions Workflow

<br/>

hub.docker.com -> Login -> Account Settings -> Personal access tokens -> Generate new token

<br/>

https://app.docker.com/accounts/webmakaka/settings/personal-access-tokens

<br/>

```
Description: github-webmakaka
Expiration date: none
Optional: Read & Write
```

Generate, Скопировать токен.

<br/>

Github -> Repo -> house-price-predictor -> Settings -> Secrets and variables -> Actions -> Variables -> Repostitory variables -> New repository variable

<br/>

https://github.com/webmakaka/house-price-predictor/settings/variables/actions

<br/>

```
DOCKERHUB_USERNAME
```

<br/>

Secrets -> New repository secret

```
DOCKERHUB_TOKEN
```

<br/>

// Создаю Dockerfile
streamlit_app/Dockerfile

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
$ vi .github/workflows/streamlit-ci.yaml
```

<br/>

```yaml
name: Streamlit CI

on:
  push:
    paths:
      - 'streamlit_app/**'
  workflow_dispatch:

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to DockerHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: docker.io
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: ./streamlit_app
          push: true
          tags: docker.io/${{ vars.DOCKERHUB_USERNAME }}/streamlit:latest
```

<br/>

https://github.com/webmakaka/house-price-predictor/actions

// OK!
RUN PIPELINE

<br/>

configs/model_config.yaml

```
model:
  best_model: GradientBoosting
  feature_sets:
    rfe:
    - '0'
    - '1'
    - '2'
    - '3'
    - '4'
    - '5'
    - '9'
    - '10'
    - '13'
    - '14'
  mae: 12310.638379356631
  name: house_price_model
  parameters:
    alpha: 0.9
    ccp_alpha: 0.0
    criterion: friedman_mse
    init: null
    learning_rate: 0.1
    loss: squared_error
    max_depth: 3
    max_features: null
    max_leaf_nodes: null
    min_impurity_decrease: 0.0
    min_samples_leaf: 1
    min_samples_split: 2
    min_weight_fraction_leaf: 0.0
    n_estimators: 100
    n_iter_no_change: null
    random_state: null
    subsample: 1.0
    tol: 0.0001
    validation_fraction: 0.1
    verbose: 0
    warm_start: false
  r2_score: 0.9937776455685025
  target_variable: price
```

<br/>

// Создаю Dockerfile
Dockerfile

<br/>

```
FROM python:3.11-slim
WORKDIR /app
COPY src/api/ .
RUN pip install -r requirements.txt
COPY models/trained/*.pkl models/trained/
EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
```

<br/>

```
$ vi .github/workflows/mlops-pipeline.yml
```

```yaml
name: MLOps Pipeline

on:
  push:
    branches: [main]
    tags: ['v*.*.*']
  pull_request:
    branches: [main]

jobs:
  data-processing:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Process data
        run: |
          python src/data/run_processing.py --input data/raw/house_data.csv --output data/processed/cleaned_house_data.csv

      - name: Engineer features
        run: |
          python src/features/engineer.py --input data/processed/cleaned_house_data.csv --output data/processed/featured_house_data.csv --preprocessor models/trained/preprocessor.pkl

      - name: Upload processed data
        uses: actions/upload-artifact@v4
        with:
          name: processed-data
          path: data/processed/featured_house_data.csv

      - name: Upload preprocessor
        uses: actions/upload-artifact@v4
        with:
          name: preprocessor
          path: models/trained/preprocessor.pkl

  model-training:
    needs: data-processing
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Download processed data
        uses: actions/download-artifact@v4
        with:
          name: processed-data
          path: data/processed/

      - name: Set up MLflow
        run: |
          docker pull ghcr.io/mlflow/mlflow:latest
          docker run -d -p 5000:5000 --name mlflow-server ghcr.io/mlflow/mlflow:latest mlflow server --host 0.0.0.0 --backend-store-uri sqlite:///mlflow.db

      - name: Wait for MLflow to start
        run: |
          for i in {1..10}; do
            curl -f http://localhost:5000/health || sleep 5;
          done

      - name: Train model
        run: |
          mkdir -p models
          python src/models/train_model.py --config configs/model_config.yaml --data data/processed/featured_house_data.csv --models-dir models --mlflow-tracking-uri http://localhost:5000

      - name: Upload trained model
        uses: actions/upload-artifact@v4
        with:
          name: trained-model
          path: models/

      - name: Clean up MLflow
        run: |
          docker stop mlflow-server || true
          docker rm mlflow-server || true

  build-and-publish:
    needs: model-training
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Download trained model
        uses: actions/download-artifact@v4
        with:
          name: trained-model
          path: models/

      - name: Download preprocessor
        uses: actions/download-artifact@v4
        with:
          name: preprocessor
          path: models/trained/

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to DockerHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: docker.io
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: ./Dockerfile
          push: true
          tags: docker.io/${{ vars.DOCKERHUB_USERNAME }}/house-price-model:latest
```
