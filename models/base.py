from datetime import datetime

from peewee import Model, DateTimeField


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
