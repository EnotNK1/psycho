import uuid

from fastapi import APIRouter, Cookie

from schemas.daily_tasks import DailyTaskId
from services.daily_task import daily_task_service
from typing import List

router = APIRouter()

@router.get(
    "/daily_tasks",
    tags=["Daily_task"],
    description="у всех упражнений destination_id=b3f24ecc-d39e-46a3-b67b-4503f9f34506 фальшивый, не пользуйтесь им"
)
def get_daily_tasks(access_token: str = Cookie(None)):
    return daily_task_service.get_daily_tasks(access_token)

@router.patch(
    "/daily_tasks",
    tags=["Daily_task"],
)
def complete_daily_task(data: DailyTaskId, access_token: str = Cookie(None)):
    return daily_task_service.complete_daily_tasks(data, access_token)

# @router.post(
#     "/daily_tasks",
#     tags=["Daily_task"],
# )
# def complete_daily_task():
#     return daily_task_service.change_daily_tasks()