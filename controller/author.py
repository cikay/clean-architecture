from use_cases.author import CreateAuthorUseCase, GetAuthorUseCase
from entities.author import AuthorCreate


class GetAuthorController:
    def __init__(self, use_case: GetAuthorUseCase):
        self.use_case = use_case

    def get(self, author_id) -> tuple[dict, int]:
        return self.use_case.execute(author_id), 200


class CreateAuthorController:
    def __init__(self, use_case: CreateAuthorUseCase):
        self.use_case = use_case

    def create(self, author: dict) -> tuple[dict, int]:
        author_instance = AuthorCreate(**author)
        return self.use_case.execute(author_instance), 201
