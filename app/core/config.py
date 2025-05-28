from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
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

    class Config: 
        env_file: str = ".env"
        case_sensitive: bool = True

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'env', 'prod.env')
print(f"Loading .env from: {ENV_PATH}")
load_dotenv(dotenv_path=ENV_PATH)
print("APP_HOST =", os.environ.get("APP_HOST"))
settings = Settings(APP_HOST = os.environ.get("APP_HOST"), 
                    APP_PORT = int(os.environ.get("APP_PORT")))