from base_use_case import BaseUseCase
from repositories.subject import SubjectRepository
from entities.subject import Subject, SubjectCreate


class CreateSubjectUseCase(BaseUseCase):
    def __init__(self, repo: SubjectRepository):
        self.repo = repo

    def execute(self, subject: SubjectCreate):
        return self.repo.create(subject)


class GetSubjectUseCase(BaseUseCase):
    def __init__(self, repo: SubjectRepository):
        self.repo = repo

    def execute(self, subject_id: int):
        return self.repo.get(subject_id)
