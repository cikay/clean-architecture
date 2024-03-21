from dataclasses import asdict

from reber.entities.author import Author, AuthorCreate
from reber.models.author import AuthorDB
from reber.repositories.base import BaseRepository


class AuthorRepository(BaseRepository[AuthorDB, Author]):
    async def create(self, author: AuthorCreate) -> Author:
        fields = asdict(author)
        discipline_db = await AuthorDB.create(**fields)
        return self.to_entity(discipline_db)
