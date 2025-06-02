from typing import Any, Sequence, Optional, Dict
from core.classes import *

from models.author import Author
from repositories.author import RepositoryAuthor

from schemas.author import *

class ServiceAuthor: 
    _repository : RepositoryAuthor
    def __init__(self) -> None:
        self._repository = RepositoryAuthor() 

    async def find_by_id(self, author_id: int) -> SchemaAuthor: 
        founded_author: Author = await self._repository.find_by_id(author_id)
        if not founded_author:
            raise ExceptionNotFound
        return SchemaAuthor.model_validate(founded_author)
    
    async def create(self, new_author: SchemaAuthorBase) -> SchemaAuthor:
        founded_author: Author = await self._repository.find_by_name(first_name=new_author.first_name, last_name=new_author.last_name)
        if founded_author:
            raise ExceptionConflict()
        model_author : Author = Author(**new_author.model_dump())
        return SchemaAuthor.model_validate(self._repository.create(model_author))
    
    async def delete(self, author_id: int) -> SchemaAuthor: 
        founded_author: Optional[SchemaAuthor] = await self.find_by_id(author_id)
        deleted_author = await self._repository.delete(author_id)
        return SchemaAuthor.model_validate(deleted_author)
    
    async def update(self, author_id: int, updated_author: SchemaAuthorUpdate) -> SchemaAuthor: 
        founded_author: Optional[SchemaAuthor] = await self.find_by_id(author_id)
        dict_author: Dict[str, Any] = updated_author.model_dump(exclude_unset=True)
        updated_author = await self._repository.update(author_id, dict_author)
        return SchemaAuthor.model_validate(updated_author)

    async def search(self, search: Optional[str]) -> Sequence[SchemaAuthor]: 
        authors: Sequence[Author] = await self._repository.search(search)
        return [SchemaAuthor.model_validate(author) for author in authors]
        
def get_service() -> ServiceAuthor: 
    return ServiceAuthor()