# Исходники сайта [docs.mlops.ru](https://docs.mlops.ru)

Запустить docs.mlops.ru на своем хосте с использованием docker контейнера:

    $ docker run -i -t -p 80:80 --name docs.mlops.ru marley/docs.mlops.ru

<br/>

### Как сервис

    # vi /etc/systemd/system/docs.mlops.ru.service

вставить содержимое файла docs.mlops.ru.service

    # systemctl enable docs.mlops.ru.service
    # systemctl start  docs.mlops.ru.service
    # systemctl status docs.mlops.ru.service

http://localhost:4006

<br/>

### Вариант для внесения изменений

Инсталлируете docker и docker-compose, далее:

    $ cd ~
    $ mkdir -p docs.mlops.ru && cd docs.mlops.ru
    $ git clone --depth=1 https://github.com/webmakaka/docs.mlops.ru.git .
    $ docker-compose up

<br/>

Остается в браузере подключиться к localhost:80
