---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - Monitoring a ML Model
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - Monitoring a ML Model
keywords: courses, devops to mlops bootcamp, Monitoring and Autoscaling a ML Model
permalink: /courses/mlops/ultimate-devops-to-mlops-bootcamp/monitoring-a-ml-model/
---

# [Course][Udemy][Gourav Shah] Ultimate DevOps to MLOps Bootcamp - Build ML CI-CD Pipelines [ENG, 2025] : 09. Monitoring a ML Model

<br/>

**Делаю:**  
2025.12.30

<br/>

// OpenTelemetry FastAPI Instrumentation
https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/fastapi/fastapi.html

<br/>

**src/api/requirements.txt**

<br/>

```
prometheus-fastapi-instrumentator==6.1.0
```

<br/>

**src/api/main.py**

<br/>

```
from prometheus_fastapi_instrumentator import Instrumentator
```

<br/>

После

```
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

<br/>

Добавляю:

<br/>

```
# Initialize and instrument Prometheus metrics
Instrumentator().instrument(app).expose(app)
```

<br/>

```
$ kubectl rollout restart deployment model
```

<br/>

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: house-price-api-monitor
  labels:
    release: prom
spec:
  selector:
    matchLabels:
      app: model
  namespaceSelector:
    matchNames:
      - default
  endpoints:
    - port: "8000"
      path: /metrics
      interval: 15s
EOF
```

```
// OK!
$ curl http://localhost:30100/metrics
```

<br/>

```
// swagger
http://localhost:30100/docs

// prometheus
http://localhost:30300/targets
```

<br/>

// Удалили gist.
// Наверное забанили за много аккаунтов
https://gist.githubusercontent.com/initcron/ca57251c80bc2f4a2adde0a878ebc585/raw/f6fb4304ebb026725c8c4d0e54c37d87ae64cafb/enhanced_fastapi_ml_dashboard.json

<br/>

```
// import grafana dashboard
http://localhost:30200/dashboard/import
```
