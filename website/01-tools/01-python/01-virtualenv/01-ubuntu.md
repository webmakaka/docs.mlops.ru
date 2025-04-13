---
layout: page
title: Подготовка виртуального окружения для запуска python приложений в изолированной среде в Ubuntu 22.04 LTS
description: Подготовка виртуального окружения для запуска python приложений в изолированной среде в Ubuntu 22.04 LTS
keywords: dev, tools, python, virtualenv, ubuntu
permalink: /tools/python/virtualenv/ubuntu/
---

# Подготовка виртуального окружения для запуска python приложений в изолированной среде в Ubuntu 22.04 LTS

<br/>

Делаю:  
2023.01.20

<br/>

```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.3 LTS
Release:	22.04
Codename:	jammy
```

<br/>

### Устанавливаю pyenv (Используется, когда нужна специфическая минорная версия python)

<br/>

```
$ sudo apt update && sudo apt upgrade -y

// python3 будет по умолчанию называться python
$ sudo apt install python-is-python3
```

<br/>

```
// На ubuntu
$ sudo apt install -y build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev tk-dev
```

<br/>

```
// В книге Building Data Science Applications with FastAPI рекомендуют
$ sudo apt update; sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

<br/>

```
$ curl https://pyenv.run | bash
```

<br/>

```
$ vi ~/.bashrc
```

```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

<br/>

logout / login

<br/>

```
$ echo ${PYENV_ROOT}
```

Возвращает:

```
/home/marley/.pyenv
```

<br/>

```
$ pyenv install --list | grep python

$ export PYTHON_VERSION=3.8.12

$ pyenv install ${PYTHON_VERSION}

// установить по умолчанию
$ pyenv global ${PYTHON_VERSION}
```

<br/>

```
// Проверка
$ ~/.pyenv/versions/${PYTHON_VERSION}/bin/python --version
Python 3.8.12
```

<br/>

### Создание проекта под окружение

```
$ export PROJECT_NAME=<MY_NEW_PROJECT_NAME>

$ pyenv virtualenv ${PYTHON_VERSION} ${PROJECT_NAME}-env

$ source ${PYENV_ROOT}/versions/${PROJECT_NAME}-env/bin/activate

$ mkdir -p  ~/projects/dev/python/${PROJECT_NAME}
$ cd ~/projects/dev/python/${PROJECT_NAME}
```

<br/>

```
$ {
  pip install pip --upgrade
  pip install setuptools --upgrade
}
```

<br/>

```
// Посмотреть список установленных пакетов
// $ pip list -v
```

<br/>

```
$ python --version
$ pip --version
```
