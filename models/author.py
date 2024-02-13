from peewee import CharField

from models.base import BaseModel


class AuthorBaseDB(BaseModel):
    firstname = CharField()
    lastname = CharField()

    class Meta:
        abstract = True


class AuthorDB(AuthorBaseDB):
    pass
