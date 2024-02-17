from controller.discipline import CreateDisciplineController, GetDisciplineController, GetManyDisciplineController
from repositories.discipline import DisciplineRepository
from use_cases.discipline import CreateDisciplineUseCase, GetDisciplineUseCase, GetManyDisciplineUseCase


class GetDisciplineControllerFactory:
    @staticmethod
    def create() -> GetDisciplineController:
        repo = DisciplineRepository()
        use_case = GetDisciplineUseCase(repo)
        return GetDisciplineController(use_case)


class GetManyDisciplineControllerFactory:
    @staticmethod
    def create() -> GetManyDisciplineController:
        repo = DisciplineRepository()
        use_case = GetManyDisciplineUseCase(repo)
        return GetManyDisciplineController(use_case)


class CreateDisciplineControllerFactory:
    @staticmethod
    def create() -> CreateDisciplineController:
        repo = DisciplineRepository()
        use_case = CreateDisciplineUseCase(repo)
        return CreateDisciplineController(use_case)
