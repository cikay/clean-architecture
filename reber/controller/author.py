from reber.use_cases.author import CreateAuthorUseCase, GetAuthorUseCase
from reber.entities.author import AuthorCreate


class GetAuthorController:
    def __init__(self, use_case: GetAuthorUseCase):
        self.use_case = use_case

    async def get(self, author_id) -> tuple[dict, int]:
        author = await self.use_case.execute(author_id)
        if not author:
            return {"detail": "author not found"}, 404

        return author, 200


class CreateAuthorController:
    def __init__(self, use_case: CreateAuthorUseCase):
        self.use_case = use_case

    async def create(self, author: dict) -> tuple[dict, int]:
        author_instance = AuthorCreate(**author)
        return await self.use_case.execute(author_instance), 201
