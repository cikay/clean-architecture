from reber.models.author import AuthorBaseDB


class TranslatorDB(AuthorBaseDB):
    class Meta:
        table_name = "translators"
