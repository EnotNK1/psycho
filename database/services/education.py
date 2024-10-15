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


class EducationServiceDB:

    def get_all_education_theme_db(self, user_id):
        with session_factory() as session:
            try:
                query = select(Educational_theme).options(selectinload(Educational_theme.educational_material).
                                                          selectinload(Educational_material.educational_progress))
                result = session.execute(query)
                education_theme = result.scalars().all()

                user_list = []
                user_dict = {}
                user_id = uuid.UUID(user_id)
                for temp in education_theme:
                    score = 0
                    for education_material in temp.educational_material:
                        if len(education_material.educational_progress) != 0:
                            for educational_progress in education_material.educational_progress:
                                if educational_progress.user_id == user_id:
                                    score += 1

                    user_dict['id'] = temp.id
                    user_dict['theme'] = temp.theme
                    user_dict['score'] = score
                    user_dict['max_score'] = len(temp.educational_material)

                    user_list.append(user_dict)
                    user_dict = {}
                return user_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_education_material_db(self, education_theme_id):
        with session_factory() as session:
            try:
                education_material = session.query(Educational_material).filter_by(educational_theme_id=education_theme_id).all()

                user_list = []
                user_dict = {}
                for temp in education_material:
                    user_dict['id'] = temp.id
                    user_dict['text'] = temp.text

                    user_list.append(user_dict)
                    user_dict = {}
                return user_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def complete_education_material_db(self, edu_id, user_id):
        with session_factory() as session:
            material = session.query(Educational_material).get(edu_id)
            if not material:
                raise HTTPException(status_code=404, detail="Материал не найден!")

            temp = session.query(Educational_progress).filter_by(
                user_id=user_id, educational_material_id=edu_id).first()

            if not temp:
                education_progress = Educational_progress(
                    id=edu_id,
                    user_id=user_id,
                    educational_material_id=edu_id
                )
                session.add(education_progress)
                session.commit()
                dic = {
                    "status": "ok"
                }
                return dic
            else:
                raise HTTPException(status_code=409, detail="Данный материал уже пройден!")


education_service_db: EducationServiceDB = EducationServiceDB()