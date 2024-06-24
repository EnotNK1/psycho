from schemas.test import SaveTestRes, CreateTest
from database.database import database_service
import uuid
from psycopg2 import Error
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token


class TestService:

    def save_test_result(self, payload: SaveTestRes, access_token):
        token_data = check_token(access_token)

        try:
            return database_service.save_test_result_db(token_data['user_id'], uuid.UUID(payload.test_id),
                                                 payload.date, payload.results)

        except(Error):
            return "error"


    def create_test(self, payload: CreateTest, access_token) -> str:
        token_data = check_token(access_token)

        role = database_service.check_role(uuid.UUID(token_data['user_id']))

        if role == 0:
            return database_service.create_test_db(payload.title, payload.description, payload.short_desc, payload.scales)
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def get_test_res(self, id: str, access_token, user_id):
        token_data = check_token(access_token)

        if database_service.get_user_by_id(user_id) == -1:
            raise HTTPException(status_code=404, detail="Пользователя с такими данными не найдено!")

        if user_id != None:
            return database_service.get_test_res_db(user_id, uuid.UUID(id))
        else:
            return database_service.get_test_res_db(token_data['user_id'], uuid.UUID(id))


    def get_test_result(self, test_result_id: str, access_token):
        token_data = check_token(access_token)

        res = database_service.get_test_result_db(token_data['user_id'], uuid.UUID(test_result_id))

        if res == -1:
            raise HTTPException(status_code=404, detail="Результат теста не найден!")

        return res


    def get_passed_tests(self, user_id: str, access_token):
        token_data = check_token(access_token)

        res_list = database_service.get_passed_tests_db(uuid.UUID(user_id))

        return res_list

    def get_all_tests(self):
        res_list = database_service.get_all_tests_db()
        return res_list

    def get_test_info(self, id):
        result = database_service.get_test_info(id)
        return result


test_service: TestService = TestService()