from base_use_case import BaseUseCase
from repositories.author import AuthorRepository
from entities.author import AuthorCreate


class CreateAuthorUseCase(BaseUseCase):
    def __init__(self, repo: AuthorRepository):
        self.repo = repo

    def execute(self, author: AuthorCreate):
        return self.repo.create(author)


class GetAuthorUseCase(BaseUseCase):
    def __init__(self, repo: AuthorRepository):
        self.repo = repo

    def execute(self, author_id: int):
        return self.repo.get(author_id)
