from database.test_info import *
from schemas.education_material import CompleteEducation
from database.database import database_service
import uuid
from psycopg2 import Error
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token


class EducationService:

    def get_all_theme(self, access_token):
        token_data = check_token(access_token)

        res_list = database_service.get_all_education_theme_db(token_data['user_id'])
        return res_list

    def get_all_education_material(self, education_theme_id, access_token):
        token_data = check_token(access_token)

        result = database_service.get_all_education_material_db(education_theme_id)
        return result

    def complete_education_material(self, payload: CompleteEducation, access_token):
        token_data = check_token(access_token)

        result = database_service.complete_education_material_db(payload.education_material_id, token_data['user_id'])
        return result


    def auto_create(self, access_token):
        token_data = check_token(access_token)

        role = database_service.check_role(token_data['user_id'])

        if role == 0:
            database_service.create_test(Test_maslach)
            database_service.create_test(Test_DASS)
            database_service.create_test(Test_STAI)
            database_service.create_test(Test_coling_strategy)
            database_service.create_test(Test_cmq)
            database_service.create_test(Test_jas)
            database_service.create_test(Test_bek21)
            return "ok"
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")



education_service: EducationService = EducationService()