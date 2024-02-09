from datetime import datetime

from peewee import Model, DateTimeField, PostgresqlDatabase

db = PostgresqlDatabase("reber", user="reber", password="reber", host="db")


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
