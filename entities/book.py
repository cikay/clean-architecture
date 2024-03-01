from datetime import datetime
from dataclasses import dataclass, field


from base_entity import BaseCreateEntity
from entities.author import Author
from entities.translator import Translator


@dataclass
class BookCreate(BaseCreateEntity):
    name: str
    language: str
    original_language: str
    authors: list[int]
    translators: list[int]


@dataclass
class Book:
    id: str
    name: str
    language: str
    original_language: str
    authors: list[Author]
    translators: list[Translator]
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    # domain business logic goes here


@dataclass
class BookQuery:
    pass
