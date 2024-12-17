from database.test_info import *
from schemas.test import SaveTestRes, CreateTest
from database.services.test import test_service_db
from database.services.users import user_service_db
from database.services.create import create_service_db
import uuid
from psycopg2 import Error
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token


class TestService:

    def save_test_result(self, payload: SaveTestRes, access_token):
        token_data = check_token(access_token)

        try:
            return test_service_db.save_test_result_db(token_data['user_id'], uuid.UUID(payload.test_id),
                                                 payload.date, payload.results)

        except(Error):
            return "error"


    def create_test(self, payload: CreateTest, access_token) -> str:
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))

        if role == 0:
            return create_service_db.create_test_db(payload.title, payload.description, payload.short_desc, payload.scales)
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    # def update_test(self, test_id, payload: UpdateTest, access_token) -> str:
    #     token_data = check_token(access_token)
    #
    #     role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
    #
    #     if role == 0:
    #         return create_service_db.update_test_db(test_id, payload.title, payload.description, payload.short_desc)
    #     else:
    #         raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def get_test_res(self, id: str, access_token, user_id):
        token_data = check_token(access_token)

        role = user_service_db.check_role(token_data['user_id'])

        if token_data["user_id"] == user_id or role == 2 or role == 3 or role == 0 or role == 1:
            if user_id != None:
                if user_service_db.get_user_by_id(user_id) == -1:
                    raise HTTPException(status_code=404, detail="Пользователя с такими данными не найдено!")

                return test_service_db.get_test_res_db(user_id, uuid.UUID(id))
            else:
                return test_service_db.get_test_res_db(token_data['user_id'], uuid.UUID(id))
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")


    def get_test_result(self, test_result_id: str, access_token):
        token_data = check_token(access_token)

        res = test_service_db.get_test_result_db(uuid.UUID(test_result_id), uuid.UUID(token_data['user_id']))

        role = user_service_db.check_role(token_data['user_id'])

        if role == 2 or role == 3 or role == 0 or role == 1:
            if res == -1:
                raise HTTPException(status_code=404, detail="Результат теста не найден!")
            return res
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")


    def get_passed_tests(self, user_id: str, access_token):
        token_data = check_token(access_token)

        res_list = test_service_db.get_passed_tests_db(uuid.UUID(user_id))

        return res_list

    def get_your_passed_tests(self, access_token):
        token_data = check_token(access_token)

        res_list = test_service_db.get_passed_tests_db(uuid.UUID(token_data['user_id']))

        return res_list

    def get_all_tests(self):
        res_list = test_service_db.get_all_tests_db()
        return res_list

    def get_test_info(self, id):
        result = test_service_db.get_test_info(id)
        return result

    def get_test_questions(self, test_id, access_token):
        token_data = check_token(access_token)

        result = test_service_db.get_test_questions_db(test_id)
        return result

    def delete_test(self, test_id: uuid.UUID, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(token_data['user_id'])

        if role == 0:
            res = test_service_db.delete_test_db(test_id)
            if res == -1:
                raise HTTPException(status_code=404, detail="Tест не найден!")
            return res
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def auto_create(self, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(token_data['user_id'])

        if role == 0:
            create_service_db.create_test(Test_maslach)
            create_service_db.create_test(Test_DASS)
            create_service_db.create_test(Test_STAI)
            create_service_db.create_test(Test_coling_strategy)
            create_service_db.create_test(Test_cmq)
            create_service_db.create_test(Test_jas)
            create_service_db.create_test(Test_bek21)
            create_service_db.create_test(Test_stress)
            return "ok"
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")



test_service: TestService = TestService()