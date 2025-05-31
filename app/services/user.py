from app.core.security import PasswordHasher
from app.schemas.user import SchemaUserRegister
from app.repositories.user import RepositoryUser, get_repository
from app.models.user import User
class ServiceUser: 
    _repository : RepositoryUser

    def __init__(self, repository: RepositoryUser) -> None: 
        self._repository = repository

    def register_user(self, new_user: SchemaUserRegister) -> SchemaUserRegister:
        new_user_dict = new_user.model_dump()
        print(new_user_dict)

        new_user_dict["password"] = PasswordHasher.hash_password(new_user.password)
        model_user = User(**new_user_dict)
        print(model_user)
        return SchemaUserRegister.model_validate(self._repository.create_user(model_user))

def get_service() -> ServiceUser: 
    return ServiceUser(get_repository())