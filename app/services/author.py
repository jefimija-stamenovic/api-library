from app.schemas.author import SchemaAuthorBase, SchemaAuthor
from app.models.author import Author
from app.repositories.author import RepositoryAuthor
from typing import Any, List, Optional

class ServiceAuthor: 
    _repository : RepositoryAuthor
    def __init__(self):
        self._repository = RepositoryAuthor() 

    def get_by_id(self, id: int) -> SchemaAuthor: 
        return SchemaAuthor.model_validate(self._repository.get_by_id(id)) 
    
    def create(self, new_author: SchemaAuthorBase) -> SchemaAuthor:
        model_author: Author = Author(**new_author.model_dump())
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