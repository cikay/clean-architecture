from entities.discipline import Discipline, DisciplineQuery
from models.discipline import DisciplineDB


class DisciplineRepository:
    def get(self, discipline_id: int) -> Discipline:
        discipline_db = DisciplineDB.get(DisciplineDB.id == discipline_id)
        return Discipline(
            id=discipline_db.id,
            name=discipline_db.name,
            created_at=discipline_db.created_at,
            updated_at=discipline_db.updated_at,
        )

    def create(self, discipline: Discipline) -> Discipline:
        discipline_db = DisciplineDB.create(name=discipline.name)
        return Discipline(
            id=discipline_db.id,
            name=discipline_db.name,
            created_at=discipline_db.created_at,
            updated_at=discipline_db.updated_at,
        )

    def get_many(self, query: DisciplineQuery) -> list[Discipline]:
        disciplines = DisciplineDB.select()
        return [
            Discipline(
                id=discipline.id,
                name=discipline.name,
                created_at=discipline.created_at,
                updated_at=discipline.updated_at,
            )
            for discipline in disciplines
        ]
