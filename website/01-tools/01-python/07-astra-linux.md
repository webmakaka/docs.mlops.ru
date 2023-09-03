---
layout: page
title: Подготовка виртуального окружения для запуска python приложений в изолированной среде Astra Linux
description: Подготовка виртуального окружения для запуска python приложений в изолированной среде Astra Linux
keywords: dev, tools, python, virtualenv, astra
permalink: /tools/python/virtualenv/astra-linux/
---

# Подготовка виртуального окружения для запуска python приложений в изолированной среде Astra Linux

<br/>

```
// На astra linux требовались
# apt-get install -y patch make gcc zlib-devel libssl-devel


// WARNINGS при отсутствии
# apt-get install -y bzip2-devel ncurses-devel readline-devel liblzma-devel libsqlite3-devel


// Ошибка без этого пакета
// ModuleNotFoundError: No module named '_ctypes'
 # apt-get install -y libffi-devel
```
