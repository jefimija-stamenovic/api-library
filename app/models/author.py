from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from core.db import Base 

class Author(Base) :
    __tablename__: str = "authors"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), nullable=False, index=True)
    last_name = Column(String(50), nullable=False, index=True)
    biography = Column(Text, nullable=True)

    books = relationship("Book", back_populates="author")