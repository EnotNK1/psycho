from psycopg2 import Error
from sqlalchemy import create_engine, select, func, distinct
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, join, DeclarativeBase
from schemas.test import ResScale, ReqBorder, ReqScale
from typing import List
from sqlalchemy.exc import NoResultFound

from database.inquiries import inquiries
from database.models.client import *
from database.models.diary import *
from database.models.education import *
from database.models.experiment import *
from database.models.inquiry import *
from database.models.mood_tracker import *
from database.models.post import *
from database.models.problem import *
from database.models.test import *
from database.models.users import *

from database.database import engine, session_factory
from database.calculator import calculator_service
from database.enum import DiaryType
from fastapi import FastAPI, HTTPException
import uuid
from datetime import datetime

class MoodTrackerServiceDB:

    def save_mood_tracker_db(self, user_id, score, free_diary_id, think_diary_id, diary_type):
        with session_factory() as session:
            if think_diary_id:
                temp = session.get(Diary_record, think_diary_id)
                if temp is None:
                    raise HTTPException(status_code=404, detail="Запись дневника мыслей не найдена!")
            if free_diary_id:
                temp = session.get(FreeDiary, free_diary_id)
                if temp is None:
                    raise HTTPException(status_code=404, detail="Запись вольного дневника не найдена!")

            id = uuid.uuid4()
            date = datetime.utcnow()
            if diary_type:
                diary_type = DiaryType(diary_type)

            temp = Mood_tracker(
                id=id,
                user_id=user_id,
                score=score,
                free_diary_id=free_diary_id,
                think_diary_id=think_diary_id,
                diary_type=diary_type,
                date=date
            )
            session.add(temp)
            session.commit()
            dic = {
                "mood_tracker_id": id
            }
            return dic

    def get_all_mood_tracker_db(self, user_id):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Mood_tracker).filter_by(user_id=user_id).all()

                for obj in temp:
                    list.append(obj)

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_mood_tracker_db(self, mood_tracker_id):
        with session_factory() as session:
            temp = session.get(Mood_tracker, mood_tracker_id)
            if temp:
                return temp
            else:
                raise HTTPException(status_code=404, detail="Запись не найдена!")



mood_tracker_service_db: MoodTrackerServiceDB = MoodTrackerServiceDB()