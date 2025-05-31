from sqlalchemy import Column, Integer, String, Boolean
from app.core.db import Base

class User(Base): 
    __tablename__: str ="users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(30), index=True, nullable=False)
    last_name = Column(String(50), index=True, nullable=False)
    email = Column(String(100), index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password_salt = Column(String(50), nullable=False)
    password_hash = Column(String(50), nullable=False)
    is_admin = Column(Boolean, default=False)
    