from dataclasses import dataclass

from reber.entities.author import Author, AuthorCreate


@dataclass
class TranslatorCreate(AuthorCreate):
    pass


@dataclass
class Translator(Author):
    pass
