from .home import router as home_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(home_router)