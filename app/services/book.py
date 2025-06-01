from app.core.classes import *
from app.repositories.book import RepositoryBook
from app.schemas.book import *
from app.models.book import Book
from typing import Any, List, Optional, Dict

class ServiceBook: 
    _repository : RepositoryBook
    def __init__(self) -> None:
        self._repository = RepositoryBook() 

    def find_by_id(self, book_id: int) -> SchemaBook: 
        founded_book: Book = self._repository.find_by_id(book_id)
        if not founded_book:
            raise ExceptionNotFound
        return SchemaBook.model_validate(founded_book)
    
    def create(self, new_author: SchemaBookBase) -> SchemaBook:
        founded_book: Book = self._repository.find_by_title(new_author.title)
        if founded_book:
            raise ExceptionConflict()
        model_book : Book = Book(**new_author.model_dump())
        return SchemaBook.model_validate(self._repository.create(model_book))
    
    def delete(self, book_id: int) -> SchemaBook: 
        founded_book: Optional[SchemaBook] = self.find_by_id(book_id)
        return SchemaBook.model_validate(self._repository.delete(book_id))
    
    def update(self, book_id: int, updated_book: SchemaBookUpdate) -> SchemaBook: 
        founded_book: Optional[SchemaBook] = self.find_by_id(book_id)
        dict_book: Dict[str, Any] = updated_book.model_dump(exclude_unset=True)
        return SchemaBook.model_validate(self._repository.update(book_id, dict_book))

    def search(self, search: Optional[str] = None, available: Optional[bool] = None, 
               author_id: Optional[int] = None, publication_date: Optional[date] = None) -> List[SchemaBook]:
        books: List[Book] = self._repository.search(search, available, author_id, publication_date)
        return [SchemaBook.model_validate(book) for book in books]
        
def get_service() -> ServiceBook: 
    return ServiceBook()