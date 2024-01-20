---
layout: page
title: Apache Kafka for Python Developers
description: Apache Kafka for Python Developers
keywords: dev, tools, python, kafka
permalink: /tools/python/kafka/
---

# Apache Kafka for Python Developers

<br/>

https://www.youtube.com/playlist?list=PLjfRmoYoxpNrs0VmIq6mOTqXP52RfZdRf

<br/>

### Install and run Apache Kafka & integration with Python using Kafka-Python

<br/>

```
$ pip install kafka-python
```

<br/>

**main.py**

<br/>

```python
from time import sleep
from json import dumps
from kafka import KafkaProducer

topic_name='hello_world'
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'number' : e}
    print(data)
    producer.send(topic_name, value=data)
    sleep(5)
```

<br/>

```
// С первого раза (наверное) будет ошибка
$ python main.py
```

<br/>

### Multiple Producer & Multiple Consumer in a Kafka Topic

<br/>

### Broker Cluster and Zookeeper in Kafka

<br/>

### Topics, partitions, and offsets in Kafka

<br/>

### Kafka Cluster with Multiple Brokers

<br/>

### Topic with Replication in Multiple Broker Kafka Cluster
