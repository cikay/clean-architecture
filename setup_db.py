from models.base import db
from models.author import AuthorDB
from models.book import BookDB
from models.translator import TranslatorDB
from models.discipline import DisciplineDB

def setup_db():
    db.connect()
    db.create_tables([DisciplineDB, AuthorDB, BookDB, TranslatorDB])
