---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End
keywords: courses, devops to mlops bootcamp
permalink: /courses/mlops/ultimate-devops-to-mlops-bootcamp/packaging-model-along-with-fastapi-wrapper-aand-streamlit-with-containers/
---

# [Course][Udemy][Gourav Shah] Ultimate DevOps to MLOps Bootcamp - Build ML CI-CD Pipelines [ENG, 2025] : 06. Packaging Model along with FastAPI Wrapper and Streamlit with Containers

<br/>

**Делаю:**  
2025.12.27

<br/>

```
$ cd ~/projects/courses/mlops/house-price-predictor/
$ source .venv/bin/activate
```

<br/>

```bash
$ python src/data/run_processing.py \
  --input data/raw/house_data.csv \
  --output data/processed/cleaned_house_data.csv
```

<br/>

```bash
// Running Feature Engineering and Preprocessing Jobs
$ python src/features/engineer.py \
  --preprocessor models/trained/preprocessor.pkl \
  --input data/processed/cleaned_house_data.csv \
  --output data/processed/featured_house_data.csv
```

<br/>

Explore and run the notebook: notebooks/03_experimentation.ipynb totun the model experiments.
This will generate configs/model_config.yaml

If you have not run this notebook, download the sample config from model_config and add it to
configs/model_config.yaml

<br/>

```bash
// Building and Training Final Model with Configs from Data Scientists
$ python src/models/train_model.py \
  --config configs/model_config.yaml \
  --data data/processed/featured_house_data.csv \
  --models-dir models \
  --mlflow-tracking-uri http://localhost:5555
```

<br/>

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
CTRL^C, CTRL^D
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
$ docker login
$ docker push docker.io/webmakaka/fastapi:dev
$ docker push docker.io/webmakaka/streamlit:dev
```

<br/>

```
$ docker compose stop
```
