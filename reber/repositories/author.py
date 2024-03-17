from dataclasses import asdict

from reber.entities.author import Author
from reber.models.author import AuthorDB
from reber.repositories.base import BaseRepository


class AuthorRepository(BaseRepository[AuthorDB, Author]):
    pass