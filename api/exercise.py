import shutil
import uuid

from fastapi import APIRouter, Cookie, Depends, UploadFile, File, HTTPException
from schemas.exercise import DefiningProblemGroups, ProblemAnalysis, ProblemsAndGoals, TestingBeliefs, BeliefAnalysis, \
    ResponseGetExerciseResult, ResponseGetDetailExerciseResult, EditExerciseResult, SaveExerciseResult
from services.exercise import exercise_service
# from database.models.exercise import Filled_field
from database.services.exercise import exercise_service_db
from services.review import review_service
from starlette.responses import JSONResponse, Response, FileResponse
from typing import List, Optional
from utils.token_utils import check_token

router = APIRouter()

@router.get(
    "/exercise/all",
    tags=["Exercise"],
    response_model=None,
)
def get_all(access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercises = exercise_service_db.get_all(
        user_id)
    return exercises


@router.get(
    "/defining_problem_groups/get_all_by_user",
    tags=["Exercise"],
    response_model=None,
)
def get_all_dpg_by_user(access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercises = exercise_service_db.get_all_defining_problem_groups_by_user(
        user_id)
    return exercises


@router.get(
    "/defining_problem_groups/get_exercise",
    tags=["Exercise"],
    response_model=None,
)
def get_dpg(exercise_id: uuid.UUID, access_token: str = Cookie(None)):
    return exercise_service.get_defining_problem_groups(exercise_id, access_token)


@router.post(
    "/defining_problem_groups/save_exercise_result",
    tags=["Exercise"],
    response_model=None,
)
def save_dpg(data: DefiningProblemGroups, access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercise_id = exercise_service_db.save_defining_problem_groups(
        user_id=user_id,
        field_1=data.sphere,
        field_2=data.emotion,
        field_3=data.target
    )

    if exercise_id:
        return {"message": "Exercise saved successfully", "exercise_id": exercise_id}
    else:
        raise HTTPException(status_code=500, detail="Failed to save exercise")


@router.get(
    "/problems_and_goals/get_all_by_user",
    tags=["Exercise"],
    response_model=None,
)
def get_all_pag_by_user(access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercises = exercise_service_db.get_all_problems_and_goals_by_user(user_id)
    return exercises


@router.get(
    "/problems_and_goals/get_exercise",
    tags=["Exercise"],
    response_model=None,
)
def get_pag(exercise_id: uuid.UUID, access_token: str = Cookie(None)):
    return exercise_service.get_problems_and_goals(exercise_id, access_token)


@router.post(
    "/problems_and_goals/save_exercise_result",
    tags=["Exercise"],
    response_model=None,
)
def save_pag(data: ProblemsAndGoals, access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercise_id = exercise_service_db.save_problems_and_goals(
        user_id=user_id,
        field_1=data.sphere,
        field_2=data.emotion,
        field_3=data.event,
        field_4=data.argument,
        field_5=data.target
    )

    if exercise_id:
        return {"message": "Exercise saved successfully", "exercise_id": exercise_id}
    else:
        raise HTTPException(status_code=500, detail="Failed to save exercise")


@router.get(
    "/problem_analysis/get_all_by_user",
    tags=["Exercise"],
    response_model=None,
)
def get_all_pa_by_user(access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercises = exercise_service_db.get_all_problem_analysis_by_user(user_id)
    return exercises


@router.get(
    "/problem_analysis/get_exercise",
    tags=["Exercise"],
    response_model=None,
)
def get_pa(exercise_id: uuid.UUID, access_token: str = Cookie(None)):
    return exercise_service.get_problem_analysis(exercise_id, access_token)


@router.post(
    "/problem_analysis/save_exercise_result",
    tags=["Exercise"],
    response_model=None,
)
def save_pa(data: ProblemAnalysis, access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercise_id = exercise_service_db.save_problem_analysis(
        user_id=user_id,
        field_1=data.problem,
        field_2=data.target,
        field_3=data.elaboration,
        field_4=data.belief
    )

    if exercise_id:
        return {"message": "Exercise saved successfully", "exercise_id": exercise_id}
    else:
        raise HTTPException(status_code=500, detail="Failed to save exercise")


@router.get(
    "/testing_beliefs/get_all_by_user",
    tags=["Exercise"],
    response_model=None,
)
def get_all_tb_by_user(access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercises = exercise_service_db.get_all_testing_beliefs_by_user(user_id)
    return exercises


@router.get(
    "/testing_beliefs/get_exercise",
    tags=["Exercise"],
    response_model=None,
)
def get_tb(exercise_id: uuid.UUID, access_token: str = Cookie(None)):
    return exercise_service.get_testing_beliefs(exercise_id, access_token)


@router.post(
    "/testing_beliefs/save_exercise_result",
    tags=["Exercise"],
    response_model=None,
)
def save_tb(data: TestingBeliefs, access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercise_id = exercise_service_db.save_testing_beliefs(
        user_id=user_id,
        field_1=data.truthfulness_dogmatic,
        field_2=data.logic_dogmatic,
        field_3=data.utility_dogmatic,
        field_4=data.truthfulness_flexible,
        field_5=data.logic_flexible,
        field_6=data.utility_flexible
    )

    if exercise_id:
        return {"message": "Exercise saved successfully", "exercise_id": exercise_id}
    else:
        raise HTTPException(status_code=500, detail="Failed to save exercise")


@router.get(
    "/belief_analysis/get_all_by_user",
    tags=["Exercise"],
    response_model=None,
)
def get_all_ba_by_user(access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercises = exercise_service_db.get_all_belief_analysis_by_user(user_id)
    return exercises


@router.get(
    "/belief_analysis/get_exercise",
    tags=["Exercise"],
    response_model=None,
)
def get_ba(exercise_id: uuid.UUID, access_token: str = Cookie(None)):
    return exercise_service.get_belief_analysis(exercise_id, access_token)


@router.post(
    "/belief_analysis/save_exercise_result",
    tags=["Exercise"],
    response_model=None,
)
def save_ba(data: BeliefAnalysis, access_token: str = Cookie(None)):
    token_data = check_token(access_token)
    user_id = token_data["user_id"]

    exercise_id = exercise_service_db.save_belief_analysis(
        user_id=user_id,
        field_1=data.action_dogmatic,
        field_2=data.interference_dogmatic,
        field_3=data.results_dogmatic,
        field_4=data.action_flexible,
        field_5=data.interference_flexible,
        field_6=data.results_flexible
    )

    if exercise_id:
        return {"message": "Exercise saved successfully", "exercise_id": exercise_id}
    else:
        raise HTTPException(status_code=500, detail="Failed to save exercise")


@router.post(
    "/exercise/upload/images_exercise",
    tags=["Exercise"],
    response_model=None,
)
def upload_image(file: UploadFile = File(...)):
    with open(f"database/images_exercise/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}


@router.get(
    "/exercise/images_exercise/{filename}",
    tags=["Exercise"],
    response_model=None,
)
def get_images(filename: str, access_token: str = Cookie(None)):
    return FileResponse(f"database/images_exercise/{filename}")


@router.get(
    "/exercise/get_all_exercises",
    tags=["Exercise"],
    response_model=None,
)
def get_all_exercises(access_token: str = Cookie(None)):
    return exercise_service.get_all_exercises(access_token)


@router.get(
     "/exercise/get_exercise",
     tags=["Exercise"],
     response_model=None,
)
def get_exercise(exercise_id: uuid.UUID, access_token: str = Cookie(None)):
     return exercise_service.get_exercise(exercise_id, access_token)


@router.post(
     "/exercise/save_exercise_result",
     tags=["Exercise"],
     response_model=None,
)
def save_test_result(data: SaveExerciseResult, access_token: str = Cookie(None)):
     return exercise_service.save_exercise_result(data, access_token)


@router.get(
    "/exercise/get_exercise_results/{exercise_id}",
    tags=["Exercise"],
    response_model=List[ResponseGetExerciseResult],
)
def get_exercise_results(exercise_id: str, access_token: str = Cookie(None)):
    return exercise_service.get_exercise_res(exercise_id, access_token)


@router.get(
    "/exercise/get_exercise_result/{completed_exercise_id}",
    tags=["Exercise"],
    response_model=ResponseGetDetailExerciseResult,
)
def get_exercise_results(completed_exercise_id: str, access_token: str = Cookie(None)):
    return exercise_service.get_completed_exercise_res(completed_exercise_id, access_token)


@router.delete(
    "/exercise/delete_exercise_result/{completed_exercise_id}",
    tags=["Exercise"],
    response_model=None,
)
def delete_exercise_result(completed_exercise_id: str, access_token: str = Cookie(None)):
    return exercise_service.delete_exercise_result(completed_exercise_id, access_token)


@router.patch(
    "/exercise/edit_exercise_result",
    tags=["Exercise"],
    response_model=None,
)
def edit_exercise_result(data: EditExerciseResult, access_token: str = Cookie(None)):
    return exercise_service.edit_exercise_result(data, access_token)

# @router.patch(
#     "/review/read/{review_id}",
#     tags=["Review"],
#     response_model=str,
# )
# def mark_review_as_read(review_id: uuid.UUID, access_token: str = Cookie(None)):
#     return review_service.mark_review_as_read(review_id, access_token)
#
#
# @router.delete(
#     "/review/delete/{review_id}",
#     tags=["Review"],
#     response_model=str,
# )
# def delete_review(review_id: uuid.UUID, access_token: str = Cookie(None)):
#     return review_service.delete_review(review_id, access_token)
