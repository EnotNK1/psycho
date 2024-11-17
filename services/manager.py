from database.services.users import user_service_db
from database.services.manager import manager_service_db
from schemas.users import Manager, GiveTask, GiveTaskAllClient, GiveTaskListClient
import uuid
from psycopg2 import Error
from utils.token_utils import check_token
from fastapi import HTTPException

class ManagerService:

    def manager_send(self, payload: Manager, access_token):
        token_data = check_token(access_token)

        try:
            result = manager_service_db.manager_send_db(token_data['user_id'], payload.username,
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
            role = user_service_db.check_role(token_data['user_id'])
            if role == 2 or role == 3 or role == 0:
                result = manager_service_db.give_task_db(token_data['user_id'], payload.text,
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

        items = manager_service_db.get_all_manager_db()
        return items




    def give_task_all_client(self, payload: GiveTaskAllClient, access_token):
        token_data = check_token(access_token)
        try:
            role = user_service_db.check_role(token_data['user_id'])
            if role == 3 or role == 0:
                result = manager_service_db.give_task_all_client(token_data['user_id'], payload.test_id,
                                                                 payload.text)

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

    def give_task_list_client(self, payload: GiveTaskListClient, access_token):
        token_data = check_token(access_token)
        try:
            role = user_service_db.check_role(token_data['user_id'])
            if role == 3 or role == 0:
                result = manager_service_db.give_task_list_client(token_data['user_id'], payload.test_id,
                                                                 payload.text, payload.list_client)

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

        items = manager_service_db.get_all_manager_db()
        return items

manager_service: ManagerService = ManagerService()
