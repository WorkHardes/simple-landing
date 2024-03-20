from src.api.mail.shemas import MailToSend


class CreateMailInteractor:
    async def execute(self, body: MailToSend) -> None:
        pass
