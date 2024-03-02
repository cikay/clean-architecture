from tortoise.fields import CharField

from models.base import BaseModel


class InterLanguageDisciplineDB(BaseModel):
    name = CharField(unique=True, max_length=255)

    class Meta:
        table = "interlanguage_disciplines"
