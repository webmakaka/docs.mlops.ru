# Исходники сайта [mlops.ru](https://mlops.ru)

Запустить mlops.ru на своем хосте с использованием docker контейнера:

    $ docker run -i -t -p 80:80 --name mlops.ru marley/mlops.ru

<br/>

### Как сервис

    # vi /etc/systemd/system/mlops.ru.service

вставить содержимое файла mlops.ru.service

    # systemctl enable mlops.ru.service
    # systemctl start  mlops.ru.service
    # systemctl status mlops.ru.service

http://localhost:4006

<br/>

### Вариант для внесения изменений

Инсталлируете docker и docker-compose, далее:

    $ cd ~
    $ mkdir -p mlops.ru && cd mlops.ru
    $ git clone --depth=1 https://github.com/webmakaka/mlops.ru.git .
    $ docker-compose up

<br/>

Остается в браузере подключиться к localhost:80
