from pydantic import BaseModel


class MailToSend(BaseModel):
    email: str
    msg: str
