from pydantic import BaseModel


class ErrorMessage(BaseModel):
    code: int
    detail: str
