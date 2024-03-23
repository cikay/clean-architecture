from tortoise.fields import CharField

from reber.models.base import BaseModel


class AuthorDB(BaseModel):
    firstname = CharField(max_length=255)
    lastname = CharField(max_length=255)
