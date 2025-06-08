import os
from typing import Optional

from sqlalchemy import create_engine, text, Engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, AsyncEngine

from alembic.config import Config
from alembic import command

from core.config import Settings

Base = declarative_base()

class Database:
    _engine: Optional[Engine] = None
    _db_url: Optional[URL] = None
    _sessionmaker: Optional[sessionmaker] = None

    _async_engine: Optional[AsyncEngine] = None 
    _async_sessionmaker : Optional[async_sessionmaker] = None 

    @classmethod
    def init(cls, settings: Settings) -> None:
        tmp_db_url: URL = URL.create(
            drivername=settings.DB_DRIVER,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            username=settings.DB_USER,
            password=settings.DB_PASSWORD
        )
        tmp_engine: Engine = create_engine(tmp_db_url)
        try:
            with tmp_engine.connect() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME}"))
                print(f"**LOG** => Database {settings.DB_NAME} is successfully created/checked")
        except Exception as e:
            print(f"**LOG** => ERROR => Error while creating database => {str(e)}")
        finally:
            tmp_engine.dispose()

        cls._db_url = URL.create(
            drivername=settings.DB_DRIVER,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            username=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME
        )
        cls._engine = create_engine(cls._db_url)

        async_url: str = f"mysql+aiomysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        cls._async_engine = create_async_engine(async_url)

        cls._sessionmaker = sessionmaker(bind=cls._engine, autocommit=False, autoflush=False)
        cls._async_sessionmaker = async_sessionmaker(bind=cls._async_engine, autoflush=False, autocommit=False)

        print("LOG ** => 🔧 Engine & sessionmaker are initialized!")
        cls.__auto_migrate()

    @classmethod
    def get_engine(cls) -> Engine:
        if cls._engine is None:
            raise RuntimeError("Database is not initialized. Call Database.init(settings) first.")
        return cls._engine

    @classmethod
    def get_session(cls) -> Session: 
        if cls._sessionmaker is None:
            raise RuntimeError("Sessionmaker is not initialized. Call Database.init(settings) first.")
        return cls._sessionmaker()
    
    @classmethod
    def get_session_async(cls) -> AsyncSession: 
        if cls._async_sessionmaker is None:
            raise RuntimeError("Async Sessionmaker is not initialized. Call Database.init(settings) first.")
        return cls._async_sessionmaker()

    @classmethod
    def __auto_migrate(cls) -> None:
        try:
            alembic_config_file = os.path.join(os.path.dirname(__file__), '..', '..', 'alembic.ini')
            alembic_cfg = Config(alembic_config_file)
            command.upgrade(alembic_cfg, "head")
            print("**LOG** => Migration are successfully applied")
        except Exception as e:
            print(f"**LOG** => ERROR => Error while applying migration => {str(e)}")
