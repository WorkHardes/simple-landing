from src.api.mail.interactor import CreateMailInteractor


def get_send_mail_interactor() -> CreateMailInteractor:
    return CreateMailInteractor()
