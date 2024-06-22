from schemas.problem import CreateDeepConviction, BeliefAnalysis, CheckBelief
from services.belief import belief_service

from fastapi import Cookie, APIRouter

router = APIRouter()


@router.post(
    "/belief/create_deep_conviction",
    tags=["Belief"],
    response_model=None,
)
def create_deep_conviction(data: CreateDeepConviction, access_token: str = Cookie(None)):
    return belief_service.create_deep_conviction(data, access_token)



@router.post(
    "/belief/save_belief_analysis",
    tags=["Belief"],
    response_model=None,
)
def save_belief_analysis(data: BeliefAnalysis, access_token: str = Cookie(None)):
    return belief_service.save_belief_analysis(data, access_token)

@router.post(
    "/belief/save_belief_check",
    tags=["Belief"],
    response_model=None,
)
def save_belief_check(data: CheckBelief, access_token: str = Cookie(None)):
    return belief_service.save_belief_check(data, access_token)
@router.get(
    "/belief/get_belief_analysis/{intermediate_conviction_id}",
    tags=["Belief"],
    response_model=None,
)
def get_belief_analysis(intermediate_conviction_id: str, access_token: str = Cookie(None)):
    return belief_service.get_belief_analysis(intermediate_conviction_id, access_token)

@router.get(
    "/belief/get_belief_check/{intermediate_conviction_id}",
    tags=["Belief"],
    response_model=None,
)
def get_belief_check(intermediate_conviction_id: str, access_token: str = Cookie(None)):
    return belief_service.get_belief_check(intermediate_conviction_id, access_token)