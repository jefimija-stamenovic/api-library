from pydantic import BaseModel, field_validator, Field
from typing import Optional
import re

class AuthorCreate(BaseModel):
    first_name : str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    biography: Optional[str] = Field()

    @field_validator("first_name", "last_name")
    def validate_name(cls, value: str) -> str:
        pattern = r"^[A-Za-zČĆŽŠĐčćžšđ\s\-]+$"
        if not re.match(pattern, value):
            raise ValueError("Name must contain only letters, spaces, or hyphens.")
        return value