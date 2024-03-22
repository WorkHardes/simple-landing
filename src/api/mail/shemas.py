from pydantic import BaseModel


class MailToSend(BaseModel):
    formwork_type: str
    total_area: str
    address: str
    customer_name: str
    customer_phone_number: str
    customer_email: str
