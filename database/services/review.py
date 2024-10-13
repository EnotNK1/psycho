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
from database.models.review import *

from database.database import engine, session_factory
from database.calculator import calculator_service
from database.enum import DiaryType
from fastapi import FastAPI, HTTPException
import uuid
from datetime import datetime

class ReviewServicedb:

    def create_review(self, review_data):
        with session_factory() as session:
            try:
                review = Review(
                    id=uuid.uuid4(),
                    text=review_data.text,
                    email=review_data.email,
                    is_read=False,
                    created_at=datetime.now()
                )
                session.add(review)
                session.commit()
                return "review.id"
            except (Exception, Error) as error:
                print(error)
                return None


    def get_all_reviews(self) -> list:
        with session_factory() as session:
            try:
                return session.query(Review).all()
            except (Exception, Error) as error:
                print(error)
                return []


    def mark_review_as_read(self, review_id: uuid.UUID):
        with session_factory() as session:
            try:
                review = session.query(Review).filter(Review.id == review_id).first()
                if review:
                    review.is_read = True
                    session.commit()
            except (Exception, Error) as error:
                print(error)


    def delete_review(self, review_id: uuid.UUID):
        with session_factory() as session:
            try:
                review = session.query(Review).filter(Review.id == review_id).first()
                if review:
                    session.delete(review)
                    session.commit()
            except (Exception, Error) as error:
                print(error)

review_service_db: ReviewServicedb = ReviewServicedb()