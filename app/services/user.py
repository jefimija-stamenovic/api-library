from app.core.security import PasswordHasher
from app.schemas.user import SchemaUserRegister
from app.repositories.user import RepositoryUser

class ServiceUser: 
    _repository : RepositoryUser

    def __init__(self, repository: RepositoryUser) -> None: 
        self._repository = repository

    def register_user(self, new_user: SchemaUserRegister): 
        hashed_password = PasswordHasher.hash_password(new_user.password)
        return self._repository.create_user(new_user, hashed_password)