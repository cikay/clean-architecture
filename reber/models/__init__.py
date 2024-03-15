from models.author import AuthorDB
from models.book import BookDB
from models.discipline import DisciplineDB
from models.interlanguage_discipline import InterLanguageDisciplineDB
from models.translator import TranslatorDB

__models__ = [DisciplineDB, AuthorDB, TranslatorDB, BookDB, InterLanguageDisciplineDB]
