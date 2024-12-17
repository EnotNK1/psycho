from fastapi import APIRouter

from api.web_socket import router as web_socket
from api.users import router as user_router
from api.items import router as item_router
from api.test import router as test_router
from api.application import router as application_router
from api.tegs import router as tegs_router
from api.belief import router as belief_router
from api.dialog import router as dialog_router
from api.problem import router as problem_router
from api.psychologist import router as psychologist_router
from api.diary import router as diary_router
from api.client import router as client_router
from api.manager import router as manager_router
from api.mood_tracker import router as mood_tracker_router
from api.educational_material import router as educational_material_router
from api.review import router as review_router
from api.exercise import router as exercise_router
from api.daily_task import router as daily_task_router
from api.user_statistics import router as user_statistics_router

router = APIRouter()

router.include_router(user_router)
router.include_router(item_router)
router.include_router(test_router)
router.include_router(application_router)
router.include_router(tegs_router)
router.include_router(belief_router)
router.include_router(dialog_router)
router.include_router(problem_router)
router.include_router(psychologist_router)
router.include_router(diary_router)
router.include_router(client_router)
router.include_router(manager_router)
router.include_router(mood_tracker_router)
router.include_router(educational_material_router)
router.include_router(review_router)
router.include_router(exercise_router)
router.include_router(daily_task_router)
router.include_router(user_statistics_router)
router.include_router(web_socket)