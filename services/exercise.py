from database.services.exercise import exercise_service_db
from schemas.users import Creds, Reg, ResetPassword, UpdateUser, UserResponse, UserData
from schemas.review import ReviewCreate, ReviewRead
from database.services.users import user_service_db
from database.services.review import review_service_db
from services.auth import send_email
from services.auth import generate_token
import uuid
from starlette.responses import Response
from smtplib import SMTPRecipientsRefused
from psycopg2 import Error
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token


class ExerciseService:

    def get_all_exercises(self, access_token: str):
        token_data = check_token(access_token)

        exercises = exercise_service_db.get_all_exercises()
        return exercises

    def get_exercise(self, exercise_id: uuid.UUID, access_token: str):
        token_data = check_token(access_token)

        exercise = exercise_service_db.get_exercise(exercise_id)
        return exercise




exercise_service: ExerciseService = ExerciseService()