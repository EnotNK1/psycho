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


class ProblemServiceDB:

    def add_problem_db(self, user_id, description, goal):
        with session_factory() as session:
            try:
                problem = Problem(id=uuid.uuid4(),
                                  description=description,
                                  user_id=user_id,
                                  goal=goal
                                  )
                session.add(problem)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def save_problem_analysis_db(self, problem_id, type):
        with session_factory() as session:
            try:
                temp = Intermediate_belief(
                    id=uuid.uuid4(),
                    problem_id=problem_id,
                    type=type
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_problem_analysis_db(self, problem_id):
        with session_factory() as session:
            try:
                temp = session.query(Intermediate_belief).filter_by(problem_id=problem_id).all()
                list = []
                dict = {}

                for obj in temp:
                    dict["id"] = obj.id
                    dict["text"] = obj.text
                    dict["truthfulness"] = obj.truthfulness
                    dict["consistency"] = obj.consistency
                    dict["usefulness"] = obj.usefulness
                    dict["feelings_and_actions"] = obj.feelings_and_actions
                    dict["motivation"] = obj.motivation
                    dict["hindrances"] = obj.hindrances
                    dict["incorrect_victims"] = obj.incorrect_victims
                    dict["results"] = obj.results
                    dict["problem_id"] = obj.problem_id
                    dict["deep_conviction_id"] = obj.deep_conviction
                    dict["type"] = obj.type
                    list.append(dict)
                    dict = {}

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_problems(self, user_id):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Problem).filter_by(user_id=user_id).all()

                for obj in temp:
                    list.append(obj)

                return list
            except (Exception, Error) as error:
                print(error)
                return -1



problem_service_db: ProblemServiceDB = ProblemServiceDB()