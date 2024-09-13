from database.services.users import user_service_db
from database.services.problem import problem_service_db
from schemas.problem import ProblemAnalysisCreate, AddProblem
import uuid
from psycopg2 import Error
from utils.token_utils import check_token



class ProblemService:

    def add_problem(self, payload: AddProblem, access_token):
        token_data = check_token(access_token)

        try:
            problem_service_db.add_problem_db(token_data['user_id'], payload.description, payload.goal)
            return "Successfully"
        except(Error):
            return "error"

    def save_problem_analysis(self, payload: ProblemAnalysisCreate, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 1 or role == 2 or role == 3:
            problem_service_db.save_problem_analysis_db(uuid.UUID(payload.problem_id), payload.type)
            return "Successfully"
        else:
            return "access denied"

    def get_problem_analysis(self, problem_id: str, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 1 or role == 2 or role == 3:
            result = problem_service_db.get_problem_analysis_db(uuid.UUID(problem_id))
            return result
        else:
            return "access denied"

    def get_all_problems(self, user_id: str, access_token):
        token_data = check_token(access_token)

        result = problem_service_db.get_all_problems(uuid.UUID(user_id))
        return result


problem_service: ProblemService = ProblemService()