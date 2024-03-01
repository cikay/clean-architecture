from controller.book import CreateBookController, GetBookController
from repositories.book import BookRepository
from use_cases.book import CreateBookUseCase, GetBookUseCase


class GetBookControllerFactory:
    @staticmethod
    def create() -> GetBookController:
        repo = BookRepository()
        use_case = GetBookUseCase(repo)
        return GetBookController(use_case)


class CreateBookControllerFactory:
    @staticmethod
    def create() -> CreateBookController:
        repo = BookRepository()
        use_case = CreateBookUseCase(repo)
        return CreateBookController(use_case)
