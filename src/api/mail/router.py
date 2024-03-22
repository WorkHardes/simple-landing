from fastapi import APIRouter, status

from src.api.mail.shemas import MailToSend
from src.api.mail.use_cases import send_mail
from src.schemas import ErrorMessage

router = APIRouter(tags=["mail"])


@router.post(
    "/mail",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorMessage},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorMessage},
    },
)
def add_account_telegram(mail_to_send: MailToSend) -> None | ErrorMessage:
    send_mail(mail_to_send)
