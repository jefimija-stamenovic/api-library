from pydantic import BaseModel, Field, ConfigDict
from datetime import date 
from typing import Optional

class SchemaBookBase(BaseModel): 
    title : str  = Field(..., min_length=1)
    description: Optional[str] = Field(None, max_length=2000)
    publication_date: Optional[date] = Field(None)
    isbn : str = Field(..., min_length=10, max_length=20)
    available: bool = Field(...)
    author_id: int = Field(..., gt=0)

    model_config = ConfigDict(from_attributes=True)

class SchemaBook(SchemaBookBase): 
    id: int = Field(..., gt=0)
