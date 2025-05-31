from app.core.config import Settings
from sqlalchemy import create_engine, text, Engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base

from alembic.config import Config
from alembic import command
import os

Base = declarative_base()

class Database: 
    def __init__(self, settings: Settings) -> None: 
        super().__init__()
        self.__create_db_if_not_exists(settings)
        self.__auto_migrate()

    def __create_db_if_not_exists(self, settings: Settings) -> None: 
        db_url : URL = URL.create(
            drivername=settings.DB_DRIVER, 
            host=settings.DB_HOST, 
            port=settings.DB_PORT, 
            username=settings.DB_USER, 
            password=settings.DB_PASSWORD
        )
        print("**LOG** => DB_URL: ", db_url)
        try: 
            engine: Engine = create_engine(db_url)
            with engine.connect() as conn: 
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME}"))
                print(f"Baza {settings.DB_NAME} je uspešno kreirana/proverena. ")
        except Exception as e: 
            print(f"**LOG** => ERROR => Došlo je do greške prilikom povezivanja na MySQL server => {str(e)}")

    def __auto_migrate(self) -> None: 
        alembic_config_file : str = os.path.join(os.path.dirname(__file__), '..', '..','alembic.ini')
        alembic_cfg = Config(alembic_config_file)
        command.upgrade(alembic_cfg, "head")
        print("**LOG** => Migracije su primenjene do najnovije verzije.")