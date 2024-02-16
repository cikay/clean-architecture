from datetime import datetime

from tortoise.fields import DatetimeField
from tortoise.models import Model



class BaseModel(Model):
    created_at = DatetimeField(default=datetime.now)
    updated_at = DatetimeField(default=datetime.now)
