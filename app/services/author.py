from app.schemas.author import SchemaAuthorBase, SchemaAuthor
from app.models.author import Author
from app.repositories.author import RepositoryAuthor
from typing import Any, List, Optional
from app.core.classes import *

class ServiceAuthor: 
    _repository : RepositoryAuthor
    def __init__(self):
        self._repository = RepositoryAuthor() 

    def find_by_id(self, id: int) -> SchemaAuthor: 
        return SchemaAuthor.model_validate(self._repository.find_by_id(id)) 
    
    def create(self, new_author: SchemaAuthorBase) -> SchemaAuthor:
        founded_author: Author = self._repository.find_by_name(first_name=new_author.first_name, last_name=new_author.last_name)
        if founded_author:
            raise ExceptionConflict("Author with this name already exists.")
        model_author : Author = Author(**new_author.model_dump())
        return SchemaAuthor.model_validate(self._repository.create(model_author))
    
    def delete(self, id: int) -> SchemaAuthor: 
        return SchemaAuthor.model_validate(self._repository.delete(id))
    
    def update(self, id: int, updated_author: SchemaAuthorBase) -> SchemaAuthor: 
        dict_author: dict[str, Any] =updated_author.model_dump()
        dict_author["id"] = id
        model_author: Author = Author(**dict_author)
        
        return SchemaAuthor.model_validate(self._repository.update(id, model_author))

    def search(self, search: Optional[str]) -> List[SchemaAuthor]: 
        authors: List[Author] = self._repository.search(search)
        return [SchemaAuthor.model_validate(author) for author in authors]
        
def get_service() -> ServiceAuthor: 
    return ServiceAuthor()