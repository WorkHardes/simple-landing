from fastapi import HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import ORJSONResponse

from src.schemas import ErrorMessage


async def http_error_handler(_: Request, exc: HTTPException) -> ORJSONResponse:
    return ORJSONResponse(
        content=ErrorMessage(
            code=exc.status_code,
            detail=str(exc.detail),
        ).model_dump_json(),
        status_code=exc.status_code,
    )


async def http422_error_handler(
    _: Request,
    req: RequestValidationError,
) -> ORJSONResponse:
    detail = "validation error; "
    for err in req.errors():
        loc = err.get("loc")
        if loc is None:
            continue
        detail += f"loc: {loc}; "
        msg = err.get("msg")
        if msg is None:
            continue
        detail += f"detail: {msg}; "
    return ORJSONResponse(
        content=ErrorMessage(
            code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail[:-2],
        ).model_dump_json(),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )
