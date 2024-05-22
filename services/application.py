from schemas.test import WatchApplication, ConfirmApplication, SendАpplication
from database.database import database_service
from services.auth import verify_token
import uuid




class ApplicationService:

    def send_application(self, payload: SendАpplication, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(payload.user_id)
        if role == 2 and token_data['user_id'] != payload.user_id:
            database_service.send_application_db(token_data['user_id'], payload.user_id, payload.text)
            return "Successfully"
        else:
            return "error"

    def confirm_application(self, payload: ConfirmApplication, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"
        role = database_service.check_role(token_data['user_id'])
        if role == 2:
            database_service.confirm_application_db(token_data['user_id'], payload.user_id, payload.status)
            return "Successfully"
        else:
            return "error"

    def get_list_applications(self, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"


        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            result = database_service.get_list_applications_db(token_data['user_id'])
            return result
        else:
            return "access denied"

    def watch_application(self, payload: WatchApplication, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"


        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            result = database_service.watch_application_db(token_data['user_id'], payload.app_id)
            return result
        else:
            return "access denied"


application_service: ApplicationService = ApplicationService()