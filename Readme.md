# Исходники сайта [aiops.ru](https://aiops.ru)

Запустить aiops.ru на своем хосте с использованием docker контейнера:

    $ docker run -i -t -p 80:80 --name aiops.ru marley/aiops.ru

<br/>

### Как сервис

    # vi /etc/systemd/system/aiops.ru.service

вставить содержимое файла aiops.ru.service

    # systemctl enable aiops.ru.service
    # systemctl start  aiops.ru.service
    # systemctl status aiops.ru.service

http://localhost:4006

<br/>

### Вариант для внесения изменений

Инсталлируете docker и docker-compose, далее:

    $ cd ~
    $ mkdir -p aiops.ru && cd aiops.ru
    $ git clone --depth=1 https://github.com/webmakaka/aiops.ru.git .
    $ docker-compose up

<br/>

Остается в браузере подключиться к localhost:80
