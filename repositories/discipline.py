from dataclasses import asdict

from entities.discipline import Discipline, DisciplineQuery
from models.discipline import DisciplineDB
from repositories.base import BaseRepository


class DisciplineRepository(BaseRepository[DisciplineDB, Discipline]):
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
