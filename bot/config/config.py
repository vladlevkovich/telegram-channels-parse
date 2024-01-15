from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class Setting(BaseSettings):
    TOKEN_BOT: str = os.getenv('TOKEN_BOT')
    DB_URL: str = os.getenv('DB_URL')
    REDIS_HOST: str = os.getenv('REDIS_HOST')
    REDIS_PORT: int = os.getenv('REDIS_PORT')
    API_ID: int = os.getenv('API_ID')
    API_HASH: str = os.getenv('API_HASH')
    CHAT_ID: str = os.getenv('CHAT_ID')


settings = Setting()
