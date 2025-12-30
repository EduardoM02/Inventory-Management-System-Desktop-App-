import os
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class Settings(BaseSettings):
    PORT: int
    HOST: str
    DATABASE: str
    USER: str
    PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, '.env'),
        env_file_encoding="utf-8",
        env_prefix="DB_"
    )

config = Settings()
print("ENV LOADED:", Settings().model_dump())