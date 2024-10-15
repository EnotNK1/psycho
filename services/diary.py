from schemas.test import ReadThinkDiary, WritingThinkDiary, WritingFreeDiary
from database.services.diary import diary_service_db
from psycopg2 import Error
import uuid
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token



class DiaryService:

    def writing_free_diary(self, payload: WritingFreeDiary, access_token):
        token_data = check_token(access_token)

        try:
            diary_service_db.writing_free_diary_db(token_data['user_id'], payload.text)
            return "Successfully"
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def writing_think_diary(self, payload: WritingThinkDiary, access_token):
        token_data = check_token(access_token)

        try:
            res = diary_service_db.writing_think_diary_db(token_data['user_id'],
                                                    payload.situation,
                                                    payload.mood, payload.level, payload.auto_thought, payload.proofs,
                                                    payload.refutations, payload.new_mood, payload.alternative_thought,
                                                    payload.new_level, payload.behavioral)
            return res
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def reading_free_diary(self, access_token):
        token_data = check_token(access_token)

        try:
            result = diary_service_db.reading_free_diary_db(token_data['user_id'])
            return result
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def reading_think_diary(self, payload: ReadThinkDiary, access_token):
        token_data = check_token(access_token)

        try:
            result = diary_service_db.reading_think_diary_db(payload.think_diary_id)
            return result
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def get_all_think_diary(self, user_id: str, access_token):
        token_data = check_token(access_token)

        result = diary_service_db.get_all_think_diary_db(uuid.UUID(user_id))
        return result

diary_service: DiaryService = DiaryService()