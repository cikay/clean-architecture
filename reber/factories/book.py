from reber.controller.book import CreateBookController, GetBookController
from reber.repositories.book import BookRepository
from reber.use_cases.book import CreateBookUseCase, GetBookUseCase


class GetBookControllerFactory:
    @staticmethod
    def create() -> GetBookController:
        repo = BookRepository()
        use_case = GetBookUseCase(repo)
        return GetBookController(use_case)


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
