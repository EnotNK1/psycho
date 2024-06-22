from schemas.test import ReadThinkDiary, WritingThinkDiary, WritingFreeDiary
from database.database import database_service
from psycopg2 import Error
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token


class DiaryService:

    def writing_free_diary(self, payload: WritingFreeDiary, access_token):
        token_data = check_token(access_token)

        try:
            database_service.writing_free_diary_db(token_data['user_id'], payload.text)
            return "Successfully"
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def writing_think_diary(self, payload: WritingThinkDiary, access_token):
        token_data = check_token(access_token)

        try:
            database_service.writing_think_diary_db(token_data['user_id'], payload.deep_conviction_id,
                                                    payload.situation,
                                                    payload.mood, payload.level, payload.auto_thought, payload.proofs,
                                                    payload.refutations, payload.new_mood, payload.new_level,
                                                    payload.behaviour)
            return "Successfully"
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def reading_free_diary(self, access_token):
        token_data = check_token(access_token)

        try:
            result = database_service.reading_free_diary_db(token_data['user_id'])
            return result
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def reading_think_diary(self, payload: ReadThinkDiary, access_token):
        token_data = check_token(access_token)

        try:
            result = database_service.reading_think_diary_db(payload.think_diary_id)
            return result
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

diary_service: DiaryService = DiaryService()