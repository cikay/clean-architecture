from reber.base_use_case import BaseUseCase
from reber.repositories.translator import TranslatorRepository
from reber.entities.translator import TranslatorCreate


class CreateTranslatorUseCase(BaseUseCase):
    def __init__(self, repo: TranslatorRepository):
        self.repo = repo

    async def execute(self, translator: TranslatorCreate):
        return await self.repo.create(translator)


class GetTranslatorUseCase(BaseUseCase):
    def __init__(self, repo: TranslatorRepository):
        self.repo = repo

    async def execute(self, translator_id: int):
        return await self.repo.get(translator_id)


class GetManyTranslatorUseCase(BaseUseCase):
    def __init__(self, repo: TranslatorRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.get_many()
