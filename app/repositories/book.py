from datetime import date
from typing import Optional, List
from sqlalchemy import or_, func
from sqlalchemy.sql import expression
from sqlalchemy.orm import Session, Query
from app.models.book import Book
from app.models.author import Author
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
    
    def find_by_title(self, title: str) -> Optional[Book]:
        return self._session.query(Book).filter(Book.title == title).first()

    def update(self, author_id, updated_data: dict) -> Book:
        updated_book: Book = self.find_by_id(author_id)
        print(updated_book)
        for attr, value in updated_data.items(): 
            if attr == 'id': 
                continue
            setattr(updated_book, attr, value)

        self._session.commit()
        self._session.refresh(updated_book)
        return updated_book

    def delete(self, book_id: int) -> bool:
        book: Book = self.find_by_id(book_id)
        self._session.delete(book)
        self._session.commit()
        return book

    def search(self, search: Optional[str] = None, available: Optional[bool] = None, author_id: Optional[int] = None,  
               publication_date: Optional[date] = None) -> List[Book]:
        query: Query[Book] = self._session.query(Book).join(Book.author)
        if search:
            param_search: str = f"%{search.lower()}%"
            query = query.filter(
                or_(
                    func.lower(Book.title).like(param_search),
                    func.lower(Book.isbn).like(param_search),
                    func.lower(Book.author).like(param_search), 
                    func.lower(Author.first_name).like(param_search),
                    func.lower(Author.last_name).like(param_search),
                )
            )
        query = query.filter(
                Book.author_id == author_id if author_id is not None else expression.true(), 
                Book.available == available if available is not None  else expression.true(), 
                Book.publication_date == publication_date if publication_date is not None else expression.true()
            )
        return query.all()