from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os, sys

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


ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'env')
if "--test" in sys.argv: 
    ENV_PATH = os.path.join(ENV_PATH, 'test.env')
else: 
    ENV_PATH = os.path.join(ENV_PATH, 'prod.env')
print(ENV_PATH)

load_dotenv(dotenv_path=ENV_PATH)
settings = Settings(APP_HOST = os.environ.get("APP_HOST"), 
                    APP_PORT = int(os.environ.get("APP_PORT")), 
                    DB_HOST = os.environ.get("DB_HOST"), 
                    DB_PORT = int(os.environ.get("DB_PORT")), 
                    DB_USER = os.environ.get("DB_USER"), 
                    DB_PASSWORD = os.environ.get("DB_PASSWORD"), 
                    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY"), 
                    ALGORITHM = os.environ.get("ALGORITHM"), 
                    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")))