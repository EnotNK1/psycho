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


class DialigServiceDB:

    def writing_r_i_dialog_db(self, problem_id, text, type):
        with session_factory() as session:
            try:
                temp = Message_r_i_dialog(
                    id=uuid.uuid4(),
                    problem_id=problem_id,
                    text=text,
                    is_rational=type,
                    date=func.now()
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def reading_r_i_dialog_db(self, problem_id):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Message_r_i_dialog).filter_by(problem_id=problem_id).all()

                for obj in temp:
                    list.append(obj)

                return list
            except (Exception, Error) as error:
                print(error)
                return -1



dialog_service_db: DialigServiceDB = DialigServiceDB()