from database.services.psychologist import psychologist_service_db
from schemas.users import Psychologist
import uuid
from psycopg2 import Error
from utils.token_utils import check_token


class PsychologistService:

    def psychologist_sent(self, payload: Psychologist, access_token):
        token_data = check_token(access_token)

        try:
            result = psychologist_service_db.psychologist_sent_db(token_data['user_id'], payload.username, payload.title,
                                                           payload.document,
                                                           payload.description,
                                                           payload.city, payload.online, payload.face_to_face,
                                                           payload.gender,
                                                           payload.birth_date,
                                                           payload.request, payload.department)
            if result != -1:
                return "Successfully"
            else:
                return "error"
        except(Error):
            return "error"

    def get_psycholog(self, psycholog_id: str, access_token):
        token_data = check_token(access_token)

        items = psychologist_service_db.get_psycholog(psycholog_id)
        return items


    # def get_list_psycholog(self, access_token):
    #     token_data = check_token(access_token)
    #
    #     items = database_service.get_list_psycholog(token_data['user_id'])
    #     return items

    def get_all_psycholog(self, access_token):
        token_data = check_token(access_token)

        items = psychologist_service_db.get_all_psycholog_db()
        return items



psychologist_service: PsychologistService = PsychologistService()
