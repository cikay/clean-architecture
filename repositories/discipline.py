from dataclasses import asdict

from entities.discipline import Discipline, DisciplineQuery
from models.discipline import DisciplineDB
from repositories.base import BaseRepository


class DisciplineRepository(BaseRepository[DisciplineDB, Discipline]):
    def get(self, discipline_id: int) -> Discipline | None:
        discipline_db = DisciplineDB.get_or_none(DisciplineDB.id == discipline_id)
        if not discipline_db:
            return None

        return self.to_entity(discipline_db)

    def create(self, discipline: Discipline) -> Discipline:
        discipline_dict = asdict(discipline)
        discipline_db = DisciplineDB.create(**discipline_dict)
        return self.to_entity(discipline_db)

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
