from tortoise import fields

from reber.models.base import BaseModel


class DisciplineDB(BaseModel):
    name = fields.CharField(unique=True, max_length=255)
    interlanguage_discipline = fields.ForeignKeyField(
        "models.InterlanguageDisciplineDB", related_name="disciplines"
    )

    class Meta:
        table = "disciplines"
