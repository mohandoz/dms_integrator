from beanie import PydanticObjectId
from fastapi_users import schemas
from fastapi_users.db import BaseOAuthAccount
from pydantic import BaseModel, Field


class OAuthAccount(BaseOAuthAccount):
    pass


class UserModel(BaseModel):
    oauth_accounts: list[OAuthAccount] = Field(default_factory=list)


class UserRead(schemas.BaseUser[PydanticObjectId]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
