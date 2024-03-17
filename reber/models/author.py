from tortoise.fields import CharField

from reber.models.base import BaseModel


class AuthorBaseDB(BaseModel):
    firstname = CharField(max_length=255)
    lastname = CharField(max_length=255)

    class Meta:
        abstract = True


class AuthorDB(AuthorBaseDB):
    pass
