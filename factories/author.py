from controller.author import CreateAuthorController, GetAuthorController
from repositories.author import AuthorRepository
from use_cases.author import CreateAuthorUseCase, GetAuthorUseCase


class GetAuthorControllerFactory:
    @staticmethod
    def create() -> GetAuthorController:
        repo = AuthorRepository()
        use_case = GetAuthorUseCase(repo)
        return GetAuthorController(use_case)


class CreateAuthorControllerFactory:
    @staticmethod
    def create() -> CreateAuthorController:
        repo = AuthorRepository()
        use_case = CreateAuthorUseCase(repo)
        return CreateAuthorController(use_case)
