from base_use_case import BaseUseCase
from repositories.translator import TranslatorRepository
from entities.translator import TranslatorCreate


class CreateTranslatorUseCase(BaseUseCase):
    def __init__(self, repo: TranslatorRepository):
        self.repo = repo

    def execute(self, translator: TranslatorCreate):
        return self.repo.create(translator)


class GetTranslatorUseCase(BaseUseCase):
    def __init__(self, repo: TranslatorRepository):
        self.repo = repo

    def execute(self, translator_id: int):
        return self.repo.get(translator_id)
