from tortoise.fields import CharField

from models.base import BaseModel


class DisciplineDB(BaseModel):
    name = CharField(unique=True, max_length=255)

    class Meta:
        table = "disciplines"
