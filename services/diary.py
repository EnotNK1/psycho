from schemas.test import ReadThinkDiary, WritingThinkDiary, WritingFreeDiary, WritingFreeDiaryWithDate
from database.services.diary import diary_service_db
from database.services.daily_task import daily_task_service_db
from psycopg2 import Error
import uuid
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token
from datetime import datetime



class DiaryService:

    def writing_free_diary(self, payload: WritingFreeDiary, access_token):
        token_data = check_token(access_token)

        try:
            diary_service_db.writing_free_diary_db(token_data['user_id'], payload.text)
            return "Successfully"
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")
    
    def writing_free_diary_with_date(self, payload: WritingFreeDiaryWithDate, access_token):
        token_data = check_token(access_token)

        try:
            diary_service_db.writing_free_diary_with_date_db(
                token_data["user_id"], payload.text, payload.created_at
            )
            return "Successfully"
        except Error:
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def writing_think_diary(self, payload: WritingThinkDiary, access_token):
        token_data = check_token(access_token)

        try:
            res = diary_service_db.writing_think_diary_db(token_data['user_id'],
                                                    payload.situation,
                                                    payload.mood, payload.level, payload.auto_thought, payload.proofs,
                                                    payload.refutations, payload.new_mood, payload.alternative_thought,
                                                    payload.new_level, payload.behavioral)
            daily_task_service_db.auto_complete_daily_task(token_data['user_id'], uuid.UUID("fd8016cf-c1b9-4ef1-a5eb-b93773bdeb74"))
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
        
    def reading_free_diary_with_date(self, access_token, date: datetime.date):
        token_data = check_token(access_token)
        try:
            result = diary_service_db.reading_free_diary_with_date_db(
                token_data["user_id"], date
            )
            return result
        except Error:
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")
        
    def reading_free_diary_by_month(self, access_token, date: int):
        token_data = check_token(access_token)
        try:
            result = diary_service_db.reading_free_diary_by_month_db(
                token_data["user_id"], date)
            if result == -1:
                raise HTTPException(
                    status_code=500, detail="Ошибка при чтении из БД")
            return result
        except Exception as e:
            print(e)
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