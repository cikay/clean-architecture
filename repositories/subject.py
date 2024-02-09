from entities.subject import Subject
from models.subject import SubjectDB


class SubjectRepository:
    def get(self, subject_id: int) -> Subject:
        return SubjectDB.get(SubjectDB.id == subject_id)

    def create(self, subject: Subject) -> Subject:
        subject_db = SubjectDB.create(name=subject.name)
        return Subject(
            id=subject_db.id,
            name=subject_db.name,
            created_at=subject_db.created_at,
            updated_at=subject_db.updated_at,
        )
