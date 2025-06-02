from typing import Dict, Any
from core.security import *
from core.classes import *
from core.config import settings
from schemas.user import *
from repositories.user import RepositoryUser, get_repository
from models.user import User

class ServiceUser: 
    _repository : RepositoryUser

    def __init__(self, repository: RepositoryUser) -> None: 
        self._repository = repository

    def register(self, new_user: SchemaUserRegister) -> SchemaUserRegister:
        founded_user: User = self._repository.find_by_email(new_user.email)
        if founded_user: 
            raise ExceptionConflict(f"User with email = {new_user.email} already exists")
        
        founded_user: User = self._repository.find_by_username(new_user.username)
        if founded_user: 
            raise ExceptionConflict(f"User with username = {new_user.username} already exists")
        
        user_dict : Dict[str, Any] = new_user.model_dump()
        user_dict["password"] = PasswordHasher.hash_password(new_user.password)
        return SchemaUserRegister.model_validate(self._repository.create(User(**user_dict)))
    
    def login(self, credentials: SchemaCredentials) -> Token: 
        founded_user: User = self._repository.find_by_username(credentials.username)
        if not founded_user: 
            raise ExceptionConflict(f"User with username = {credentials.username} not found")
        
        if not PasswordHasher.verify_password(credentials.password, founded_user.hashed_password):
            raise ExceptionNotAuthorized()

        data: Dict[str, Any] = {"sub": founded_user.username}
        access_token: str = JWTHelper.create_access_token(data, settings.JWT_SECRET_KEY, settings.ALGORITHM, settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token: str = JWTHelper.create_refresh_token(data, settings.JWT_SECRET_KEY, settings.ALGORITHM, settings.REFRESH_TOKEN_EXPIRE_DAYS)

        return Token(access_token=access_token, refresh_token=refresh_token)
def get_service() -> ServiceUser: 
    return ServiceUser(get_repository())