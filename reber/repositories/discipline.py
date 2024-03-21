from dataclasses import asdict

from reber.entities.discipline import Discipline, DisciplineCreate
from reber.models.discipline import DisciplineDB
from reber.repositories.base import BaseRepository


class DisciplineRepository(BaseRepository[DisciplineDB, Discipline]):
    async def get_many(self) -> list[Discipline]:
        disciplines = await DisciplineDB.all()
        return [self.to_entity(discipline) for discipline in disciplines]

    async def create(self, discipline: DisciplineCreate) -> Discipline:
        fields = asdict(discipline)
        discipline_db = await DisciplineDB.create(**fields)
        return self.to_entity(discipline_db)
