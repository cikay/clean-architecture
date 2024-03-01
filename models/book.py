from tortoise import fields

from models.base import BaseModel


class BookDB(BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    language = fields.CharField(max_length=255)
    original_language = fields.CharField(max_length=255)
    authors = fields.ManyToManyField("models.AuthorDB", related_name="books")
    translators = fields.ManyToManyField("models.TranslatorDB", related_name="books")


    class Meta:
        table_name = "books"
