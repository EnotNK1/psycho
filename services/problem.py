from database.database import database_service
from schemas.problem import ProblemAnalysisGet, ProblemAnalysisCreate, AddProblem
from services.auth import verify_token
import uuid
from psycopg2 import Error



class ProblemService:

    def add_problem(self, payload: AddProblem, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            database_service.add_problem_db(token_data['user_id'], payload.description, payload.goal)
            return "Successfully"
        except(Error):
            return "error"

    def save_problem_analysis(self, payload: ProblemAnalysisCreate, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            database_service.save_problem_analysis_db(uuid.UUID(payload.problem_id), payload.type)
            return "Successfully"
        else:
            return "access denied"

    def get_problem_analysis(self, payload: ProblemAnalysisGet, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            result = database_service.get_problem_analysis_db(payload.problem_id)
            return result
        else:
            return "access denied"


problem_service: ProblemService = ProblemService()