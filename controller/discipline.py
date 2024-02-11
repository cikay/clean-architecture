from use_cases.discipline import CreateDisciplineUseCase, GetDisciplineUseCase
from entities.discipline import DisciplineCreate


class GetDisciplineController:
    def __init__(self, use_case: GetDisciplineUseCase):
        self.use_case = use_case

    def get(self, discipline_id) -> tuple[dict, int]:
        discipline = self.use_case.execute(discipline_id)

        if not discipline:
            return {"detail": "discipline not found"}, 404

        return discipline, 200


class CreateDisciplineController:
    def __init__(self, use_case: CreateDisciplineUseCase):
        self.use_case = use_case

    def create(self, discipline: dict) -> tuple[dict, int]:
        discipline_instance = DisciplineCreate(**discipline)
        return self.use_case.execute(discipline_instance), 201
