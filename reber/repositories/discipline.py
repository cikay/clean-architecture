from dataclasses import asdict

from reber.entities.discipline import Discipline, DisciplineCreate
from reber.models.discipline import DisciplineDB
from reber.repositories.base import BaseRepository


class DisciplineRepository(BaseRepository[DisciplineDB, Discipline]):
    async def get(
        self, id: int, relational_fields: None | set = None
    ) -> Discipline | None:
        db_type = self._get_db_type()
        if relational_fields:
            db_instance = (
                await db_type.filter(id=id).prefetch_related(*relational_fields).first()
            )
        else:
            db_instance = await db_type.filter(id=id).first()

        if not db_instance:
            return None

        return self.to_entity(db_instance, relational_fields)

    async def get_many(self, relational_fields: set | None = None) -> list[Discipline]:
        if relational_fields:
            disciplines = await DisciplineDB.all().prefetch_related(*relational_fields)
        else:
            disciplines = await DisciplineDB.all()

        return [self.to_entity(discipline) for discipline in disciplines]

    async def create(self, discipline: DisciplineCreate) -> Discipline:
        fields = asdict(discipline)
        discipline_db = await DisciplineDB.create(**fields)
        discipline_db = await DisciplineDB.get(id=discipline_db.id).prefetch_related(
            "sub_disciplines", "parent_discipline", "interlanguage_discipline"
        )
        return self.to_entity(discipline_db)
