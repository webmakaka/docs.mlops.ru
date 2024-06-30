---
layout: page
title: Установка MinIO
description: Установка MinIO
keywords: tools, minio
permalink: /tools/minio/
---

# Установка MinIO с помощью docker compose

<br/>

Делаю:  
2024.06.30

<br/>

**YouTube:**  
https://www.youtube.com/watch?v=tRlEctAwkk8

**Git:**  
https://github.com/minio/minio/tree/master/docs/orchestration/docker-compose

<br/>

```
$ mkdir -p ~/projects/dev/db/minio
$ cd ~/projects/dev/db/minio
```

<br/>

```
// Пофик, что качаю весь проект
// Потом переделаю
$ git clone git@github.com:minio/minio.git
$ cd minio/docs/orchestration/docker-compose/
```

```
$ docker-compose pull
$ docker-compose up
```

```
// minioadmin / minioadmin
http://127.0.0.1:9001/login
```
