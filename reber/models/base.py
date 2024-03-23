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

    def get_list_fields(self):
        list_fields = set()
        for field_name, value in self._meta.fields_map.items():
            if isinstance(value, fields.relational.ManyToManyFieldInstance):
                list_fields.add(field_name)
            elif isinstance(value, fields.relational.ForeignKeyFieldInstance):
                _, model_name = self._meta.fields_map[field_name].model_name.split(".")
                if model_name == self.__class__.__name__:
                    list_field = self._meta.fields_map[field_name].related_name
                    list_fields.add(list_field)

        return list_fields

    def get_foreign_key_fields(self):
        return {
            k
            for k, v in self._meta.fields_map.items()
            if isinstance(v, fields.relational.ForeignKeyFieldInstance)
        }

    @classmethod
    def get_fields_name(cls) -> set[str]:
        fields_name = set()
        for key, value in cls._meta.fields_map.items():
            print(key)
            if not isinstance(value, fields.relational.BackwardFKRelation):
                fields_name.add(key)

        return fields_name
