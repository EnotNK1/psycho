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
from database.services.users import user_service_db


class PsychologistServiceDB:

    def psychologist_sent_db(self, user_id, username, title, document, description, city, online, face_to_face, gender,
                             birth_date, request):
        with session_factory() as session:
            try:
                user_service_db.update_user_db(user_id, username, gender, birth_date, request, city, description, 2)
                user = session.get(Users, user_id)
                user.online = online
                user.face_to_face = face_to_face
                user.role_id = 2

                ed = session.query(Education).filter_by(psychologist_id=user_id).all()
                for obj in ed:
                    session.delete(obj)
                session.commit()

                educ = Education(
                    id=uuid.uuid4(),
                    title=title,
                    document=document,
                    psychologist_id=user_id
                )
                session.add(educ)

                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_psycholog(self, user_id):
        with session_factory() as session:
            user = session.get(Users, user_id)
            list = []
            request = session.query(User_inquiries).filter_by(user_id=user_id, type=2).all()
            edu = session.query(Education).filter_by(psychologist_id=user_id).first()
            for obj in request:
                list.append(session.get(Inquiry, obj.inquiry_id).text)

            user_dict = {}
            user_dict['username'] = user.username
            user_dict['birth_date'] = user.birth_date
            user_dict['gender'] = user.gender
            user_dict['city'] = user.city
            user_dict['online'] = user.online
            user_dict['face_to_face'] = user.face_to_face
            user_dict['title'] = edu.title
            user_dict['document'] = edu.document
            user_dict['description'] = user.description
            user_dict['request'] = list

        session.commit()
        return user_dict

    def get_list_psycholog(self, user_id):
        with session_factory() as session:
            user_dict = {}
            user_list = []

            list_psycholog = session.query(Clients).filter_by(client_id=user_id, status=True).all()
            for obj in list_psycholog:
                request_list = []

                temp = session.get(Users, obj.psychologist_id)

                user_dict["id"] = temp.id
                user_dict["username"] = temp.username
                user_dict['is_active'] = temp.is_active

                request_id = session.query(User_inquiries).filter_by(user_id=temp.id, type=2).all()

                for i in request_id:
                    request = session.query(Inquiry).filter_by(id=i.inquiry_id).first()
                    request_list.append(request.text)

                user_dict['request'] = request_list

                user_list.append(user_dict)
                user_dict = {}

            session.commit()
            return user_list

    def get_all_psycholog_db(self):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Users).filter_by(role_id=2).all()

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

psychologist_service_db: PsychologistServiceDB = PsychologistServiceDB()