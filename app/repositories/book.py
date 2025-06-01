from typing import Optional, List
from sqlalchemy import or_, func
from sqlalchemy.sql import expression
from sqlalchemy.orm import Session, Query
from app.models.book import Book
from app.core.db import Database

class RepositoryBook:
    _session : Session 
    def __init__(self) -> None:
        self._session = Database.get_session()

    def create(self, new_book: Book) -> Book:
            self._session.add(new_book)
            self._session.commit()
            self._session.refresh(new_book)
            return new_book

    def find_by_id(self, book_id: int) -> Optional[Book]:
        return self._session.query(Book).filter(Book.id == book_id).first()

    def update(self, book_id: int, updated_book: Book) -> bool:
        book = self._session.query(Book).filter(Book.id == book_id).first()
        if not book:
            return False
        for key, value in updated_book.model_dump().items():
            setattr(book, key, value)
        self._session.commit()
        return True

    def delete(self, book_id: int) -> bool:
        book = self._session.query(Book).filter(Book.id == book_id).first()
        if not book:
            return False
        self._session.delete(book)
        self._session.commit()
        return True

    def search(self, search: Optional[str] = None, available: Optional[bool] = None) -> List[Book]:
        query: Query[Book] = self._session.query(Book)
        if search:
            param_search: str = f"%{search.lower()}%"
            query = query.filter(
                or_(
                    func.lower(Book.title).like(param_search),
                    func.lower(Book.isbn).like(param_search),
                    func.lower(Book.author).like(param_search)
                ), 
                Book.available == available if available else expression.true(), 
            )

        return query.all()