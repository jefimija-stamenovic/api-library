from app.models.user import User

class RepositoryUser: 
    
    def create_user(self, new_user: User) -> User: 
        return User() 


def get_repository() -> RepositoryUser: 
    return RepositoryUser()