import smtplib
from email.header import Header
from email.mime.text import MIMEText

from src.api.mail.shemas import MailToSend
from src.core.logger import logger
from src.core.settings import settings

smtp_client = smtplib.SMTP(settings.MAIL_HOST, settings.MAIL_PORT)


def _get_msg(mail_to_send: MailToSend) -> MIMEText:
    text = (
        "Данные заказчика\n"
        f"имя: {mail_to_send.customer_name}\n"
        f"номер телефона: {mail_to_send.customer_phone_number}\n"
        f"почта: {mail_to_send.customer_email}"
        f"тип опалубки: {mail_to_send.formwork_type}\n"
        f"общая площадь: {mail_to_send.total_area}\n"
        f"адрес: {mail_to_send.address}"
    )

    msg = MIMEText(text, "plain", "utf-8")
    msg["Subject"] = Header("Заказ опалубки", "utf-8")
    msg["From"] = settings.MAIL_USERNAME
    msg["To"] = settings.MAIL_USERNAME

    return msg


def send_mail(mail_to_send: MailToSend) -> None:
    msg = _get_msg(mail_to_send)
    try:
        smtp_client.sendmail(
            from_addr=msg["From"],
            to_addrs=settings.MAIL_USERNAME,
            msg=msg.as_string(),
        )
    except Exception as e:
        logger.error(
            f"Error send mail to {msg['From']}. Detail: {e!r}",
        )
        return
    logger.info(f"The mail to {msg['From']} sent successfully")
