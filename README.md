# Тестовое задание для Флайдата

[Условие](#link_to_pdf)

## Установка и запуск

### С помощью docker-compose

Запускаются два контейнера - БД и приложение.

```commandline
git clone...
cd ....
```
Отредактировать .env
```commandline
source .env
docker-compose up
```

### В venv

Запускается только приложение

```commandline
git clone....
cd ...
pip install virtualenv
python3 -m virtualenv venv
source ./venv/bin/activate
export $(grep -v '^#' .env | xargs)
python3 main.py
```