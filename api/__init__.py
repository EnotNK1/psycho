from fastapi import APIRouter

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