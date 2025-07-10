# Используем официальный slim-образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем необходимые системные зависимости
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install poetry

# Копируем только файл pyproject.toml
COPY pyproject.toml .

# Настраиваем Poetry и устанавливаем зависимости
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# Копируем исходный код приложения в контейнер
COPY . .

# Устанавливаем переменную окружения для Python
ENV PYTHONUNBUFFERED=1

# Пробрасываем порт, который будет использовать Django
EXPOSE 8000

# Добавляем команду запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
