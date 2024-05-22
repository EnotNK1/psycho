from schemas.test import ReadThinkDiary, WritingThinkDiary, WritingFreeDiary
from database.database import database_service
from services.auth import verify_token
from psycopg2 import Error




class DiaryService:

    def writing_free_diary(self, payload: WritingFreeDiary, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            database_service.writing_free_diary_db(token_data['user_id'], payload.text)
            return "Successfully"
        except(Error):
            return "error"

    def writing_think_diary(self, payload: WritingThinkDiary, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            database_service.writing_think_diary_db(token_data['user_id'], payload.deep_conviction_id,
                                                    payload.situation,
                                                    payload.mood, payload.level, payload.auto_thought, payload.proofs,
                                                    payload.refutations, payload.new_mood, payload.new_level,
                                                    payload.behaviour)
            return "Successfully"
        except(Error):
            return "error"

    def reading_free_diary(self, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.reading_free_diary_db(token_data['user_id'])
            return result
        except(Error):
            return "error"

    def reading_think_diary(self, payload: ReadThinkDiary, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.reading_think_diary_db(payload.think_diary_id)
            return result
        except(Error):
            return "error"

diary_service: DiaryService = DiaryService()