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


class ManagerServiceDB:
    def get_all_manager_db(self):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Users).filter_by(role_id=3).all()

                for obj in temp:
                    dic = {
                        "id": obj.id,
                        "city": obj.city,
                        "is_active": obj.is_active,
                        "company": obj.company,
                        "online": obj.online,
                        "username": obj.username,
                        "face_to_face": obj.face_to_face,
                        "gender": obj.gender,
                        "email": obj.email,
                        "birth_date": obj.birth_date,
                        "description": obj.description,
                        "role_id": obj.role_id
                    }
                    list.append(dic)
                    dic = {}

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def manager_send_db(self, user_id, username, description, city, company, online, gender, birth_date):
        with session_factory() as session:
            try:
                user = session.get(Users, user_id)
                user.username = username
                user.description = description
                user.city = city
                user.company = company
                user.gender = gender
                user.birth_date = birth_date
                user.online = online
                user.role_id = 3

                session.commit()

                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def give_task_db(self, psychologist_id, text, test_title, test_id, client_id):
        with session_factory() as session:
            try:
                user = session.get(Users, client_id)
                test = session.get(Test, test_id)
                if user is None:
                    return -2
                elif test is None:
                    return -3
                temp = Task(
                    id=uuid.uuid4(),
                    psychologist_id=psychologist_id,
                    text=text,
                    test_title=test_title,
                    test_id=test_id,
                    client_id=client_id,
                    is_complete=False
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1



manager_service_db: ManagerServiceDB = ManagerServiceDB()