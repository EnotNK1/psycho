from database.database import database_service
from schemas.users import Psychologist
from services.auth import verify_token
import uuid
from psycopg2 import Error


class PsychologistService:

    def psychologist_sent(self, payload: Psychologist, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.psychologist_sent_db(token_data['user_id'], payload.username, payload.title,
                                                           payload.document,
                                                           payload.description,
                                                           payload.city, payload.online, payload.face_to_face,
                                                           payload.gender,
                                                           payload.birth_date,
                                                           payload.request)
            if result != -1:
                return "Successfully"
            else:
                return "error"
        except(Error):
            return "error"

    def get_psycholog(self, psycholog_id: str, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        items = database_service.get_psycholog(psycholog_id)
        return items


    def get_list_psycholog(self, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        items = database_service.get_list_psycholog(token_data['user_id'])
        return items



psychologist_service: PsychologistService = PsychologistService()
