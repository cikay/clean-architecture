from reber.use_cases.base import BaseCreateUseCase, GetManyUseCase, GetUseCase
from reber.repositories.discipline import DisciplineRepository
from reber.entities.discipline import DisciplineCreate


class CreateDisciplineUseCase(BaseCreateUseCase):
    def __init__(self, repo: DisciplineRepository):
        self.repo = repo

    async def execute(self, create_type: DisciplineCreate):
        return await self.repo.create(create_type)


class GetDisciplineUseCase(GetUseCase):
    def __init__(self, repo: DisciplineRepository):
        self.repo = repo

    async def execute(self, discipline_id: int):
        return await self.repo.get(discipline_id)


class GetManyDisciplineUseCase(GetManyUseCase):
    def __init__(self, repo: DisciplineRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.get_many()
