---
layout: page
title: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - Autoscaling a ML Model
description: DevOps to MLOps Bootcamp - Build & Deploy ML Systems End-to-End - Autoscaling a ML Model
keywords: courses, devops to mlops bootcamp, Autoscaling a ML Model
permalink: /courses/mlops/ultimate-devops-to-mlops-bootcamp/autoscaling-a-ml-model/
---

# [Course][Udemy][Gourav Shah] Ultimate DevOps to MLOps Bootcamp - Build ML CI-CD Pipelines [ENG, 2025] : 09. Autoscaling a ML Model

<br/>

**Делаю:**  
2025.12.30

<br/>

https://keda.sh/

<br/>

```
$ helm repo add kedacore https://kedacore.github.io/charts
$ helm repo update
```

<br/>

```
$ helm install keda kedacore/keda \
  --namespace keda \
  --create-namespace
```

<br/>

```
$ kubectl get pods -n keda
NAME                                               READY   STATUS    RESTARTS        AGE
keda-admission-webhooks-66d8d7cf95-kvbnz           1/1     Running   0               2m32s
keda-operator-7d6d994857-wzsr7                     1/1     Running   1 (2m17s ago)   2m32s
keda-operator-metrics-apiserver-6fd7b6694f-8s52h   1/1     Running   0               2m32s
```

<br/>

**Задаем ресурсы:**

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: model
  labels:
    app: model
spec:
  replicas: 1
  selector:
    matchLabels:
      app: model
  template:
    metadata:
      labels:
        app: model
    spec:
      containers:
      - image: webmakaka/house-price-model:latest
        name: house-price-model
        ports:
        - containerPort: 8000
        resources:
          requests:
            cpu: "50m"
            memory: "64Mi"
          limits:
            cpu: "100m"
            memory: "128Mi"
EOF
```

<br/>

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: fastapi-latency-autoscaler
  namespace: default
spec:
  scaleTargetRef:
    name: model
  minReplicaCount: 1
  maxReplicaCount: 5
  pollingInterval: 30
  cooldownPeriod: 300
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://prom-kube-prometheus-stack-prometheus.monitoring.svc:9090
      metricName: fastapi_latency_p95
      query: |
        histogram_quantile(0.95,
          sum(rate(http_request_duration_seconds_bucket[1m])) by (le))
      threshold: "0.5"
EOF
```

<br/>

```
$ kubectl get scaledobject
NAME                         SCALETARGETKIND      SCALETARGETNAME   MIN   MAX   READY   ACTIVE   FALLBACK   PAUSED   TRIGGERS     AUTHENTICATIONS   AGE
fastapi-latency-autoscaler   apps/v1.Deployment   model             1     5     True    True     False      False    prometheus                     8m27s
```

<br/>

```
$ kubectl get hpa
NAME                                  REFERENCE          TARGETS          MINPODS   MAXPODS   REPLICAS   AGE
keda-hpa-fastapi-latency-autoscaler   Deployment/model   94m/500m (avg)   1         5         1          43s
```

<br/>

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: fastapi-latency-autoscaler
  namespace: default
spec:
  scaleTargetRef:
    name: model
  minReplicaCount: 1
  maxReplicaCount: 5
  pollingInterval: 30
  cooldownPeriod: 300
  triggers:

  - type: prometheus
    metadata:
      serverAddress: http://prom-kube-prometheus-stack-prometheus.monitoring.svc:9090
      metricName: fastapi_latency_p95
      query: |
        histogram_quantile(0.95,
          sum(rate(http_request_duration_seconds_bucket[1m])) by (le))
      threshold: "0.5"

  - type: prometheus
    metadata:
      serverAddress: http://prom-kube-prometheus-stack-prometheus.monitoring.svc:9090
      metricName: request_rate
      query: sum(rate(http_requests_total[1m]))
      threshold: "1000"
EOF
```

<br/>

```
$ kubectl get hpa
NAME                                  REFERENCE          TARGETS                        MINPODS   MAXPODS   REPLICAS   AGE
keda-hpa-fastapi-latency-autoscaler   Deployment/model   94m/500m (avg), 66m/1k (avg)   1         5         1          16m
```

<br/>

```
$ kubectl logs -n keda deploy/keda-operator
```

<br/>

```
$ kubectl logs -n keda deploy/keda-operator
```

<br/>

### Нагружаем

```
$ sudo snap install hey
```

<br/>

```
// OK!
$ curl -X POST http://localhost:30100/predict -H "Content-Type: application/json" -d '{"sqft":4500,"bedrooms":4,"bathrooms":2,"year_built":2014,"condition":"Good","location":"Urban"}' | jq
```

<br/>

```json
{
  "predicted_price": 819093.18,
  "confidence_interval": [737183.86, 901002.5],
  "features_importance": {},
  "prediction_time": "2025-12-30T13:46:19.759867"
}
```

<!-- <br/>

```
// OK!
$ hey -n 5000 -c 200 -m POST \
  -H "Content-Type: application/json" \
  -d predict.json \
  http://localhost:30100/predict
``` -->

<br/>

```
$ hey -n 5000 -c 200 -m POST -H "Content-Type: application/json" \
  -d '{"sqft":4500,"bedrooms":4,"bathrooms":2,"year_built":2014,"condition":"Good","location":"Urban"}' \
  http://localhost:30100/predict
```

<!-- <br/>

```
// 3 минуты
// OK!
$ hey -z 3m -c 200 -m POST \
-H "Content-Type: application/json" \
-d predict.json \
http://localhost:30100/predict
``` -->

<br/>

```
// 3 минуты
// OK!
$ hey -z 3m -c 200 -m POST \
-H "Content-Type: application/json" \
-d '{"sqft":4500,"bedrooms":4,"bathrooms":2,"year_built":2014,"condition":"Good","location":"Urban"}' \
http://localhost:30100/predict
```

<br/>

### Не заработало!

Решили использовать другой порт для мониторинга

<br/>

**src/api/main.py**

<br/>

```
import threading
```

<br/>

После:

```
# Initialize and instrument Prometheus metrics
Instrumentator().instrument(app).expose(app)
```

<br/>

Добавляем

<br/>

```
# Start Prometheus metrics server on port 9100 in a background thread
def start_metrics_server():
    start_http_server(9100)

threading.Thread(target=start_metrics_server, daemon=True).start()
```

<br/>

**Dockerfile**

<br/>

```
EXPOSE 8000
```

<br/>

Меняем на:

```
EXPOSE 8000 9100
```

<br/>

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    app: model
  name: model
spec:
  ports:
    - name: web
      nodePort: 30100
      port: 8000
      protocol: TCP
      targetPort: 8000
    - name: metrics
      port: 9100
      protocol: TCP
      targetPort: 9100
  selector:
    app: model
  type: NodePort
status:
  loadBalancer: {}
EOF
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
    - port: metrics
      path: /
      interval: 15s
      scrapeTimeout: 10s
EOF
```

<br/>

**Уменьшаем значения параметров threshold**

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: fastapi-latency-autoscaler
  namespace: default
spec:
  scaleTargetRef:
    name: model
  minReplicaCount: 1
  maxReplicaCount: 5
  pollingInterval: 30
  cooldownPeriod: 300
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://prom-kube-prometheus-stack-prometheus.monitoring.svc:9090
      metricName: fastapi_latency_p95
      query: |
        histogram_quantile(0.95,
          sum(rate(http_request_duration_seconds_bucket[1m])) by (le))
      threshold: "0.08"

  - type: prometheus
    metadata:
      serverAddress: http://prom-kube-prometheus-stack-prometheus.monitoring.svc:9090
      metricName: request_rate
      query: sum(rate(http_requests_total[1m]))
      threshold: "20"
EOF
```

<br/>

```
// 3 минуты
// OK!
$ hey -z 3m -c 200 -m POST \
-H "Content-Type: application/json" \
-d '{"sqft":4500,"bedrooms":4,"bathrooms":2,"year_built":2014,"condition":"Good","location":"Urban"}' \
http://localhost:30100/predict
```

<br/>

```
$ kubectl get hpa
NAME                                  REFERENCE          TARGETS                   MINPODS   MAXPODS   REPLICAS   AGE
keda-hpa-fastapi-latency-autoscaler   Deployment/model   0/80m (avg), 0/20 (avg)   1         5         1          147m
```

<br/>

Все равно у меня не заработало!
Метрики не существуют в Prometheus

```
$ curl "http://localhost:30300/api/v1/query?query=http_requests_total"
$ curl "http://localhost:30300/api/v1/query?query=http_request_duration_seconds_bucket"
```

Метрики не найдены в Prometheus. Это означает, что:

Либо FastAPI не экспортирует метрики с этими именами

Либо Prometheus не настроен на сбор метрик с вашего приложения

<br/>

### CPU Based Auto Scaling with KEDA

<br/>

```
$ cd ~/tmp
$ git clone https://github.com/schoolofdevops/metrics-server.git
$ kubectl apply -k metrics-server/manifests/overlays/release
```

<br/>

```
$ kubectl top pods
$ kubectl top nodes
```

<br/>

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: fastapi-latency-autoscaler
  namespace: default
spec:
  scaleTargetRef:
    name: model
  minReplicaCount: 1
  maxReplicaCount: 5
  pollingInterval: 30
  cooldownPeriod: 300
  triggers:

  - type: prometheus
    metadata:
      serverAddress: http://prom-kube-prometheus-stack-prometheus.monitoring.svc:9090
      metricName: fastapi_latency_p95
      query: |
        histogram_quantile(0.95,
          sum(rate(http_request_duration_seconds_bucket[1m])) by (le))
      threshold: "0.1"

  - type: cpu
    metricType: Utilization
    metadata:
      value: "50"

EOF
```

<br/>

```
$ kubectl get hpa
NAME                                  REFERENCE          TARGETS                    MINPODS   MAXPODS   REPLICAS   AGE
keda-hpa-fastapi-latency-autoscaler   Deployment/model   0/80m (avg), cpu: 4%/50%   1         5         1          3h3m
```

<br/>

```
// 3 минуты
// OK!
$ hey -z 3m -c 200 -m POST \
-H "Content-Type: application/json" \
-d '{"sqft":4500,"bedrooms":4,"bathrooms":2,"year_built":2014,"condition":"Good","location":"Urban"}' \
http://localhost:30100/predict
```

<br/>

```
$ kubectl get hpa
NAME                                  REFERENCE          TARGETS                       MINPODS   MAXPODS   REPLICAS   AGE
keda-hpa-fastapi-latency-autoscaler   Deployment/model   0/100m (avg), cpu: 140%/50%   1         5         1          3h6m
```

<br/>

```
$ kubectl get pods
NAME                        READY   STATUS              RESTARTS   AGE
model-86cd7ffd9f-2w4ct      0/1     ContainerCreating   0          26s
model-86cd7ffd9f-5qhm4      1/1     Running             0          41s
model-86cd7ffd9f-j6nhp      1/1     Running             0          42m
model-86cd7ffd9f-p7m4x      0/1     ContainerCreating   0          41s
model-86cd7ffd9f-rgxts      1/1     Running             0          26s
streamlit-94fb5b648-pm8gl   1/1     Running             0          5h41m
```

<br/>

### Using VerticlePodAutoscaler

<br/>

```
$ cd ~/tmp
$ git clone https://github.com/kubernetes/autoscaler.git
$ cd autoscaler/vertical-pod-autoscaler/
```

<br/>

```
$ ./hack/vpa-up.sh
```

<br/>

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: model
  labels:
    role: model
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: model
  updatePolicy:
    updateMode: Auto
  resourcePolicy:
    containerPolicies:
    - containerName: '*'
      minAllowed:
        cpu: 50m
        memory: 64Mi
      maxAllowed:
        cpu: 500m
        memory: 512Mi
      controlledResources:
      - cpu
      - memory
EOF
```

<br/>

```
$ kubectl get vpa model --watch
NAME    MODE   CPU   MEM     PROVIDED   AGE
model   Auto   50m   250Mi   True       53s
```

<br/>

```
$ hey -z 3m -c 200 -m POST \
-H "Content-Type: application/json" \
-d '{"sqft":4500,"bedrooms":4,"bathrooms":2,"year_built":2014,"condition":"Good","location":"Urban"}' \
http://localhost:30100/predict
```

<br/>

```
$ kubectl get pods
NAME                        READY   STATUS    RESTARTS   AGE
model-86cd7ffd9f-2g8wd      1/1     Running   0          22s
model-86cd7ffd9f-92lxp      1/1     Running   0          7s
model-86cd7ffd9f-fczwz      1/1     Running   0          7s
model-86cd7ffd9f-m8nbc      1/1     Running   0          22s
model-86cd7ffd9f-p7m4x      1/1     Running   0          24m
streamlit-94fb5b648-pm8gl   1/1     Running   0          6h4m
```
