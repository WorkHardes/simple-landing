import smtplib

from src.core.logger import logger
from src.core.settings import settings

smtp_client = smtplib.SMTP(settings.MAIL_HOST, settings.MAIL_PORT)


def send_mail(email: str, msg: str) -> None:
    try:
        smtp_client.sendmail(from_addr=settings.MAIL_USERNAME, to_addrs=email, msg=msg)
    except Exception as e:
        logger.error(
            f"Error send mail to {email}. Detail: {e!r}",
        )
        return
    logger.info(f"The mail to {email} sent successfully")
