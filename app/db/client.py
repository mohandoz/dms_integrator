import motor.motor_asyncio
from project.settings import settings

DATABASE_URL = settings.MONGODB_URL

client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL,
    minPoolSize=settings.MIN_CONNECTIONS_COUNT,
    maxPoolSize=settings.MAX_CONNECTIONS_COUNT,
    uuidRepresentation="standard",
)
db = client[settings.MONGODB_NAME]
