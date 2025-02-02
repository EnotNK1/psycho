from psycopg2 import Error
from sqlalchemy import create_engine, select, func, distinct, cast, Date
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, join, DeclarativeBase
from schemas.test import ResScale, ReqBorder, ReqScale
from typing import List
from sqlalchemy.exc import NoResultFound, SQLAlchemyError

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
import calendar
from datetime import datetime, date, time, timedelta
from sqlalchemy.sql.expression import cast
from sqlalchemy.types import Date


class DiaryServiceDB:

    def writing_free_diary_db(self, user_id, text):
        with session_factory() as session:
            try:
                temp = FreeDiary(
                    id=uuid.uuid4(),
                    user_id=user_id,
                    text=text,
                    created_at=datetime.now()
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, SQLAlchemyError) as error:
                print(error)
                return -1

    def writing_think_diary_db(self, user_id, situation, mood, level, auto_thought, proofs,
                               refutations, new_mood, alternative_thought, new_level, behavioral):
        with session_factory() as session:
            try:
                id = uuid.uuid4()
                temp = Diary_record(
                    id=id,
                    user_id=user_id,
                    situation=situation,
                    mood=mood,
                    level=level,
                    auto_thought=auto_thought,
                    proofs=proofs,
                    refutations=refutations,
                    new_mood=new_mood,
                    alternative_thought=alternative_thought,
                    new_level=new_level,
                    behavioral=behavioral,
                    created_at=datetime.now()
                )
                session.add(temp)
                session.commit()
                res = {
                    "think_diary_id": id
                }

                return res
            except (Exception, SQLAlchemyError) as error:
                print(error)
                return -1

    def reading_think_diary_db(self, think_diary_id):
        with session_factory() as session:
            try:
                dic = {}
                temp = session.get(Diary_record, think_diary_id)

                dic["situation"] = temp.situation
                dic["mood"] = temp.mood
                dic["level"] = temp.level
                dic["auto_thought"] = temp.auto_thought
                dic["proofs"] = temp.proofs
                dic["refutations"] = temp.refutations
                dic["new_mood"] = temp.new_mood
                dic["alternative_thought"] = temp.alternative_thought
                dic["new_level"] = temp.new_level
                dic["behavioral"] = temp.behavioral
                dic["created_at"] = temp.created_at
                return dic
            except (Exception, SQLAlchemyError) as error:
                print(error)
                return -1

    def reading_free_diary_db(self, user_id):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(FreeDiary).filter_by(user_id=user_id).order_by(FreeDiary.created_at).all()

                for obj in temp:
                    list.append({
                        "text": obj.text,
                        "free_diary_id": obj.id,
                        "created_at": obj.created_at
                    })

                return list
            except (Exception, SQLAlchemyError) as error:
                print(error)
                return -1
            
    def writing_free_diary_with_date_db(self, user_id, text, created_at):
        with session_factory() as session:
            try:
                temp = FreeDiary(
                    id=uuid.uuid4(),
                    user_id=user_id,
                    text=text,
                    created_at=created_at,
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, SQLAlchemyError) as error:
                print(error)
                return -1
            
    def reading_free_diary_with_date_db(self, user_id, date):
        with session_factory() as session:
            try:
                temp = (
                    session.query(FreeDiary)
                    .filter(
                        FreeDiary.user_id == user_id,
                        cast(FreeDiary.created_at, Date) == date,
                    )
                    .order_by(FreeDiary.created_at)
                    .all()
                )
                # Формируем список заметок
                result = [
                    {
                        "text": obj.text,
                        "free_diary_id": str(obj.id),
                        "created_at": obj.created_at,
                    }
                    for obj in temp
                ]

                return result
            except (Exception, SQLAlchemyError) as error:
                print(error)
                return -1
            
    def reading_free_diary_by_month_db(self, user_id, unix_date: int):
        with session_factory() as session:
            try:
                # Преобразуем unix метку в datetime (предполагаем, что время всегда 00:00)
                month_datetime = datetime.fromtimestamp(unix_date)
                # Первый день месяца
                first_day = month_datetime.replace(day=1)
                # Последний день месяца
                last_day_number = calendar.monthrange(first_day.year, first_day.month)[1]
                last_day = first_day.replace(day=last_day_number)

                # Запрос заметок за указанный месяц
                diaries = (
                    session.query(FreeDiary)
                    .filter(
                        FreeDiary.user_id == user_id,
                        cast(FreeDiary.created_at, Date) >= first_day.date(),
                        cast(FreeDiary.created_at, Date) <= last_day.date()
                    )
                    .all()
                )

                # Собираем набор дат, на которые имеются заметки
                diary_dates = {diary.created_at.date() for diary in diaries}

                # Формируем список всех дней месяца с нужной информацией
                days_list = []
                current_day = first_day.date()
                while current_day <= last_day.date():
                    # Формируем datetime для 00:00 текущего дня
                    current_day_dt = datetime.combine(current_day, time(0, 0))
                    days_list.append({
                        "date": int(current_day_dt.timestamp()),
                        "diary": current_day in diary_dates
                    })
                    current_day += timedelta(days=1)

                return days_list
            except (Exception, SQLAlchemyError) as error:
                print(error)
                return -1


    def get_all_think_diary_db(self, user_id):
        with session_factory() as session:
            try:
                lis = []
                dic = {}
                temp = session.query(Diary_record).filter_by(user_id=user_id).all()

                for obj in temp:
                    dic["id"] = obj.id
                    dic["situation"] = obj.situation
                    dic["created_at"] = obj.created_at

                    lis.append(dic)
                    dic = {}

                return lis
            except (Exception, SQLAlchemyError) as error:
                print(error)
                return -1


diary_service_db: DiaryServiceDB = DiaryServiceDB()