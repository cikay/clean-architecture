from reber.base_use_case import BaseUseCase
from repositories.book import BookRepository
from reber.entities.book import BookCreate


class CreateBookUseCase(BaseUseCase):
    def __init__(self, repo: BookRepository):
        self.repo = repo

    async def execute(self, book: BookCreate):
        return await self.repo.create(book)


class GetBookUseCase(BaseUseCase):
    def __init__(self, repo: BookRepository):
        self.repo = repo

    async def execute(self, book_id: int):
        return await self.repo.get(book_id)
