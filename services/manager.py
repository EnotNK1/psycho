from database.database import database_service
from schemas.users import Manager, GiveTask
from services.auth import verify_token
import uuid
from psycopg2 import Error


class ManagerService:

    def manager_send(self, payload: Manager, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

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
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            role = database_service.check_role(token_data['user_id'])
            if role == 2 or role == 3 or role == 0:
                result = database_service.give_task_db(token_data['user_id'], payload.text,
                                                          payload.test_title,
                                                          payload.test_id, payload.user_id)
                if result != -1:
                    return "Successfully"
                else:
                    return "error"
            else:
                return "access denied"
        except(Error):
            return "error"



manager_service: ManagerService = ManagerService()
