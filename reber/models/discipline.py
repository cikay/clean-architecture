from tortoise import fields

from reber.models.base import BaseModel


class DisciplineDB(BaseModel):
    name = fields.CharField(unique=True, max_length=255)
    interlanguage_discipline = fields.ForeignKeyField(
        "models.InterLanguageDisciplineDB", related_name="disciplines"
    )
    parent_discipline = fields.ForeignKeyField(
        "models.DisciplineDB", related_name="sub_disciplines", null=True
    )

    class Meta:
        table = "disciplines"
