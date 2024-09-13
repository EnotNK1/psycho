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


class BeliefServiceDB:
    def create_deep_conviction_db(self, problem_id, disadaptive, adaptive):
        with session_factory() as session:
            try:
                temp = Deep_conviction(
                    id=uuid.uuid4(),
                    problem_id=problem_id,
                    disadaptive=disadaptive,
                    adaptive=adaptive
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def save_belief_analysis_db(self, intermediate_conviction_id, text,
                                feeling_and_actions, motivation, hindrances, incorrect_victims, results):
        with session_factory() as session:
            try:
                temp = session.get(Intermediate_belief, intermediate_conviction_id)
                temp.text = text
                temp.feelings_and_actions = feeling_and_actions
                temp.motivation = motivation
                temp.hindrances = hindrances
                temp.incorrect_victims = incorrect_victims
                temp.results = results
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def save_belief_check_db(self, intermediate_conviction_id, truthfulness, consistency, usefulness):
        with session_factory() as session:
            try:
                temp = session.get(Intermediate_belief, intermediate_conviction_id)
                temp.truthfulness = truthfulness
                temp.consistency = consistency
                temp.usefulness = usefulness
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_belief_analysis(self, intermediate_conviction_id):
        with session_factory() as session:
            try:
                dic = {}
                temp = session.get(Intermediate_belief, intermediate_conviction_id)
                dic["feelings_and_actions"] = temp.feelings_and_actions
                dic["motivation"] = temp.motivation
                dic["hindrances"] = temp.hindrances
                dic["incorrect_victims"] = temp.incorrect_victims
                dic["results"] = temp.results

                return dic
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_belief_check(self, intermediate_conviction_id):
        with session_factory() as session:
            try:
                dic = {}
                temp = session.get(Intermediate_belief, intermediate_conviction_id)
                dic["truthfulness"] = temp.truthfulness
                dic["consistency"] = temp.consistency
                dic["usefulness"] = temp.usefulness

                return dic
            except (Exception, Error) as error:
                print(error)
                return -1


bser_service_db: BeliefServiceDB = BeliefServiceDB()