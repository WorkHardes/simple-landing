from functools import cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # server
    DEBUG: bool

    # mail
    MAIL_HOST: str
    MAIL_PORT: int
    MAIL_USERNAME: str
    MAIL_PASSWORD: str


@cache
def get_settings():
    return Settings()


settings = get_settings()
