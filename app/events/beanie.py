from beanie import init_beanie
from db import db


async def init_db():
    await init_beanie(
        database=db,
        document_models=[],
    )
