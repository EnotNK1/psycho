#!/bin/bash
set -e

# Настройка PYTHONPATH
export PYTHONPATH=/app

# Запуск приложения
uvicorn main:app --host 0.0.0.0 --port 8080 &

sleep 5

# Выполнение миграций базы данных (если необходимо)
alembic upgrade head

# Выполнение дополнительного кода
python /app/entrypoint/entrypoint.py

# Ожидание завершения uvicorn
wait