from database.services.user_statistics import user_statistics_service_db
from database.test_info import *
from schemas.test import SaveTestRes, CreateTest
from database.services.test import test_service_db
from database.services.users import user_service_db
from database.services.create import create_service_db
import uuid
from psycopg2 import Error
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token


class UserStatisticsService:

    def general_test_results(self, psychologist_id: uuid.UUID, access_token: str):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))

        if role in [0, 1, 2, 3]:
            return user_statistics_service_db.general_test_results(psychologist_id)
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")



user_statistics_service: UserStatisticsService = UserStatisticsService()