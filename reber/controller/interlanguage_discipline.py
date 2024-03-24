from dataclasses import asdict

from reber.use_cases.interlanguage_discipline import (
    CreateInterLanguageDisciplineUseCase,
    GetManyInterLanguageDisciplineUseCase,
)
from reber.entities.interlanguage_discipline import InterLanguageDisciplineCreate


class GetInterLanguageDisciplineController:
    def __init__(self, use_case: InterLanguageDisciplineCreate):
        self.use_case = use_case

    async def execute(self, discipline_id) -> tuple[dict, int]:
        discipline = await self.use_case.execute(discipline_id)

        if not discipline:
            return {"detail": "discipline not found"}, 404

        discipline_dict = asdict(discipline)
        return discipline_dict, 200


class GetManyInterLanguageDisciplineController:
    def __init__(self, use_case: GetManyInterLanguageDisciplineUseCase):
        self.use_case = use_case

    async def get_many(self) -> tuple[dict, int]:
        disciplines = await self.use_case.execute()
        return disciplines, 200


class CreateInterLanguageDisciplineController:
    def __init__(self, use_case: CreateInterLanguageDisciplineUseCase):
        self.use_case = use_case

    async def execute(self, discipline: dict) -> tuple[dict, int]:
        discipline_create_instance = InterLanguageDisciplineCreate(**discipline)
        discipline_instance = await self.use_case.execute(discipline_create_instance)
        discipline_dict = asdict(discipline_instance)
        return discipline_dict, 201
