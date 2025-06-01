from pydantic import BaseModel, Field, ConfigDict, field_validator
import re
from datetime import date 
from typing import Optional

class SchemaBookUpdate(BaseModel):
    id: Optional[int] = Field(None, gt = 0)
    title: Optional[str]  = Field(None, min_length=1)
    description: Optional[str] = Field(None, max_length=2000)
    publication_date: Optional[date] = Field(None)
    isbn: Optional[str] = Field(None, min_length=10, max_length=20)
    available: Optional[bool] = Field(None)
    author_id: Optional[int] = Field(None, gt=0)

    model_config = ConfigDict(from_attributes=True)

    @field_validator("title")
    def validate_title(cls, value: str) -> str:
        pattern = r"^[A-Za-z0-9ČĆŽŠĐčćžšđ\s\-\.,!?\"'()]+$"
        if not re.match(pattern, value):
            raise ValueError("Title may contain letters, numbers, spaces, punctuation, and hyphens only.")
        return value

    @field_validator("isbn")
    def validate_isbn(cls, value: str) -> str:
        pattern = r"^[0-9\-]+$"
        if not re.match(pattern, value):
            raise ValueError("ISBN must contain only digits and hyphens.")
        return value

class SchemaBookBase(BaseModel): 
    title : str  = Field(min_length=1)
    description: Optional[str] = Field(None, max_length=2000)
    publication_date: Optional[date] = Field(None)
    isbn : str = Field(min_length=10, max_length=20)
    available: bool = Field()
    author_id: int = Field(gt=0)

    @field_validator("title")
    def validate_title(cls, value: str) -> str:
        pattern = r"^[A-Za-z0-9ČĆŽŠĐčćžšđ\s\-\.,!?\"'()]+$"
        if not re.match(pattern, value):
            raise ValueError("Title may contain letters, numbers, spaces, punctuation, and hyphens only.")
        return value

    @field_validator("isbn")
    def validate_isbn(cls, value: str) -> str:
        pattern = r"^[0-9\-]+$"
        if not re.match(pattern, value):
            raise ValueError("ISBN must contain only digits and hyphens.")
        return value

    model_config = ConfigDict(from_attributes=True)

class SchemaBook(SchemaBookBase): 
    id: int = Field(gt=0)
