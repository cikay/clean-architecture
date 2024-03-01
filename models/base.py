from datetime import datetime
from typing import Iterable, Optional

from tortoise import fields
from tortoise.models import Model
from tortoise.backends.base.client import BaseDBAsyncClient


class BaseModel(Model):
    created_at = fields.DatetimeField(editable=True)
    updated_at = fields.DatetimeField()

    def save(
        self,
        using_db: Optional[BaseDBAsyncClient] = None,
        update_fields: Optional[Iterable[str]] = None,
        force_create: bool = False,
        force_update: bool = False,
    ):
        if not self.id:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super().save(using_db, update_fields, force_create, force_update)

    def get_m2m_fields(self):
        return {
            k
            for k, v in self._meta.fields_map.items()
            if isinstance(v, fields.relational.ManyToManyFieldInstance)
        }
