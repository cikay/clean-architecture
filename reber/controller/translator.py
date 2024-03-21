from use_cases.translator import CreateTranslatorUseCase, GetTranslatorUseCase
from reber.entities.translator import TranslatorCreate


class GetTranslatorController:
    def __init__(self, use_case: GetTranslatorUseCase):
        self.use_case = use_case

    async def get(self, translator_id) -> tuple[dict, int]:
        translator = await self.use_case.execute(translator_id)
        if not translator:
            return {"detail": "Translator not found"}, 404

        return translator, 200


class CreateTranslatorController:
    def __init__(self, use_case: CreateTranslatorUseCase):
        self.use_case = use_case

    async def create(self, translator: dict) -> tuple[dict, int]:
        translator_instance = TranslatorCreate(**translator)
        return await self.use_case.execute(translator_instance), 201
