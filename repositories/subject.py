from entities.subject import Subject


class SubjectRepository:
    def get(self, subject_id: int) -> Subject:
        return {"subject_id": subject_id, "name": "Math"}

    def create(self, subject: Subject) -> Subject:
        return subject
