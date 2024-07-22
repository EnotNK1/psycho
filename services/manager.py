from database.database import database_service
from schemas.users import Manager, GiveTask
import uuid
from psycopg2 import Error
from utils.token_utils import check_token
from fastapi import HTTPException

class ManagerService:

    def manager_send(self, payload: Manager, access_token):
        token_data = check_token(access_token)

        try:
            result = database_service.manager_send_db(token_data['user_id'], payload.username,
                                                      payload.description,
                                                      payload.city, payload.company, payload.online, payload.gender,
                                                      payload.birth_date)
            if result != -1:
                return "Successfully"
            else:
                return "error"
        except(Error):
            return "error"

    def give_task(self, payload: GiveTask, access_token):
        token_data = check_token(access_token)

        try:
            role = database_service.check_role(token_data['user_id'])
            if role == 2 or role == 3 or role == 0:
                result = database_service.give_task_db(token_data['user_id'], payload.text,
                                                          payload.test_title,
                                                          payload.test_id, payload.user_id)
                if result == -2:
                    raise HTTPException(status_code=404, detail="Пользователя с такими данными не найдено!")
                if result == -3:
                    raise HTTPException(status_code=404, detail="Тест с такими данными не найден!")
                elif result != -1:
                    return "Successfully"
                else:
                    return "error"
            else:
                return "access denied"
        except(Error):
            return "error"

    def get_all_manager(self, access_token):
        token_data = check_token(access_token)

        items = database_service.get_all_manager_db()
        return items



manager_service: ManagerService = ManagerService()
