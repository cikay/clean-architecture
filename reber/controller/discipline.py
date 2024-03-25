from dataclasses import asdict
from reber.controller.base import GetController, GetManyController
from reber.use_cases.discipline import (
    CreateDisciplineUseCase,
    GetDisciplineUseCase,
    GetManyDisciplineUseCase,
)
from reber.entities.discipline import DisciplineCreate


class GetDisciplineController(GetController):
    def __init__(self, use_case: GetDisciplineUseCase):
        self.use_case = use_case

    async def execute(self, discipline_id) -> tuple[dict, int]:
        discipline = await self.use_case.execute(discipline_id)
        if not discipline:
            return {"detail": "discipline not found"}, 404

        discipline_dict = asdict(discipline)
        return discipline_dict, 200


class GetManyDisciplineController(GetManyController):
    def __init__(self, use_case: GetManyDisciplineUseCase):
        self.use_case = use_case

    async def execute(self) -> tuple[dict, int]:
        disciplines = await self.use_case.execute()
        disciplines_dict = [asdict(discipline) for discipline in disciplines]
        return disciplines_dict, 200


class CreateDisciplineController:
    def __init__(self, use_case: CreateDisciplineUseCase):
        self.use_case = use_case

    async def execute(self, discipline: dict) -> tuple[dict, int]:
        discipline_instance = DisciplineCreate(**discipline)
        discipline_instance = await self.use_case.execute(discipline_instance)
        discipline_dict = asdict(discipline_instance)
        return discipline_dict, 201
