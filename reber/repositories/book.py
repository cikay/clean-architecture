from dataclasses import asdict

from reber.entities.book import Book
from reber.models.author import AuthorDB
from reber.models.book import BookDB
from reber.models.translator import TranslatorDB
from reber.repositories.base import BaseRepository


class BookRepository(BaseRepository[BookDB, Book]):
    async def create(self, book: Book) -> Book:
        fields = asdict(book)
        import ipdb

        ipdb.set_trace()
        authors = fields.pop("authors")
        translators = fields.pop("translators")
        discipline = fields.pop("discipline")
        author_instances = await AuthorDB.filter(id__in=authors)
        translators_instance = await TranslatorDB.filter(id__in=translators)
        fields["discipline"] = await DisciplineDB.get(id=discipline)

        book_db = await BookDB.create(**fields)
        await book_db.authors.add(*author_instances)
        await book_db.translators.add(*translators_instance)
        book_db = await BookDB.filter(id=book_db.id).prefetch_related(
            "authors", "translators", "discipline"
        )

        return self.to_entity(book_db)

    async def get(self, id: int) -> Book | None:
        db_type = self._get_db_type()
        db_instance = (
            await db_type.filter(id=id)
            .prefetch_related("translators", "authors", "discipline")
            .first()
        )
        if not db_instance:
            return None

        return self.to_entity(db_instance)
