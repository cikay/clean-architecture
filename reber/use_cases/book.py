from reber.use_cases.base import BaseCreateUseCase, GetUseCase
from reber.repositories.book import BookRepository
from reber.entities.book import BookCreate


class CreateBookUseCase(BaseCreateUseCase):
    def __init__(self, repo: BookRepository):
        self.repo = repo

    async def execute(self, create_type: BookCreate):
        return await self.repo.create(create_type)


class GetBookUseCase(GetUseCase):
    def __init__(self, repo: BookRepository):
        self.repo = repo

    async def execute(self, book_id: int):
        return await self.repo.get(book_id)
