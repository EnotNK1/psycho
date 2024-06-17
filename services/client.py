from database.database import database_service
from schemas.users import GetClient
from services.auth import verify_token
from fastapi import FastAPI, HTTPException
import uuid
from psycopg2 import Error



class ClientService:

    def get_client(self, payload: GetClient, access_token):
        if not access_token:
            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 0 or role == 2:
            items = database_service.getClient(payload.user_id)
            return items
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def get_list_client(self, access_token):
        if not access_token:
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 0 or role == 2:
            items = database_service.getListClient(token_data['user_id'])
            return items
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def get_tasks(self, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.get_tasks_db(token_data['user_id'])
            if result != -1:
                return result
            else:
                return "error"
        except(Error):
            return "error"



client_service: ClientService = ClientService()