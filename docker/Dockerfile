# Используем базовый образ Python
FROM public.ecr.aws/docker/library/python:3.9

# Устанавливаем зависимости
WORKDIR /app
COPY ../requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Копируем исходный код приложения в образ
COPY .. /app

# Определяем переменные окружения для подключения к PostgreSQL
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=dbname
ENV POSTGRES_HOST=db

# Копируем и устанавливаем права на выполнение скрипта entrypoint
COPY ../entrypoint/entrypoint.sh /app/entrypoint/entrypoint.sh
RUN chmod +x /app/entrypoint/entrypoint.sh

# Консольная команда create_admin
RUN mv create_admin.py create_admin
RUN chmod +x /app/create_admin


# Устанавливаем entrypoint
#ENTRYPOINT ["/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint/entrypoint.sh"]

# Запускаем приложение
#CMD uvicorn main:app --host 0.0.0.0 --port 8080
#CMD ["python", "main.py"]