from database.services.daily_task import daily_task_service_db
from psycopg2 import Error
from utils.token_utils import check_token
from schemas.daily_tasks import DailyTaskId
from fastapi import HTTPException
import uuid


class DailyTaskService:

    def get_daily_tasks(self, access_token):
        token_data = check_token(access_token)

        try:
            result = daily_task_service_db.get_daily_tasks(token_data["user_id"])
            return result
        except(Error):
            return "error"

    def complete_daily_tasks(self, payload: DailyTaskId, access_token):
        token_data = check_token(access_token)

        try:
            result = daily_task_service_db.complete_daily_task(payload.daily_task_id)
            if result == 0:
                return {"status": "OK"}
            else:
                raise HTTPException(status_code=404, detail="Ежедневное задание не найдено!")
        except(Error):
            return "error"

    def change_daily_tasks(self):

        daily_task_service_db.set_daily_tasks()


daily_task_service: DailyTaskService = DailyTaskService()