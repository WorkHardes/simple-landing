from pydantic import BaseModel


class MailToSend(BaseModel):
    text: str
