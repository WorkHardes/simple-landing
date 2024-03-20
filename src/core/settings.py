from functools import cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False


@cache
def get_settings():
    return Settings()


settings = get_settings()
