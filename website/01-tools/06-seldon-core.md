---
layout: page
title: Seldon Core
description: Seldon Core
keywords: dev, tools, python, Seldon Core
permalink: /tools/seldon-core/
---

# Seldon Core

<br/>

**Делаю:**  
2025.12.21

<br/>

**Minikube + MetalLB**

<br/>

https://www.youtube.com/watch?v=L746MuYzX1c

https://github.com/yinondn/seldon-core-tutorial/blob/main/quickstart.md

<br/>

```
$ kubectl create namespace seldon-system


$ helm install seldon-core seldon-core-operator \
    --repo https://storage.googleapis.com/seldon-charts \
    --set usageMetrics.enabled=true \
    --namespace seldon-system
```

<br/>

```
$ kubectl create namespace my-models
```

<br/>

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: machinelearning.seldon.io/v1
kind: SeldonDeployment
metadata:
  name: iris-model
  namespace: my-models
spec:
  name: iris
  predictors:
  - graph:
      implementation: SKLEARN_SERVER
      modelUri: gs://seldon-models/v1.10.0-dev/sklearn/iris
      name: classifier
    name: default
    replicas: 1
EOF
```

<br/>

```yaml
$ cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: seldon-8080
  namespace: my-models
spec:
  selector:
    app: iris-model-default-0-classifier
  ports:
    - port: 8080
      targetPort: 9000
  type: LoadBalancer
EOF
```

<br/>

```
$ kubectl get sdep iris-model -o json --namespace my-models | jq .status
```

<br/>

```json
{
  "address": {
    "url": "http://iris-model-default.my-models.svc.cluster.local:8000/api/v1.0/predictions"
  },
  "conditions": [
    {
      "lastTransitionTime": "2025-12-21T00:40:19Z",
      "reason": "No Ambassador Mappaings defined",
      "status": "True",
      "type": "AmbassadorMappingsReady"
    },
    {
      "lastTransitionTime": "2025-12-21T00:40:19Z",
      "message": "Deployment has minimum availability.",
      "reason": "MinimumReplicasAvailable",
      "status": "True",
      "type": "DeploymentsReady"
    },
    {
      "lastTransitionTime": "2025-12-21T00:38:16Z",
      "reason": "No HPAs defined",
      "status": "True",
      "type": "HpasReady"
    },
    {
      "lastTransitionTime": "2025-12-21T00:38:16Z",
      "reason": "No KEDA resources defined",
      "status": "True",
      "type": "KedaReady"
    },
    {
      "lastTransitionTime": "2025-12-21T00:38:16Z",
      "reason": "No PDBs defined",
      "status": "True",
      "type": "PdbsReady"
    },
    {
      "lastTransitionTime": "2025-12-21T00:40:19Z",
      "status": "True",
      "type": "Ready"
    },
    {
      "lastTransitionTime": "2025-12-21T00:40:19Z",
      "reason": "All services created",
      "status": "True",
      "type": "ServicesReady"
    },
    {
      "lastTransitionTime": "2025-12-21T00:40:19Z",
      "reason": "No VirtualServices defined",
      "status": "True",
      "type": "istioVirtualServicesReady"
    }
  ],
  "deploymentStatus": {
    "iris-model-default-0-classifier": {
      "availableReplicas": 1,
      "replicas": 1
    }
  },
  "replicas": 1,
  "serviceStatus": {
    "iris-model-default": {
      "grpcEndpoint": "iris-model-default.my-models:5001",
      "httpEndpoint": "iris-model-default.my-models:8000",
      "svcName": "iris-model-default"
    },
    "iris-model-default-classifier": {
      "grpcEndpoint": "iris-model-default-classifier.my-models:9500",
      "httpEndpoint": "iris-model-default-classifier.my-models:9000",
      "svcName": "iris-model-default-classifier"
    }
  },
  "state": "Available"
}
```

<br/>

```
$ kubectl get svc seldon-8080 -n my-models
NAME          TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)          AGE
seldon-8080   LoadBalancer   10.108.124.126   192.168.49.21   8080:30128/TCP   12m
```

<br/>

```
$ curl -X POST http://192.168.49.21:8080/api/v1.0/predictions \
  -H 'Content-Type: application/json' \
  -d '{"data": {
          "names": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
          "ndarray": [[5.1, 3.5, 1.4, 0.2]]}}' \
  | jq
```

<br/>

```json
{
  "data": {
    "names": ["t:0", "t:1", "t:2"],
    "ndarray": [
      [0.8780303050242675, 0.12195890005077532, 1.0794924957147728e-5]
    ]
  },
  "meta": {
    "requestPath": {
      "classifier": "seldonio/sklearnserver:1.17.1"
    }
  }
}
```
