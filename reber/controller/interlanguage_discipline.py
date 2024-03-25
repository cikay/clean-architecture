from dataclasses import asdict

from reber.controller.base import GetController, GetManyController
from reber.use_cases.interlanguage_discipline import (
    CreateInterLanguageDisciplineUseCase,
)
from reber.entities.interlanguage_discipline import InterLanguageDisciplineCreate


class GetInterLanguageDisciplineController(GetController):
    async def execute(self, id) -> tuple[dict, int]:
        discipline = await self.use_case.execute(id)

        if not discipline:
            return {"detail": "discipline not found"}, 404

        discipline_dict = asdict(discipline)
        return discipline_dict, 200


class GetManyInterLanguageDisciplineController(GetManyController):
    async def execute(self) -> tuple[dict, int]:
        disciplines = await self.use_case.execute()
        disciplines_dict = [asdict(discipline) for discipline in disciplines]
        return disciplines_dict, 200


class CreateInterLanguageDisciplineController:
    def __init__(self, use_case: CreateInterLanguageDisciplineUseCase):
        self.use_case = use_case

    async def execute(self, discipline: dict) -> tuple[dict, int]:
        discipline_create_instance = InterLanguageDisciplineCreate(**discipline)
        discipline_instance = await self.use_case.execute(discipline_create_instance)
        discipline_dict = asdict(discipline_instance)
        return discipline_dict, 201
