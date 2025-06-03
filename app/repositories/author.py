from typing import Optional, Sequence
from sqlalchemy import or_, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from models.author import Author
from core.db import Database


class RepositoryAuthor:
    _session: AsyncSession

    def __init__(self) -> None:
        self._session = Database.get_session_async()

    async def create(self, new_author: Author) -> Author:
        self._session.add(new_author)
        await self._session.commit()
        await self._session.refresh(new_author)

        result = await self._session.execute(
            select(Author)
            .options(selectinload(Author.books))
            .where(Author.id == new_author.id)
        )
        author_with_books = result.scalar_one()
        return author_with_books

    async def find_by_id(self, author_id: int) -> Optional[Author]:
        stmt = (
            select(Author)
            .options(selectinload(Author.books))
            .where(Author.id == author_id)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def find_by_name(self, first_name: str, last_name: str) -> Optional[Author]:
        stmt = (
            select(Author)
            .options(selectinload(Author.books))
            .where(Author.first_name == first_name, Author.last_name == last_name)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, author_id: int, updated_data: dict) -> Author:
        author: Author = await self.find_by_id(author_id)
        for attr, value in updated_data.items():
            if attr == "books":
                continue
            setattr(author, attr, value)

        await self._session.commit()
        await self._session.refresh(author)
        return author

    async def delete(self, author_id: int) -> Optional[Author]:
        print("DELETE")
        author: Author = await self.find_by_id(author_id)
        await self._session.delete(author)
        await self._session.commit()
        return author

    async def search(self, search: Optional[str] = None) -> Sequence[Author]:
        stmt = select(Author).options(selectinload(Author.books))
        if search:
            param_search = f"%{search.lower()}%"
            stmt = stmt.where(
                or_(
                    func.lower(Author.first_name).like(param_search),
                    func.lower(Author.last_name).like(param_search),
                    func.lower(Author.biography).like(param_search),
                )
            )

        result = await self._session.execute(stmt)
        return result.scalars().all()
