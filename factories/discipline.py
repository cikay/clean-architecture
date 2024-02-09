from controller.discipline import CreateDisciplineController, GetDisciplineController
from repositories.discipline import DisciplineRepository
from use_cases.discipline import CreateDisciplineUseCase, GetDisciplineUseCase


class GetDisciplineControllerFactory:
    @staticmethod
    def create() -> GetDisciplineController:
        repo = DisciplineRepository()
        use_case = GetDisciplineUseCase(repo)
        return GetDisciplineController(use_case)


class CreateDisciplineControllerFactory:
    @staticmethod
    def create() -> CreateDisciplineController:
        repo = DisciplineRepository()
        use_case = CreateDisciplineUseCase(repo)
        return CreateDisciplineController(use_case)
