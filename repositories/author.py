from dataclasses import asdict
from entities.author import Author
from models.author import AuthorDB
from repositories.base import BaseRepository


class AuthorRepository(BaseRepository[AuthorDB, Author]):
    def get(self, author_id: int) -> Author | None:
        author_db = AuthorDB.get_or_none(AuthorDB.id == author_id)
        if not author_db:
            return None

        return self.to_entity(author_db)

    def create(self, author: Author) -> Author:
        author_dict = asdict(author)
        author_db = AuthorDB.create(**author_dict)
        return self.to_entity(author_db)
