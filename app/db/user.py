from typing import Optional

from beanie import PydanticObjectId
from fastapi import Depends, Request
from fastapi_users import BaseUserManager
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase, ObjectIDIDMixin
from models import UserModel


class UserDoc(BeanieBaseUser[PydanticObjectId], UserModel):
    class Settings(BeanieBaseUser.Settings):
        name = "user"


class UserManager(ObjectIDIDMixin, BaseUserManager[UserDoc, PydanticObjectId]):
    async def on_after_register(self, user: UserDoc, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: UserDoc, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: UserDoc, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_db():
    yield BeanieUserDatabase(UserDoc)


async def get_user_manager(user_db: BeanieUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
