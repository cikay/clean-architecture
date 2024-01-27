from controller.subject import CreateSubjectController, GetSubjectController
from repositories.subject import SubjectRepository
from use_cases.subject import CreateSubjectUseCase, GetSubjectUseCase


class GetSubjectControllerFactory:
    @staticmethod
    def create() -> GetSubjectController:
        repo = SubjectRepository()
        use_case = GetSubjectUseCase(repo)
        return GetSubjectController(use_case)


class CreateSubjectControllerFactory:
    @staticmethod
    def create() -> CreateSubjectController:
        repo = SubjectRepository()
        use_case = CreateSubjectUseCase(repo)
        return CreateSubjectController(use_case)
