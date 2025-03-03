from database.services.dialog import dialog_service_db
from schemas.test import ReadRIDialog, WritingRIDialog
from psycopg2 import Error
from utils.token_utils import check_token



class DialogService:

    def writing_r_i_dialog(self, payload: WritingRIDialog, access_token):
        token_data = check_token(access_token)

        try:
            dialog_service_db.writing_r_i_dialog_db(payload.problem_id, payload.text, payload.type)
            return "Successfully"
        except(Error):
            return "error"

    def reading_r_i_dialog(self, payload: ReadRIDialog, access_token):
        token_data = check_token(access_token)

        try:
            result = dialog_service_db.reading_r_i_dialog_db(payload.problem_id)
            return result
        except(Error):
            return "error"


dialog_service: DialogService = DialogService()