from auth import auth_backend, fastapi_users
from db.user import UserDoc
from dependencies import current_active_admin, current_active_user
from fastapi import APIRouter, Depends
from models import UserCreate, UserRead

router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["users"]
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["users"],
)


@router.get("/user", response_model=UserRead, tags=["users"])
async def get_active_user(user: UserDoc = Depends(current_active_user)):
    return user
