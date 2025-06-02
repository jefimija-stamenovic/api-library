from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from typing import Dict, Any
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from repositories.user import RepositoryUser, get_repository
from schemas.user import *
from core.classes import *
from core.config import settings
 
class PasswordHasher: 
   _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

   @classmethod
   def hash_password(cls, password: str) -> str:
      return cls._pwd_context.hash(password)

   @classmethod
   def verify_password(cls, password: str, hashed_password: str) -> bool:
      return cls._pwd_context.verify(password, hashed_password)
   
class JWTHelper: 
   oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
   @classmethod
   def create_access_token(cls, data: Dict[str, Any]) -> str:
      expire: datetime = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
      data.update({"exp": expire})
      return jwt.encode(data, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)

   @classmethod
   def create_refresh_token(cls, data: Dict[str, Any]) -> str:
      expire: datetime = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
      data.update({"exp": expire})
      return jwt.encode(data, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
   

   @classmethod
   def get_current_user(cls, token: str = Depends(oauth2_scheme), repository: RepositoryUser = Depends(get_repository)) -> SchemaUser:
      try:
         payload: Any = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
         username: str = payload.get("sub")
         if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials.", headers={"WWW-Authenticate": "Bearer"})
         return SchemaUser.model_validate(repository.find_by_username(username)) 
      except ExceptionNotAuthorized as e: 
         raise HTTPException( status_code=status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized")
      except Exception as e: 
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))