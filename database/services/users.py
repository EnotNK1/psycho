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

class UserServiceDB:
    def create_tables(self):
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def register_user(self, id, username, email, password, city, online, face_to_face, gender, description, role_id,
                      is_active):
        with session_factory() as session:
            try:
                user = Users(id=id,
                             username=username,
                             email=email,
                             password=password,
                             city=city,
                             online=online,
                             face_to_face=face_to_face,
                             gender=gender,
                             description=description,
                             role_id=role_id,
                             is_active=is_active
                             )
                session.add(user)
                session.commit()
                return 0
            except (Exception, Error) as error:
                # print(error)
                return -1

    def check_user(self, email, password):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(email=email).one()
                pas = user.password

                if pas == password:
                    return 0
                else:
                    return -1

            except (Exception, Error) as error:
                print(error)
                return -1

    def check_role(self, id):
        with session_factory() as session:
            try:
                user = session.get(Users, id)
                role_id = user.role_id
                if role_id == 0:
                    return 0
                elif role_id == 1:
                    return 1
                elif role_id == 2:
                    return 2
                elif role_id == 3:
                    return 3
                else:
                    return -1

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_id_user(self, email):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(email=email).one()

                return user.id

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_user(self, email):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(email=email).one()

                return user

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_user_by_id(self, id):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(id=id).one()

                return user

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_password_user(self, email):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(email=email).one()
                return user.password

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_users(self):
        with session_factory() as session:
            try:
                query = select(Users)
                result = session.execute(query)
                users = result.scalars().all()

                user_list = []
                user_dict = {}
                for user in users:
                    user_dict['id'] = user.id
                    user_dict['username'] = user.username
                    user_dict['email'] = user.email
                    user_dict['password'] = user.password
                    user_dict['city'] = user.city
                    user_dict['online'] = user.online
                    user_dict['face_to_face'] = user.face_to_face
                    user_dict['gender'] = user.gender
                    user_dict['description'] = user.description
                    user_dict['role_id'] = user.role_id
                    user_dict['is_active'] = user.is_active
                    user_dict['token'] = user.token
                    user_list.append(user_dict)
                    user_dict = {}
                return user_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_data_user(self, user_id: uuid.UUID):
        with session_factory() as session:
            try:
                query = (
                    session.query(Users)
                    .filter(Users.id == user_id)
                    .options(
                        selectinload(Users.inquiry)
                    )
                )
                user = query.one_or_none()

                inquiries = session.query(User_inquiries).filter_by(user_id=user_id).all()
                request_list = [{"text": inq.text, "id": inq.id} for inq in user.inquiry]
                type_value = inquiries[0].type if inquiries else 0

                return {
                    "birth_date": user.birth_date,
                    "gender": user.gender,
                    "username": user.username,
                    "request": request_list,
                    "city": user.city,
                    "description": user.description,
                    "type": type_value
                }
            except NoResultFound:
                return None
            except Exception as e:
                raise RuntimeError(f"Database query error: {e}")

    def update_user_db(self, user_id, username, gender, birth_date, request, city, description, type):

        with session_factory() as session:
            inquiry1 = session.query(User_inquiries).filter_by(user_id=user_id, type=type).all()
            for obj in inquiry1:
                session.delete(obj)
            user = session.get(Users, user_id)
            user.username = username
            user.gender = gender
            user.birth_date = birth_date
            user.city = city
            if user.role_id == 2:
                user.description = description
            session.commit()
            for i in range(len(request)):
                try:
                    user_inquiry = User_inquiries(id=uuid.uuid4(),
                                                  user_id=user_id,
                                                  inquiry_id=request[i],
                                                  type=type
                                                  )

                    session.add(user_inquiry)

                except (Exception, Error) as error:
                    print(error)
                    return -1

            session.commit()
            return 0

    def add_token_db(self, user_id, token_str):
        with session_factory() as session:
            try:
                token = Token(id=uuid.uuid4(),
                              user_id=user_id,
                              token=token_str,
                              exp_date=func.now(),
                              type=""
                              )
                session.add(token)
                session.commit()
                return 0
            except (Exception, Error) as error:
                raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def get_user_by_token(self, token_id):
        with session_factory() as session:
            try:
                token = session.query(Token).filter_by(token=token_id)
                user_id = token[0].user_id
                user = session.query(Users).filter_by(id=user_id).one()
                if user:
                    return user
                else:
                    return 0
            except (Exception, Error) as error:
                print(error)
                return 0



    def get_email_by_id(self, user_id: uuid.UUID):
        with session_factory() as session:
            try:
                user = session.get(Users, user_id)
                return user.email
            except (Exception, Error) as error:
                print(error)


user_service_db: UserServiceDB = UserServiceDB()