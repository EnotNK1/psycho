from schemas.test import SaveTestRes, CreateTest, GetTestRes, GetPassTest
from database.database import database_service
from services.auth import verify_token
import uuid
from psycopg2 import Error


class TestService:

    def save_test_result(self, payload: SaveTestRes, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.save_test_result_db(token_data['user_id'], payload.title, uuid.UUID(payload.test_id),
                                                 payload.date, payload.score, payload.min, payload.max)
            if result == 0:
                return "Successfully"
            else:
                return "error"
        except(Error):
            return "error"

    def create_test(self, payload: CreateTest, access_token) -> str:
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))

        if role == 0:
            database_service.create_test_db(payload.title, payload.description, payload.short_desc)
            return "Successfully"
        else:
            return "access denied"

    def get_test_res(self, payload: GetTestRes, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        res_list = database_service.get_test_res_db(token_data['user_id'], uuid.UUID(payload.test_id))

        return res_list

    def get_passed_tests(self, payload: GetPassTest, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        res_list = database_service.get_passed_tests_db(payload.user_id)

        return res_list

    def get_all_tests(self):
        res_list = database_service.get_all_tests_db()
        return res_list


test_service: TestService = TestService()