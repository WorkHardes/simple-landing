from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.api.mail.dependencies import get_send_mail_interactor
from src.api.mail.interactor import CreateMailInteractor
from src.api.mail.shemas import MailToSend
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
async def add_account_telegram(
    body: MailToSend,
    interactor: Annotated[CreateMailInteractor, Depends(get_send_mail_interactor)],
) -> None | ErrorMessage:
    await interactor.execute(body)
