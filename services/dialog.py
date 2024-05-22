from database.database import database_service
from schemas.test import ReadRIDialog, WritingRIDialog
from services.auth import verify_token
from psycopg2 import Error



class DialogService:

    def writing_r_i_dialog(self, payload: WritingRIDialog, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            database_service.writing_r_i_dialog_db(payload.problem_id, payload.text, payload.type)
            return "Successfully"
        except(Error):
            return "error"

    def reading_r_i_dialog(self, payload: ReadRIDialog, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.reading_r_i_dialog_db(payload.problem_id)
            return result
        except(Error):
            return "error"


dialog_service: DialogService = DialogService()