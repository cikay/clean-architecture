from reber.use_cases.base import BaseCreateUseCase
from reber.repositories.interlanguage_discipline import (
    InterLanguageDisciplineRepository,
)
from reber.entities.interlanguage_discipline import InterLanguageDisciplineCreate


class CreateInterLanguageDisciplineUseCase(BaseCreateUseCase):
    def __init__(self, repo: InterLanguageDisciplineRepository):
        self.repo = repo

    async def execute(self, create_type: InterLanguageDisciplineCreate):
        return await self.repo.create(create_type)


class GetInterLanguageDisciplineUseCase:
    def __init__(self, repo: InterLanguageDisciplineRepository):
        self.repo = repo

    async def execute(self, discipline_id: int):
        return await self.repo.get(discipline_id)


class GetManyInterLanguageDisciplineUseCase:
    def __init__(self, repo: InterLanguageDisciplineRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.get_many()
