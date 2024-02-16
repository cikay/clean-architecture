from dataclasses import asdict

from entities.discipline import Discipline, DisciplineQuery
from models.discipline import DisciplineDB
from repositories.base import BaseRepository


class DisciplineRepository(BaseRepository[DisciplineDB, Discipline]):
    async def get(self, discipline_id: int) -> Discipline | None:
        discipline_db = await DisciplineDB.filter(id=discipline_id).first()
        if not discipline_db:
            return None

        return self.to_entity(discipline_db)

    async def create(self, discipline: Discipline) -> Discipline:
        discipline_dict = asdict(discipline)
        discipline_db = await DisciplineDB.create(**discipline_dict)
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
