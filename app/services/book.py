from app.repositories.book import RepositoryBook
from app.schemas.book import SchemaBook, SchemaBookBase
from app.models.book import Book
from typing import Any, List, Optional

class ServiceBook: 
    _repository : RepositoryBook
    def __init__(self) -> None:
        self._repository = RepositoryBook() 

    def find_by_id(self, book_id: int) -> SchemaBook: 
        return SchemaBook.model_validate(self._repository.find_by_id(book_id)) 
    
    def create(self, new_author: SchemaBookBase) -> SchemaBook:
        model_author: Book = Book(**new_author.model_dump())
        return SchemaBook.model_validate(self._repository.create(model_author)) 
    
    def delete(self, id: int) -> SchemaBook: 
        return SchemaBook.model_validate(self._repository.delete(id))
    
    def update(self, book_id: int, updated_book: SchemaBook) -> SchemaBook: 
        #model_book: Book = Book(**updated_book.model_dump())   
        return self.find_by_id(book_id) 
        return SchemaBook.model_validate(self._repository.update(book_id, model_book))

    def search(self, search: Optional[str] = None, available: Optional[bool] = None) -> List[SchemaBook]:
        books: List[Book] = self._repository.search(search, available)
        return [SchemaBook.model_validate(book) for book in books]
        
def get_service() -> ServiceBook: 
    return ServiceBook()