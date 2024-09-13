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


class ApplicationServiceDB:

    def send_application_db(self, client_id, psyh_id, text):
        with session_factory() as session:
            temp = session.query(Clients).filter_by(client_id=client_id, psychologist_id=psyh_id).first()
            if temp:
                session.delete(temp)

            try:
                app = Clients(id=uuid.uuid4(),
                              psychologist_id=psyh_id,
                              client_id=client_id,
                              text=text,
                              status=False
                              )
                session.add(app)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def confirm_application_db(self, psyh_id, client_id, status):
        with session_factory() as session:
            try:

                temp = session.query(Clients).filter_by(client_id=client_id, psychologist_id=psyh_id).first()

                if temp is None:
                    raise ValueError(f"Клиент с client_id={client_id} и psychologist_id={psyh_id} не найден")

                if status is False:
                    session.delete(temp)
                elif status is True:
                    temp.status = status

                session.commit()
                return 0
            except ValueError as ve:
                print(f"Ошибка значения: {ve}")
                return -1
            except (Exception, Error) as error:
                print(f"Исключение: {error}")
                session.rollback()  # Откат в случае ошибки
                return -1

    def get_list_applications_db(self, user_id):
        with session_factory() as session:
            try:
                result_list = []

                temp = session.query(Clients).filter_by(psychologist_id=user_id, status=False).all()

                for obj in temp:
                    user = session.get(Users, obj.client_id)
                    if user is None:
                        continue  # Skip if user not found

                    problem = session.query(Problem).filter_by(user_id=user.id).first()
                    if problem is None:
                        dict_item = {
                            "app_id": obj.id,
                            "client_id": obj.client_id,
                            "username": user.username,
                            "text": obj.text,
                            "online": user.online,
                            "problem_id": None,
                            "problem": None
                        }
                        result_list.append(dict_item)
                        continue  # Skip if problem not found

                    # Create a new dictionary for each iteration
                    dict_item = {
                        "app_id": obj.id,
                        "client_id": obj.client_id,
                        "username": user.username,
                        "text": obj.text,
                        "online": user.online,
                        "problem_id": problem.id,
                        "problem": problem.description
                    }

                    result_list.append(dict_item)
                return result_list
            except (Exception, Error) as error:
                print(error)
                return -1

    def watch_application_db(self, user_id, app_id):
        with session_factory() as session:
            try:
                app = session.get(Clients, app_id)
                user = session.get(Users, app.client_id)
                dict = {}

                dict["app_id"] = app.id
                dict["client_id"] = app.client_id
                dict["username"] = user.username
                dict["is_active"] = False
                dict["birth_date"] = user.birth_date
                dict["gender"] = user.gender
                dict["text"] = app.text

                return dict
            except (Exception, Error) as error:
                print(error)
                return -1



application_service_db: ApplicationServiceDB = ApplicationServiceDB()