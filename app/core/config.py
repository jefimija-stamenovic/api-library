from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os, sys
from core.constants import *

class Settings(BaseSettings):
    DB_DRIVER: str
    APP_HOST: str
    APP_PORT : int 
    DB_HOST: str
    DB_PORT: int 
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str 

    JWT_SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    class Config: 
        env_file: str = ".env"
        case_sensitive: bool = True


ENV_PATH: str = os.path.join(os.path.dirname(__file__), '..', 'env')

ENV_PATH = os.path.join(ENV_PATH, 'prod.env') if "--prod" in sys.argv else os.path.join(ENV_PATH, 'test.env')
print(ENV_PATH)
load_dotenv(dotenv_path=ENV_PATH)
settings = Settings(DB_DRIVER=os.environ.get("DB_DRIVER", cDB_DRIVER.value), 
                    APP_HOST = os.environ.get("APP_HOST", cAPP_HOST.value), 
                    APP_PORT = int(os.environ.get("APP_PORT", cAPP_PORT.value)), 
                    DB_NAME = os.environ.get("DB_NAME", cDB_NAME.value), 
                    DB_HOST = os.environ.get("DB_HOST", cDB_HOST.value), 
                    DB_PORT = int(os.environ.get("DB_PORT", cDB_PORT.value)), 
                    DB_USER = os.environ.get("DB_USER", cDB_USER.value), 
                    DB_PASSWORD = os.environ.get("DB_PASSWORD", cDB_PASSWORD.value), 
                    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", cJWT_SECRET_KEY.value), 
                    ALGORITHM = os.environ.get("ALGORITHM", cALGORITHM.value), 
                    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", cACCESS_TOKEN_EXPIRE_MINUTES.value)), 
                    REFRESH_TOKEN_EXPIRE_DAYS = int(os.environ.get("REFRESH_TOKEN_EXPIRE_DAYS", cREFRESH_TOKEN_EXPIRE_DAYS.value)))