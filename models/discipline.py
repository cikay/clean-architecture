from peewee import CharField

from models.base import BaseModel


class DisciplineDB(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = "disciplines"
