from dataclasses import asdict
from entities.author import Author
from models.author import AuthorDB
from repositories.base import BaseRepository


class AuthorRepository(BaseRepository[AuthorDB, Author]):
    pass