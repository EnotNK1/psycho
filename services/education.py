from database.services.daily_task import daily_task_service_db
from database.test_info import *
from schemas.education_material import CompleteEducation
from database.services.education import education_service_db
from database.services.users import user_service_db
from database.services.create import create_service_db
import uuid
from psycopg2 import Error
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token


class EducationService:

    def get_all_theme(self, access_token):
        token_data = check_token(access_token)

        res_list = education_service_db.get_all_education_theme_db(token_data['user_id'])
        return res_list

    def get_all_education_material(self, education_theme_id, access_token):
        token_data = check_token(access_token)

        result = education_service_db.get_all_education_material_db(education_theme_id, token_data["user_id"])
        return result

    def complete_education_material(self, payload: CompleteEducation, access_token):
        token_data = check_token(access_token)

        result = education_service_db.complete_education_material_db(payload.education_material_id, token_data['user_id'])

        # theme_id = education_service_db.get_edu_theme_by_edu_material(payload.education_material_id)
        daily_task_service_db.auto_complete_daily_task(token_data['user_id'], payload.education_material_id)
        return result

    def delete_education(self, education_id: str, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(token_data['user_id'])

        if role == 0:
            res = education_service_db.delete_education_theme_db(uuid.UUID(education_id))
            if res == -1:
                raise HTTPException(status_code=404, detail="Тема не найдена!")
            return res
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")



education_service: EducationService = EducationService()