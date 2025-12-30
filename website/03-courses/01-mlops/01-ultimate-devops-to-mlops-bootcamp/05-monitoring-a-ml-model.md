---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - Monitoring a ML Model
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - Monitoring a ML Model
keywords: courses, devops to mlops bootcamp, Monitoring a ML Model
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

**enhanced_fastapi_ml_dashboard.json**

https://gist.github.com/gouravjshah/ca57251c80bc2f4a2adde0a878ebc585

<br/>

```json
{
  "title": "ML Model API - Full Observability Dashboard",
  "timezone": "browser",
  "refresh": "10s",
  "schemaVersion": 30,
  "version": 1,
  "panels": [
    {
      "type": "timeseries",
      "title": "Request Rate (Total per Endpoint)",
      "targets": [
        {
          "expr": "sum(rate(http_requests_total[1m])) by (handler)",
          "legendFormat": "{{handler}}",
          "refId": "A"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": { "x": 0, "y": 0, "w": 12, "h": 8 }
    },
    {
      "type": "timeseries",
      "title": "Latency (95th Percentile)",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[1m])) by (le, handler))",
          "legendFormat": "{{handler}}",
          "refId": "B"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": { "x": 12, "y": 0, "w": 12, "h": 8 }
    },
    {
      "type": "timeseries",
      "title": "Error Rate (4xx/5xx Responses)",
      "targets": [
        {
          "expr": "sum(rate(http_requests_total{status=~\"4..|5..\"}[1m])) by (handler)",
          "legendFormat": "{{handler}}",
          "refId": "C"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": { "x": 0, "y": 8, "w": 12, "h": 8 }
    },
    {
      "type": "timeseries",
      "title": "Request Size (Bytes/sec)",
      "targets": [
        {
          "expr": "sum(rate(http_request_size_bytes_sum[1m])) by (handler)",
          "legendFormat": "{{handler}}",
          "refId": "D"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": { "x": 12, "y": 8, "w": 12, "h": 8 }
    },
    {
      "type": "timeseries",
      "title": "Response Size (Bytes/sec)",
      "targets": [
        {
          "expr": "sum(rate(http_response_size_bytes_sum[1m])) by (handler)",
          "legendFormat": "{{handler}}",
          "refId": "E"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": { "x": 0, "y": 16, "w": 12, "h": 8 }
    },
    {
      "type": "timeseries",
      "title": "In-Flight Requests",
      "targets": [
        {
          "expr": "http_request_duration_seconds_count - ignoring(le) group_left sum(http_request_duration_seconds_bucket) by (handler)",
          "legendFormat": "{{handler}}",
          "refId": "F"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": { "x": 12, "y": 16, "w": 12, "h": 8 }
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "type": "dashboard",
        "name": "Annotations & Alerts",
        "enable": true
      }
    ]
  }
}
```

<br/>

**fastapi_prom_grafana_dashboard.json**

https://gist.github.com/gouravjshah/2dd5482c36bc9c2111e036fb70916249

```json
{
  "title": "FastAPI Prometheus Metrics Dashboard",
  "timezone": "browser",
  "refresh": "10s",
  "schemaVersion": 30,
  "version": 1,
  "panels": [
    {
      "type": "timeseries",
      "title": "Request Rate (Total)",
      "targets": [
        {
          "expr": "sum(rate(http_requests_total[1m])) by (handler)",
          "legendFormat": "{{handler}}",
          "refId": "A"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": {
        "x": 0,
        "y": 0,
        "w": 12,
        "h": 8
      }
    },
    {
      "type": "timeseries",
      "title": "Latency (95th Percentile)",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[1m])) by (le, handler))",
          "legendFormat": "{{handler}}",
          "refId": "A"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": {
        "x": 12,
        "y": 0,
        "w": 12,
        "h": 8
      }
    },
    {
      "type": "timeseries",
      "title": "Request Size (Bytes/sec)",
      "targets": [
        {
          "expr": "rate(http_request_size_bytes_sum[1m])",
          "legendFormat": "{{handler}}",
          "refId": "A"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": {
        "x": 0,
        "y": 8,
        "w": 12,
        "h": 8
      }
    },
    {
      "type": "timeseries",
      "title": "Response Size (Bytes/sec)",
      "targets": [
        {
          "expr": "rate(http_response_size_bytes_sum[1m])",
          "legendFormat": "{{handler}}",
          "refId": "A"
        }
      ],
      "datasource": "Prometheus",
      "gridPos": {
        "x": 12,
        "y": 8,
        "w": 12,
        "h": 8
      }
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "type": "dashboard",
        "name": "Annotations & Alerts",
        "enable": true
      }
    ]
  }
}
```

<br/>

```
// import grafana dashboard
http://localhost:30200/dashboard/import
```
