from schemas.test import SaveTestRes, CreateTest
from database.database import database_service
from services.auth import verify_token
import uuid
from psycopg2 import Error
from fastapi import FastAPI, HTTPException


class TestService:

    def save_test_result(self, payload: SaveTestRes, access_token):
        if not access_token:
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

        try:
            return database_service.save_test_result_db(token_data['user_id'], uuid.UUID(payload.test_id),
                                                 payload.date, payload.results)

        except(Error):
            return "error"


    def create_test(self, payload: CreateTest, access_token) -> str:
        if not access_token:
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

        role = database_service.check_role(uuid.UUID(token_data['user_id']))

        if role == 0:
            return database_service.create_test_db(payload.title, payload.description, payload.short_desc, payload.scales)
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def get_test_res(self, id: str, access_token):
        if not access_token:
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

        res_list = database_service.get_test_res_db(token_data['user_id'], uuid.UUID(id))

        return res_list

    def get_passed_tests(self, user_id: str, access_token):
        if not access_token:
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

        res_list = database_service.get_passed_tests_db(uuid.UUID(user_id))

        return res_list

    def get_all_tests(self):
        res_list = database_service.get_all_tests_db()
        return res_list

    def get_test_info(self, id):
        result = database_service.get_test_info(id)
        return result


test_service: TestService = TestService()