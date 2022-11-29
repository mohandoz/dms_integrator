from fastapi import APIRouter

from .endpoints import user_router

router = APIRouter()
router.include_router(user_router, tags=["users"], prefix="/v1")
