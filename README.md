#  Pulses orchestra

**pulsorch**

## Стек технологий

- **[Flask](https://flask.palletsprojects.com/)** — для создания веб-приложений.
- **[SQLAlchemy](https://www.sqlalchemy.org/)** — для работы с базой данных.
- **[Alembic](https://alembic.sqlalchemy.org/)** — для миграций базы данных.
- **[PostgreSQL](https://www.postgresql.org/)** — для хранения данных.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — для работы с переменными окружения.
- **[Pydantic](https://docs.pydantic.dev/latest/)** — для валидации и сериализации данных.
- **[mypy](http://mypy-lang.org/)** — для статического анализа типов.
- **[ruff](https://github.com/charliermarsh/ruff)** — для линтинга кода.
- **[pytest](https://pytest.org/)** — для написания тестов.

## Установка

Для начала работы с проектом нужно создать виртуальное окружение и установить зависимости.

1. **Создание виртуального окружения**:

    ```bash
    uv venv
    ```

2. **Активировать виртуальное окружение**:

    - Для **Windows (Git Bash)**:
      ```bash
      .venv/Scripts/activate
      ```

    - Для **macOS/Linux**:
      ```bash
      source .venv/bin/activate
      ```

3. **Установка зависимостей**:

    В виртуальном окружении установим все необходимые пакеты:

    ```bash
    uv lock
    uv sync --all-extras
    ```

    Это установит все зависимости, включая библиотеки для разработки, такие как `flake8`, `pytest`, и другие.

4. **Настройка Alembic**:

    Чтобы управлять миграциями базы данных, выполните следующие шаги:

    - Инициализируйте Alembic:

      ```bash
      alembic init alembic
      ```

    - Настройте строку подключения в `alembic.ini`:

       ```python
       from pulsorch.config import get_db_url
       config.set_main_option("sqlalchemy.url", get_db_url())
       ```

    - Создайте миграцию с помощью команды:

      ```bash
      alembic revision --autogenerate -m "Initial migration"
      ```

    - Примените миграцию:

      ```bash
      alembic upgrade head
      ```

## Управление Docker

### Базовые команды

```bash
# Запуск всех сервисов в фоновом режиме
docker compose up -d

# Запуск только сервиса БД
docker compose up -d db

# Остановка всех сервисов с таймаутом 1 сек
docker compose stop -t1

# Остановка и удаление контейнеров/сетей
docker compose down -t1

# Просмотр статуса контейнеров
docker compose ps

# Просмотр логов БД (последние 100 строк)
docker compose logs --tail 100 -f db

# Обновить образы
docker compose pull

# Сборка с кэшем
docker compose build

# Полная пересборка
docker compose build --no-cache

# Удалить всё (контейнеры, образы, volumes)
docker system prune -af --volumes

# Live-режим разработки
docker compose up -d db && docker compose up app

# Вход в контейнер
docker compose exec app bash

# Применить миграции
docker compose exec app alembic upgrade head

# Полная пересборка
docker compose down -v
docker compose build
docker compose up -d

# Проверка логов
docker compose logs -f api

