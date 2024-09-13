from schemas.test import ConfirmApplication, SendАpplication
from database.services.application import application_service_db
from database.services.users import user_service_db
from utils.token_utils import check_token
import uuid
from fastapi import FastAPI, HTTPException




class ApplicationService:

    def send_application(self, payload: SendАpplication, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(payload.user_id)
        if (role == 2 or role == 3) and token_data['user_id'] != payload.user_id:
            result = application_service_db.send_application_db(token_data['user_id'], uuid.UUID(payload.user_id), payload.text)
            if result == 0:
                return "Successfully"
            else:
                raise HTTPException(status_code=404, detail="Пользователь не найден!")
        else:
            raise HTTPException(status_code=404, detail="Психолог не найден!")

    def confirm_application(self, payload: ConfirmApplication, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(token_data['user_id'])
        if role == 2 or role == 3:
            result = application_service_db.confirm_application_db(token_data['user_id'], uuid.UUID(payload.user_id), payload.status)
            if result == 0:
                return "Successfully"
            else:
                raise HTTPException(status_code=500, detail="Что-то пошло не так!")
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def get_list_applications(self, access_token):
        token_data = check_token(access_token)


        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 2 or role == 3:
            result = application_service_db.get_list_applications_db(token_data['user_id'])
            return result
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def watch_application(self, app_id: str, access_token):
        token_data = check_token(access_token)


        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 2 or role == 3:
            result = application_service_db.watch_application_db(token_data['user_id'], app_id)
            return result
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")


application_service: ApplicationService = ApplicationService()