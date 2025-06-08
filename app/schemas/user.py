from pydantic import BaseModel, EmailStr, field_validator, Field, ConfigDict
from typing import Any
import re

class SchemaToken(BaseModel): 
    access_token: str = Field()
    refresh_token: str = Field()

class SchemaCredentials(BaseModel): 
    username: str = Field(min_length=4, max_length=20, description="Username")
    password: str = Field(min_length=8, description="Password")

class SchemaUserRegister(SchemaCredentials):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    first_name: str = Field(min_length=2, max_length=50, description="First name of user")
    last_name: str = Field(min_length=2, max_length=50, description="Last name of user")
    email : EmailStr = Field(description="Email of user")
    is_admin: bool = Field(False, description="Is user administrator?")

    @field_validator("first_name", "last_name")
    def validate_name(cls, value: str) -> str:
        pattern = r"^[A-Za-zČĆŽŠĐčćžšđ\s\-]+$"
        if not re.match(pattern, value):
            raise ValueError("Name must contain only letters, spaces, or hyphens.")
        return value
    
    @field_validator("username")
    def validate_username(cls, value: str)-> str:
        if not re.match(r'^[a-zA-Z0-9_\.]+$', value):
            raise ValueError("Username can only contain letters, digits, and underscores.")
        return value
    
    @field_validator("password")
    def validate_password(cls, value: str) -> str: 
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).*$'
        if not re.match(pattern, value):
            raise ValueError("Password must be at least 8 characters long, and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return value
    
class SchemaUser(SchemaUserRegister): 
    id: int = Field(gt=0)