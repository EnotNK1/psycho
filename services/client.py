from database.services.users import user_service_db
from database.services.client import client_service_db
from schemas.users import TaskId
from services.auth import verify_token
from fastapi import FastAPI, HTTPException
import uuid
from psycopg2 import Error
from utils.token_utils import check_token


class ClientService:

    def get_client(self, client_id: str, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 0 or role == 2 or role == 3:
            items = client_service_db.getClient(client_id)
            return items
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def get_list_client(self, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 0 or role == 2 or role == 3:
            items = client_service_db.getListClient(token_data['user_id'])
            return items
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def get_tasks(self, access_token):
        token_data = check_token(access_token)

        try:
            result = client_service_db.get_tasks_db(token_data['user_id'])
            if result != -1:
                return result
            else:
                return "error"
        except(Error):
            return "error"

    def get_given_tasks(self, access_token):
        token_data = check_token(access_token)

        try:
            role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
            if role == 0 or role == 2 or role == 3:
                result = client_service_db.get_given_tasks_db(token_data['user_id'])
                if result != -1:
                    return result
                else:
                    return "error"
            else:
                raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")
        except(Error):
            return "error"

    def complete_task(self, payload: TaskId, access_token):
        token_data = check_token(access_token)

        try:
            result = client_service_db.complete_task_db(token_data['user_id'], payload.task_id)
            if result != -1:
                if result == 1:
                    return "Successfully"
                else:
                    return "задача не того пользователя"
            else:
                return "error"
        except(Error):
            return "error"

    def delete_task(self, payload: TaskId, access_token):
        token_data = check_token(access_token)

        try:
            role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
            if role == 0 or role == 2 or role == 3:
                result = client_service_db.delete_task_db(payload.task_id)
                if result != -1:
                    if result == 1:
                        return "Successfully"
                    else:
                        return "Задача не найдена"
                else:
                    return "error"
            else:
                raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")
        except(Error):
            return "error"

    def delete_incorrect_tasks(self, access_token):
        token_data = check_token(access_token)

        try:
            role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
            if role == 0:
                result = client_service_db.delete_incorrect_tasks_db()
                if result != -1:
                    return "Successfully"
                else:
                    return "error"
            else:
                raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")
        except(Error):
            return "error"

    def unfulfilled_task(self, payload: TaskId, access_token):
        token_data = check_token(access_token)

        try:
            result = client_service_db.unfulfilled_task_db(token_data['user_id'], payload.task_id)
            if result != -1:
                if result == 1:
                    return "Successfully"
                else:
                    return "задача не того пользователя"
            else:
                return "error"
        except(Error):
            return "error"

    def get_your_psychologist(self, access_token):
        token_data = check_token(access_token)

        result = client_service_db.get_your_psychologist_db(token_data['user_id'])
        return result



client_service: ClientService = ClientService()