---
layout: page
title: Camunda
description: Camunda
keywords: dev, tools, python, Camunda
permalink: /tools/camunda/
---

# Camunda

<br/>

https://www.youtube.com/watch?v=XSlSk8hBtVs&list=PLIGDNOJWiL1-bKGF5lSfRDL4sIkkNI9kg

<br/>

https://camunda.com/download/modeler/

<br/>

```
$ git clone git@github.com:tkssharma/Camunda-for-Beginners.git
$ cd Camunda-for-Beginners/
$ docker-compose up
```

<br/>

```
// demo / demo
http://localhost:8080/camunda/
```

```
// Deployment
// POST
$ curl \
    -F "files=@/tmp/diagram_deployment.bpmn" \
    --header "Content-Type: multipart/form-data" \
    --request POST \
    --url "http://localhost:8080/engine-rest/deployment/create" \
    | jq
```

<br/>

**response:**

```
{
  "links": [
    {
      "method": "GET",
      "href": "http://localhost:8080/engine-rest/deployment/48f1d6b0-f618-11ed-ac96-0242ac140003",
      "rel": "self"
    }
  ],
  "id": "48f1d6b0-f618-11ed-ac96-0242ac140003",
  "name": null,
  "source": null,
  "deploymentTime": "2023-05-19T07:39:28.181+0000",
  "tenantId": null,
  "deployedProcessDefinitions": {
    "deployment-test:1:48f38462-f618-11ed-ac96-0242ac140003": {
      "id": "deployment-test:1:48f38462-f618-11ed-ac96-0242ac140003",
      "key": "deployment-test",
      "category": "http://bpmn.io/schema/bpmn",
      "description": null,
      "name": null,
      "version": 1,
      "resource": "diagram_deployment.bpmn",
      "deploymentId": "48f1d6b0-f618-11ed-ac96-0242ac140003",
      "diagram": null,
      "suspended": false,
      "tenantId": null,
      "versionTag": null,
      "historyTimeToLive": 50,
      "startableInTasklist": true
    }
  },
  "deployedCaseDefinitions": null,
  "deployedDecisionDefinitions": null,
  "deployedDecisionRequirementsDefinitions": null
}
```

<br/>

```
// Start BPMN
// POST
$ curl \
    --data '{
      "task":"Quake 2"
      }' \
    --header "Content-Type: application/json" \
    --request POST \
    --url http://localhost:8080/engine-rest/process-definition/key/deployment-test/start \
    | jq
```

<br/>

**response:**

```
{
  "links": [
    {
      "method": "GET",
      "href": "http://localhost:8080/engine-rest/process-instance/926df123-f618-11ed-ac96-0242ac140003",
      "rel": "self"
    }
  ],
  "id": "926df123-f618-11ed-ac96-0242ac140003",
  "definitionId": "deployment-test:1:48f38462-f618-11ed-ac96-0242ac140003",
  "businessKey": null,
  "caseInstanceId": null,
  "ended": false,
  "suspended": false,
  "tenantId": null
}

```

<br/>

```
// Каким-то способом можно передать параметры
// JSON
{
  "variables": {
    "someData": {
      "value": "someValue",
      "type": "String"
    }
  },
  "businessKey": "12345"
}
```
