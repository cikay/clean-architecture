from controller.interlanguage_discipline import (
    CreateInterLanguageDisciplineController,
    GetInterLanguageDisciplineController,
    GetManyInterLanguageDisciplineController,
)
from repositories.interlanguage_discipline import InterLanguageDisciplineRepository
from use_cases.interlanguage_discipline import (
    CreateInterLanguageDisciplineUseCase,
    GetInterLanguageDisciplineUseCase,
    GetManyInterLanguageDisciplineUseCase,
)


class GetInterLanguageDisciplineControllerFactory:
    @staticmethod
    def create() -> GetInterLanguageDisciplineController:
        repo = InterLanguageDisciplineRepository()
        use_case = GetInterLanguageDisciplineUseCase(repo)
        return GetInterLanguageDisciplineController(use_case)


class GetManyInterLanguageDisciplineControllerFactory:
    @staticmethod
    def create() -> GetManyInterLanguageDisciplineController:
        repo = InterLanguageDisciplineRepository()
        use_case = GetManyInterLanguageDisciplineUseCase(repo)
        return GetManyInterLanguageDisciplineController(use_case)


class CreateInterLanguageDisciplineControllerFactory:
    @staticmethod
    def create() -> CreateInterLanguageDisciplineController:
        repo = InterLanguageDisciplineRepository()
        use_case = CreateInterLanguageDisciplineUseCase(repo)
        return CreateInterLanguageDisciplineController(use_case)
