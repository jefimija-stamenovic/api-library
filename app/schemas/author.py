from pydantic import BaseModel, field_validator, Field, ConfigDict
from app.schemas.book import SchemaBook
from typing import Optional, List
import re

class SchemaAuthorBase(BaseModel):
    first_name : str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    biography: Optional[str] = Field(default=None)

    @field_validator("first_name", "last_name")
    def validate_name(cls, value: str) -> str:
        pattern = r"^[A-Za-zČĆŽŠĐčćžšđ\s\-]+$"
        if not re.match(pattern, value):
            raise ValueError("Name must contain only letters, spaces, or hyphens.")
        return value
    
    model_config: ConfigDict = ConfigDict(from_attributes=True)

class SchemaAuthorUpdate(SchemaAuthorBase): 
    books: List[SchemaBook] = Field(default_factory=list)

class SchemaAuthor(SchemaAuthorUpdate): 
    id: int = Field(gt=0)