from typing import Any, List, Optional, Dict
from core.classes import *

from models.author import Author
from repositories.author import RepositoryAuthor

from schemas.author import *

class ServiceAuthor: 
    _repository : RepositoryAuthor
    def __init__(self) -> None:
        self._repository = RepositoryAuthor() 

    def find_by_id(self, author_id: int) -> SchemaAuthor: 
        founded_author: Author = self._repository.find_by_id(author_id)
        if not founded_author:
            raise ExceptionNotFound
        return SchemaAuthor.model_validate(founded_author)
    
    def create(self, new_author: SchemaAuthorBase) -> SchemaAuthor:
        founded_author: Author = self._repository.find_by_name(first_name=new_author.first_name, last_name=new_author.last_name)
        if founded_author:
            raise ExceptionConflict()
        model_author : Author = Author(**new_author.model_dump())
        return SchemaAuthor.model_validate(self._repository.create(model_author))
    
    def delete(self, author_id: int) -> SchemaAuthor: 
        founded_author: Optional[SchemaAuthor] = self.find_by_id(author_id)
        return SchemaAuthor.model_validate(self._repository.delete(author_id))
    
    def update(self, author_id: int, updated_author: SchemaAuthorUpdate) -> SchemaAuthor: 
        founded_author: Optional[SchemaAuthor] = self.find_by_id(author_id)
        dict_author: Dict[str, Any] = updated_author.model_dump(exclude_unset=True)
        return SchemaAuthor.model_validate(self._repository.update(author_id, dict_author))

    def search(self, search: Optional[str]) -> List[SchemaAuthor]: 
        authors: List[Author] = self._repository.search(search)
        return [SchemaAuthor.model_validate(author) for author in authors]
        
def get_service() -> ServiceAuthor: 
    return ServiceAuthor()