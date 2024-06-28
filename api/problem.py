from schemas.problem import AddProblem, ProblemAnalysisCreate
from services.problem import problem_service
from fastapi import Cookie, APIRouter

router = APIRouter()

@router.post(
    "/problem/new_problem",
    tags=["Problem"],
    response_model=None,
)
def add_problem(data: AddProblem, access_token: str = Cookie(None)):
    return problem_service.add_problem(data, access_token)

@router.post(
    "/problem/save_problem_analysis",
    tags=["Problem"],
    response_model=None,
)
def save_problem_analysis(data: ProblemAnalysisCreate, access_token: str = Cookie(None)):
    return problem_service.save_problem_analysis(data, access_token)

@router.get(
    "/problem/get_analysis/{problem_id}",
    tags=["Problem"],
    response_model=None,
)
def get_analysis(problem_id: str, access_token: str = Cookie(None)):
    return problem_service.get_problem_analysis(problem_id, access_token)

@router.get(
    "/problem/get_all_problems/{user_id}",
    tags=["Problem"],
    response_model=None,
)
def get_all_problems(user_id: str, access_token: str = Cookie(None)):
    return problem_service.get_all_problems(user_id, access_token)