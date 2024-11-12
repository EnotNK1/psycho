from celery.schedules import crontab
from database.services.daily_task import daily_task_service_db

from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://redis:6379",
    include=["tasks.tasks"]
)
celery_app.conf.timezone = 'Europe/Moscow'

@celery_app.task
def my_scheduled_function():
    daily_task_service_db.set_daily_tasks()


@celery_app.on_after_configure.connect
def setup_periodic_task(sender, **kwargs):
    sender.add_periodic_task(crontab(hour='20', minute='0'), my_scheduled_function.s())