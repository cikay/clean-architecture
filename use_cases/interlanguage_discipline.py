from base_use_case import BaseUseCase
from repositories.interlanguage_discipline import InterLanguageDisciplineRepository
from entities.interlanguage_discipline import InterLanguageDisciplineCreate


class CreateInterLanguageDisciplineUseCase(BaseUseCase):
    def __init__(self, repo: InterLanguageDisciplineRepository):
        self.repo = repo

    async def execute(self, discipline: InterLanguageDisciplineCreate):
        return await self.repo.create(discipline)


class GetInterLanguageDisciplineUseCase(BaseUseCase):
    def __init__(self, repo: InterLanguageDisciplineRepository):
        self.repo = repo

    async def execute(self, discipline_id: int):
        return await self.repo.get(discipline_id)


class GetManyInterLanguageDisciplineUseCase(BaseUseCase):
    def __init__(self, repo: InterLanguageDisciplineRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.get_many()
