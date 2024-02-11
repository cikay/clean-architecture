from use_cases.author import CreateAuthorUseCase, GetAuthorUseCase
from entities.author import AuthorCreate


class GetAuthorController:
    def __init__(self, use_case: GetAuthorUseCase):
        self.use_case = use_case

    def get(self, author_id) -> tuple[dict, int]:
        author = self.use_case.execute(author_id)
        if not author:
            return {"detail": "author not found"}, 404

        return author, 200


class CreateAuthorController:
    def __init__(self, use_case: CreateAuthorUseCase):
        self.use_case = use_case

    def create(self, author: dict) -> tuple[dict, int]:
        author_instance = AuthorCreate(**author)
        return self.use_case.execute(author_instance), 201
