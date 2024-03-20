from functools import cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # server
    DEBUG: bool
    LOGGER_CONFIG_FILE_PATH: str

    # mail
    MAIL_HOST: str
    MAIL_PORT: int
    MAIL_USERNAME: str
    MAIL_PASSWORD: str


@cache
def get_settings():
    return Settings()


settings = get_settings()
