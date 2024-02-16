from base_use_case import BaseUseCase
from repositories.discipline import DisciplineRepository
from entities.discipline import DisciplineCreate


class CreateDisciplineUseCase(BaseUseCase):
    def __init__(self, repo: DisciplineRepository):
        self.repo = repo

    async def execute(self, discipline: DisciplineCreate):
        return await self.repo.create(discipline)


class GetDisciplineUseCase(BaseUseCase):
    def __init__(self, repo: DisciplineRepository):
        self.repo = repo

    async def execute(self, discipline_id: int):
        return await self.repo.get(discipline_id)
