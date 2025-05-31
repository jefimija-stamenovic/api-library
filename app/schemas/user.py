from pydantic import BaseModel, EmailStr, field_validator 
from typing import Any
import re

class SchemaUserRegister(BaseModel):
    first_name: str 
    last_name: str 
    email : EmailStr 
    username: str  
    password: str
    is_admin: bool

    @field_validator('first_name', 'last_name')
    def validator_name(cls, value) -> Any: 
        if not re.match(r'^[A-Za-zČĆŽŠĐčćžšđ ]{2,50}$', value): 
            raise ValueError("Ime i prezime smeju da sadrže samo slova i da budu dužine između 2 i 50 karaktera")
        return value 
    
    @field_validator("username")
    def validate_username(cls, value)-> Any:
        if not re.match(r'^[a-zA-Z0-9_]{4,20}$', value):
            raise ValueError("Korisničko ime mora biti između 4 i 50 karaktera, a sme sadržati samo slova, brojeve i donju crtu")
        return value
    
    @field_validator("password")
    def validate_password(cls, value) -> Any: 
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'
        if not re.match(pattern, value):
            raise ValueError("Lozinka mora imati najmanje 8 karaktera, jedno veliko i malo slovo, jedan broj i specijalni karakter")
        return value