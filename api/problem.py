from schemas.problem import AddProblem, ProblemAnalysisCreate, ProblemAnalysisGet
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

@router.post(
    "/problem/get_analysis",
    tags=["Problem"],
    response_model=None,
)
def get_analysis(data: ProblemAnalysisGet, access_token: str = Cookie(None)):
    return problem_service.get_problem_analysis(data, access_token)