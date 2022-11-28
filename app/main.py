import uvicorn
from api.api_v1.api import router as api_router_v1
from fastapi import FastAPI
from project.settings import settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, debug=settings.DEBUG, version=settings.VERSION
    )
    application.include_router(
        api_router_v1,
        prefix=settings.API_PREFIX,
    )
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=settings.DEBUG)
