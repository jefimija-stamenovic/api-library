from typing import Optional
from sqlalchemy.orm import Session
from core.db import Database
from models.user import User

class RepositoryUser: 

    def __init__(self) -> None:
        self._session: Session = Database.get_session()

    def create(self, new_user: User) -> User:
        self._session.add(new_user)
        self._session.commit()
        self._session.refresh(new_user)
        return new_user

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self._session.query(User).filter(User.id == user_id).first()
    
    def find_by_email(self, email: str) -> Optional[User]:
        return self._session.query(User).filter(User.email == email).first()
    
    def find_by_username(self, username: str) -> Optional[User]: 
        return self._session.query(User).filter(User.username == username).first()


def get_repository() -> RepositoryUser: 
    return RepositoryUser()