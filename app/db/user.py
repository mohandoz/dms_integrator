from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser
from models import UserModel


class UserDoc(BeanieBaseUser[PydanticObjectId], UserModel):
    class Settings(BeanieBaseUser.Settings):
        name = "user"

async def get_user_db():
    yield BeanieUserDatabase(UserDoc)
