from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from src.api.mail.router import router as mail_router
from src.core.exception_handlers import http422_error_handler, http_error_handler
from src.core.settings import settings


def create_app() -> FastAPI:
    app = FastAPI(
        debug=settings.DEBUG,
        title="MSF web API",
        description="Rest API for simple landing",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    api_prefix = "/api/v1"
    app.include_router(mail_router, prefix=api_prefix)

    app.add_exception_handler(HTTPException, http_error_handler)
    app.add_exception_handler(RequestValidationError, http422_error_handler)

    return app


app = create_app()


@app.get("/ping", status_code=status.HTTP_200_OK, tags=["healthcheck"])
def ping() -> str:
    return "pong"
