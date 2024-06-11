from schemas.test import ReadThinkDiary, WritingThinkDiary, WritingFreeDiary
from database.database import database_service
from services.auth import verify_token
from psycopg2 import Error
from fastapi import FastAPI, HTTPException




class DiaryService:

    def writing_free_diary(self, payload: WritingFreeDiary, access_token):
        if not access_token:
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

        try:
            database_service.writing_free_diary_db(token_data['user_id'], payload.text)
            return "Successfully"
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def writing_think_diary(self, payload: WritingThinkDiary, access_token):
        if not access_token:
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

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
        if not access_token:
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

        try:
            result = database_service.reading_free_diary_db(token_data['user_id'])
            return result
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def reading_think_diary(self, payload: ReadThinkDiary, access_token):
        if not access_token:
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            raise HTTPException(status_code=401, detail="Время сессии истекло!")
        elif token_data == 'Invalid token':
            raise HTTPException(status_code=401, detail="Вы не авторизованы!")

        try:
            result = database_service.reading_think_diary_db(payload.think_diary_id)
            return result
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

diary_service: DiaryService = DiaryService()