# Тестовое задание для Флайдата

### [Условие](docs/test_python_postgres.pdf)

Выполнено на fastapi и postgresql

Проверить API можно с помощью swagger (http://{{address}}:{{port}}/docs/)

## Установка и запуск

### С помощью docker-compose

Запускаются два контейнера - БД и приложение.

1. Скачать репозиторий 

```commandline
git clone https://github.com/mikepro-alfamail-ru/flydata.git
cd flydata
```

2. Отредактировать .env - внести свои параметры.

```commandline
vi .env
```

3. Запустить docker-compose

```commandline
export $(grep -v '^#' .env | xargs)
docker-compose up
```

### В venv

Запускается только приложение

```commandline
git clone https://github.com/mikepro-alfamail-ru/flydata.git
cd flydata
pip install virtualenv
python3 -m virtualenv venv
source ./venv/bin/activate
#
# vi .env
# (if needed)
#
export $(grep -v '^#' .env | xargs)
python3 main.py
```
