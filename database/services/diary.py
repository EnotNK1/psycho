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


class DiaryServiceDB:

    def writing_free_diary_db(self, user_id, text):
        with session_factory() as session:
            try:
                temp = FreeDiary(
                    id=uuid.uuid4(),
                    user_id=user_id,
                    text=text
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
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
                )
                session.add(temp)
                session.commit()
                res = {
                    "think_diary_id": id
                }

                return res
            except (Exception, Error) as error:
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
                return dic
            except (Exception, Error) as error:
                print(error)
                return -1

    def reading_free_diary_db(self, user_id):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(FreeDiary).filter_by(user_id=user_id).all()

                for obj in temp:
                    list.append({
                        "text": obj.text,
                        "free_diary_id": obj.id
                    })

                return list
            except (Exception, Error) as error:
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

                    lis.append(dic)
                    dic = {}

                return lis
            except (Exception, Error) as error:
                print(error)
                return -1


diary_service_db: DiaryServiceDB = DiaryServiceDB()