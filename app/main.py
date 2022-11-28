import uvicorn
from api.api_v1.api import router as api_router_v1
from fastapi import FastAPI


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router_v1)
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)
