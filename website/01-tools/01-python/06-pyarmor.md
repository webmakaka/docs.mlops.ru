---
layout: page
title: Pyarmor
description: Pyarmor
keywords: dev, tools, ubuntu, python, pyarmor
permalink: /tools/python/pyarmor/
---

# Pyarmor

<br/>

```
$ pip install pyarmor
```

<br/>

```
// OK!
$ pyarmor gen -O dist -r servicepy/
$ cd dist
$ mv pyarmor_runtime_000000/ ./servicepy/
$ python servicepy/run.py
```

<!-- <br/>

https://pyarmor.readthedocs.io/en/stable/tutorial/obfuscation.html

```
// FAIL!
$ pip install pyinstaller
```

<br/>

```
$ pyinstaller -F servicepy/run.py
$ ls dist/run
$ pyarmor gen -O obfdist --pack dist/run servicepy/run.py
$ cd dist
$ ./run
``` -->

<br/>

**Dockerfile**

```
FROM python:3.8-slim AS builder

RUN apt -o Acquire::Check-Valid-Until=false update && apt -o Acquire::Check-Valid-Until=false install -y procps gcc make curl wget vim net-tools iputils-ping python-is-python3 && apt clean
RUN python -m pip install --upgrade pip

WORKDIR /build

COPY ./servicepy/requirements-build.txt ./
RUN pip install -r ./requirements-build.txt

COPY ./servicepy ./servicepy

RUN pyarmor gen -O dist -r servicepy/
RUN mv ./dist/pyarmor_runtime_000000/ ./dist/servicepy/

# ----------------------------------------------------------------------

FROM python:3.8-slim

RUN apt -o Acquire::Check-Valid-Until=false update && apt -o Acquire::Check-Valid-Until=false install -y procps gcc make curl wget vim net-tools iputils-ping python-is-python3 && apt clean
RUN python -m pip install --upgrade pip

COPY ./servicestart /servicestart

WORKDIR /app

COPY ./servicepy/requirements.txt ./
RUN pip install -r ./requirements.txt

COPY --from=builder /build/dist ./

RUN adduser --system --no-create-home --disabled-login --group app && chown -R app:app /app && chown -R app:app /servicestart &&  chmod 744 /servicestart/service-start.sh

USER app

CMD ["/bin/sh", "/servicestart/service-start.sh"]
```

<br/>

**requirements-build.txt**

```
pyarmor==8.3.1
```

<br/>

**service-start.sh**

```
#!/bin/sh

cd /app/servicepy
python run.py
```
