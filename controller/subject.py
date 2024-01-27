from use_cases.subject import CreateSubjectUseCase, GetSubjectUseCase
from entities.subject import SubjectCreate


class GetSubjectController:
    def __init__(self, use_case: GetSubjectUseCase):
        self.use_case = use_case

    def get(self, subject_id) -> tuple[dict, int]:
        return self.use_case.execute(subject_id), 200


class CreateSubjectController:
    def __init__(self, use_case: CreateSubjectUseCase):
        self.use_case = use_case

    def create(self, subject: dict) -> tuple[dict, int]:
        subject_instance = SubjectCreate(**subject)
        return self.use_case.execute(subject_instance), 201
