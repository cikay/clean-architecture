from peewee import CharField, PostgresqlDatabase

from models.base import BaseModel


db = PostgresqlDatabase("reber", user="reber", password="reber", host="db")


class DisciplineDB(BaseModel):
    name = CharField(unique=True)

    class Meta:
        database = db
        table_name = "disciplines"
