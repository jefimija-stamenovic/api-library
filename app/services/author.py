from app.models.book import Book
from app.schemas.author import SchemaAuthorBase, SchemaAuthor, SchemaAuthorUpdate
from app.models.author import Author
from app.repositories.author import RepositoryAuthor
from app.services.book import ServiceBook

from typing import Any, List, Optional, Dict
from app.core.classes import *

class ServiceAuthor: 
    _repository : RepositoryAuthor
    _service_book : ServiceBook
    def __init__(self) -> None:
        self._repository = RepositoryAuthor() 
        self._service_book = ServiceBook()

    def find_by_id(self, author_id: int) -> SchemaAuthor: 
        founded_author: Author = self._repository.find_by_id(author_id)
        if not founded_author:
            raise ExceptionNotFound
        return SchemaAuthor.model_validate(founded_author)
    
    def create(self, new_author: SchemaAuthorBase) -> SchemaAuthor:
        founded_author: Author = self._repository.find_by_name(first_name=new_author.first_name, last_name=new_author.last_name)
        if founded_author:
            raise ExceptionConflict("Author with this name already exists.")
        model_author : Author = Author(**new_author.model_dump())
        return SchemaAuthor.model_validate(self._repository.create(model_author))
    
    def delete(self, id: int) -> SchemaAuthor: 
        return SchemaAuthor.model_validate(self._repository.delete(id))
    
    def update(self, author_id: int, updated_author: SchemaAuthorUpdate) -> SchemaAuthor: 
        founded_author: Optional[Author] = self._repository.find_by_id(author_id)
        if not founded_author: 
            raise ExceptionNotFound
        dict_author: Dict[str, Any] = updated_author.model_dump(exclude_unset=True)

        if updated_author.books:
            for updated_book in updated_author.books:
                pass 
                #self._service_book.update(updated_book.id, updated_book)
           
        return SchemaAuthor.model_validate(self._repository.update(author_id, dict_author))

    def search(self, search: Optional[str]) -> List[SchemaAuthor]: 
        authors: List[Author] = self._repository.search(search)
        return [SchemaAuthor.model_validate(author) for author in authors]
        
def get_service() -> ServiceAuthor: 
    return ServiceAuthor()