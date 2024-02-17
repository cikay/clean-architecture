from base_use_case import BaseUseCase
from repositories.author import AuthorRepository
from entities.author import AuthorCreate


class CreateAuthorUseCase(BaseUseCase):
    def __init__(self, repo: AuthorRepository):
        self.repo = repo

    async def execute(self, author: AuthorCreate):
        return await self.repo.create(author)


class GetAuthorUseCase(BaseUseCase):
    def __init__(self, repo: AuthorRepository):
        self.repo = repo

    async def execute(self, author_id: int):
        return await self.repo.get(author_id)
