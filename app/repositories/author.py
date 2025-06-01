from typing import Optional, List
from sqlalchemy import or_, func
from sqlalchemy.orm import Session, Query
from app.models.author import Author
from app.core.db import Database

class RepositoryAuthor:
    _session: Session

    def __init__(self) -> None:
        self._session = Database.get_session()

    def create(self, new_author: Author) -> Author:
        self._session.add(new_author)
        self._session.commit()
        self._session.refresh(new_author)
        return new_author

    def find_by_id(self, author_id: int) -> Optional[Author]:
        return self._session.query(Author).filter(Author.id == author_id).first()
    
    def find_by_name(self, first_name: str, last_name: str) -> Optional[Author]:
        return self._session.query(Author).filter(Author.first_name == first_name, 
                                                  Author.last_name == last_name).first()

    def update(self, author_id: int, updated_author: Author) -> bool:
        author: Optional[Author] = self.find_by_id(author_id)
        if not author:
            return False
        for key, value in updated_author.model_dump().items():
            setattr(author, key, value)
        self._session.add(author)
        self._session.commit()
        return True

    def delete(self, author_id: int) -> bool:
        author: Optional[Author] = self.find_by_id(author_id)
        if not author:
            return False
        self._session.delete(author)
        self._session.commit()
        return True

    def search(self, search: Optional[str] = None) -> List[Author]:
        query: Query[Author] = self._session.query(Author)
        if search:
            param_search: str = f"%{search.lower()}%"
            query = query.filter(
                or_(
                    func.lower(Author.first_name).like(param_search),
                    func.lower(Author.last_name).like(param_search),
                    func.lower(Author.biography).like(param_search)
                )
            )
        return query.all()
