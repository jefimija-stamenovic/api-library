from typing import Dict, Any
from core.classes import *
from core.config import settings
from core.security import PasswordHasher, JWTHelper
from schemas.user import *
from repositories.user import RepositoryUser, get_repository
from models.user import User

class ServiceUser: 
    _repository : RepositoryUser

    def __init__(self, repository: RepositoryUser) -> None: 
        self._repository = repository

    def find_by_username(self, username: str) -> SchemaUser: 
        founded_user: User = self._repository.find_by_username(username)
        if not founded_user: 
            raise ExceptionNotAuthorized()
        return SchemaUser.model_validate(founded_user)

    def register(self, new_user: SchemaUserRegister) -> SchemaUser:
        founded_user: User = self._repository.find_by_email(new_user.email)
        if founded_user: 
            raise ExceptionConflict(f"User with email = {new_user.email} already exists")
        
        founded_user: User = self._repository.find_by_username(new_user.username)
        if founded_user: 
            raise ExceptionConflict(f"User with username = {new_user.username} already exists")
        
        user_dict : Dict[str, Any] = new_user.model_dump()
        user_dict["password"] = PasswordHasher.hash_password(new_user.password)
        model_user : User = User(**user_dict)
        return SchemaUser.model_validate(self._repository.create(model_user))
    
    def login(self, credentials: SchemaCredentials) -> SchemaToken: 
        founded_user: SchemaUser = self.find_by_username(credentials.username)
        
        if not PasswordHasher.verify_password(credentials.password, str(founded_user.password)):
            raise ExceptionNotAuthorized()

        data: Dict[str, Any] = {"sub": founded_user.username}
        access_token: str = JWTHelper.create_access_token(data)
        refresh_token: str = JWTHelper.create_refresh_token(data)
        return SchemaToken(access_token=access_token, refresh_token=refresh_token)
def get_service() -> ServiceUser: 
    return ServiceUser(get_repository())