from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api import router
from core.exceptions import CustomException
from core.config import config


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)

def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="FastAPI D'Hondt Seat Allocation",
        description="API REST para calcular la distribución de escaños utilizando el sistema D'Hondt.",
        version=config.RELEASE_VERSION,
        contact={
            "name": "Brian",
            "email": "brianretamar0101@gmail.com",
        },
        license_info={
            "name": "MIT",
        },
        docs_url=None if config.ENVIRONMENT == "production" else "/docs",
        redoc_url=None if config.ENVIRONMENT == "production" else "/redoc",
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    return app_


app = create_app()