from dataclasses import asdict

from entities.discipline import Discipline, DisciplineQuery
from reber.models.discipline import DisciplineDB
from repositories.base import BaseRepository


class DisciplineRepository(BaseRepository[DisciplineDB, Discipline]):
    async def get_many(self) -> list[Discipline]:
        disciplines = await DisciplineDB.all()
        return [self.to_entity(discipline) for discipline in disciplines]
