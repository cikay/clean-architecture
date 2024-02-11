from peewee import CharField, ManyToManyField

from models.base import BaseModel


class BookDB(BaseModel):
    name = CharField()
    authors = ManyToManyField("AuthorDB", backref="books")
    translators = ManyToManyField("TranslatorDB", backref="books")

    class Meta:
        table_name = "books"
