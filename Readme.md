# Исходники сайта [dlops.ru](https://dlops.ru)

Запустить dlops.ru на своем хосте с использованием docker контейнера:

    $ docker run -i -t -p 80:80 --name dlops.ru marley/dlops.ru

<br/>

### Как сервис

    # vi /etc/systemd/system/dlops.ru.service

вставить содержимое файла dlops.ru.service

    # systemctl enable dlops.ru.service
    # systemctl start  dlops.ru.service
    # systemctl status dlops.ru.service

http://localhost:4006

<br/>

### Вариант для внесения изменений

Инсталлируете docker и docker-compose, далее:

    $ cd ~
    $ mkdir -p dlops.ru && cd dlops.ru
    $ git clone --depth=1 https://github.com/webmakaka/dlops.ru.git .
    $ docker-compose up

<br/>

Остается в браузере подключиться к localhost:80
