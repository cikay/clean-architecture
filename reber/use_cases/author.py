from reber.use_cases.base import BaseCreateUseCase, GetManyUseCase, GetUseCase
from reber.repositories.author import AuthorRepository
from reber.entities.author import AuthorCreate


class CreateAuthorUseCase(BaseCreateUseCase):
    def __init__(self, repo: AuthorRepository):
        self.repo = repo

    async def execute(self, create_type: AuthorCreate):
        return await self.repo.create(create_type)


class GetAuthorUseCase(GetUseCase):
    def __init__(self, repo: AuthorRepository):
        self.repo = repo

    async def execute(self, author_id: int):
        return await self.repo.get(author_id)


class GetManyAuthorUseCase(GetManyUseCase):
    def __init__(self, repo: AuthorRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.get_many()
