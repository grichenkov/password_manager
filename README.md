# Password Manager

Менеджер паролей с API для безопасного хранения паролей, привязанных к имени сервиса.

## Используемый стек

Python 3.11     
FastAPI  
SQLAlchemy  
Pydantic    
PostgreSQL  
Alembic (миграции)  
Docker + Docker Compose 
Pytest (тестирование)   
Black, Flake8, MyPy (линтеры и форматтеры)

## Настройка переменных окружения
Перед запуском нужно создать файл .env (на основе example.env)

# Запуск через Docker

Запустить проект можно с помощью docker-compose:

```bash
docker-compose up -d --build
```
Флаг --build нужен при первом запуске или при изменении зависимостей.


### После запуска API будет доступен по адресу: http://localhost:8000


## Остановка контейнеров

```bash
docker-compose down
```

## Работа с миграциями
Перед запуском проекта примените все миграции:
```bash
docker exec -it password_manager_app alembic upgrade head
```

Если нужно откатить последнюю миграцию:
```bash
docker exec -it password_manager_app alembic downgrade -1
```

## API
После запуска документация API будет доступна:  
Swagger UI: http://localhost:8000/docs  
ReDoc: http://localhost:8000/redoc

# Локальный запуск без Docker

Создай виртуальное окружение:
```bash
python -m venv venv
```

Активируй виртуальное окружение:
```bash
source venv/bin/activate
```

Установи poetry:
```bash
pip install poetry
```

Установи зависимости проекта:
```bash
poetry install
```

Создать или ззапустить базу на локали и настроить её под .env.example, не забыть поставить в хосте localhost

## Применение миграций (Alembic)
Применить миграции:
```bash
alembic upgrade head
```

Откатить последнюю миграцию:
```bash
alembic downgrade -1
```

##  Запуск проекта

```bash
poetry run password-manager
```

Swagger доступен по адресу:
```bash
http://127.0.0.1:8000/docs
```

# Запуск линтеров с помощью Makefile
Flake8
```bash
make lint
```
MyPy
```bash
make mypy
```
Black
```bash
make format
```