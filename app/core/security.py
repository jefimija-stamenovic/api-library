from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from typing import Dict, Any
import jwt

class PasswordHasher: 
   _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

   @classmethod
   def hash_password(cls, password: str) -> str:
      return cls._pwd_context.hash(password)

   @classmethod
   def verify_password(cls, password: str, hashed_password: str) -> bool:
      return cls._pwd_context.verify(password, hashed_password)
   

class JWTHelper: 
   
   @classmethod
   def create_access_token(cls, data: Dict[str, Any], secret_key: str, algorithm: str, expire_minutes: int) -> str:
      expire: datetime = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
      data.update({"exp": expire})
      return jwt.encode(data, secret_key, algorithm=algorithm)

   @classmethod
   def create_refresh_token(cls, data: Dict[str, Any], secret_key: str, algorithm: str, expire_days: int) -> str:
      expire: datetime = datetime.now(timezone.utc) + timedelta(days=expire_days)
      data.update({"exp": expire})
      return jwt.encode(data, secret_key, algorithm=algorithm)