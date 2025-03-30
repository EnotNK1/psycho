from database.services.daily_task import daily_task_service_db
from database.services.exercise import exercise_service_db
from schemas.exercise import ProblemAnalysis, DefiningProblemGroups, ProblemsAndGoals, TestingBeliefs, BeliefAnalysis, \
    EditExerciseResult, SaveExerciseResult
# from database.models.exercise import Сompleted_exercise, Filled_field
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
from typing import List


class ExerciseService:

    def get_defining_problem_groups(self, exercise_id: uuid.UUID, access_token: str):
        token_data = check_token(access_token)

        exercise = exercise_service_db.get_defining_problem_groups(exercise_id)
        return exercise

    def get_problems_and_goals(self, exercise_id: uuid.UUID, access_token: str):
        token_data = check_token(access_token)

        exercise = exercise_service_db.get_problems_and_goals(exercise_id)
        return exercise

    def get_problem_analysis(self, exercise_id: uuid.UUID, access_token: str):
        token_data = check_token(access_token)

        exercise = exercise_service_db.get_problem_analysis(exercise_id)
        return exercise

    def get_testing_beliefs(self, exercise_id: uuid.UUID, access_token: str):
        token_data = check_token(access_token)

        exercise = exercise_service_db.get_testing_beliefs(exercise_id)
        return exercise

    def get_belief_analysis(self, exercise_id: uuid.UUID, access_token: str):
        token_data = check_token(access_token)

        exercise = exercise_service_db.get_belief_analysis(exercise_id)
        return exercise


    def get_all_exercises(self, access_token: str):
        token_data = check_token(access_token)

        exercises = exercise_service_db.get_all_exercises()
        return exercises

    def get_exercise_res(self, exercise_id: str, access_token):
        token_data = check_token(access_token)
        user_id = token_data["user_id"]
        exercise = exercise_service_db.get_exercise_results(exercise_id, user_id)

        if exercise == -1:
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

        return exercise

    def get_completed_exercise_res(self, completed_exercise_id: str, access_token):
        token_data = check_token(access_token)
        user_id = token_data["user_id"]
        exercise = exercise_service_db.get_completed_exercise_results(completed_exercise_id, user_id)

        if exercise == -1:
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")
        return exercise

    def delete_exercise_result(self, completed_exercise_id: str, access_token):
        token_data = check_token(access_token)
        user_id = token_data["user_id"]
        exercise = exercise_service_db.delete_exercise_result(completed_exercise_id, user_id)

        if exercise == -1:
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")
        else: print("Выполненное упражнение успешно удалено")
        return exercise

    def edit_exercise_result(self, payload: EditExerciseResult, access_token):
        token_data = check_token(access_token)
        user_id = token_data["user_id"]
        exercise = exercise_service_db.edit_exercise_result(payload.completed_exercise_id, payload.result, user_id)

        if exercise == -1:
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")
        else:
            return {"status": "OK"}

    def get_exercise(self, exercise_id: uuid.UUID, access_token: str):
        token_data = check_token(access_token)

        exercise = exercise_service_db.get_exercise(exercise_id)
        return exercise

    def save_exercise_result(self, payload: SaveExerciseResult, access_token):
        token_data = check_token(access_token)
        try:
            result = exercise_service_db.save_exercise_result_db(token_data['user_id'],
                                                                     payload.exercise_structure_id,
                                                                     payload.result)
            daily_task_service_db.auto_complete_daily_task(token_data['user_id'], payload.exercise_structure_id)
            return
        except(Error):
            return "error"


exercise_service: ExerciseService = ExerciseService()
