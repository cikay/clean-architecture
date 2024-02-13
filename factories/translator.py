from controller.translator import CreateTranslatorController, GetTranslatorController
from repositories.translator import TranslatorRepository
from use_cases.translator import CreateTranslatorUseCase, GetTranslatorUseCase


class GetTranslatorControllerFactory:
    @staticmethod
    def create() -> GetTranslatorController:
        repo = TranslatorRepository()
        use_case = GetTranslatorUseCase(repo)
        return GetTranslatorController(use_case)


class CreateTranslatorControllerFactory:
    @staticmethod
    def create() -> CreateTranslatorController:
        repo = TranslatorRepository()
        use_case = CreateTranslatorUseCase(repo)
        return CreateTranslatorController(use_case)
