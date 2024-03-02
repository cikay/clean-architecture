from dataclasses import asdict
from entities.interlanguage_discipline import InterLanguageDiscipline
from models.interlanguage_discipline import InterLanguageDisciplineDB
from repositories.base import BaseRepository


class InterLanguageDisciplineRepository(
    BaseRepository[InterLanguageDisciplineDB, InterLanguageDiscipline]
):
    async def get_many(self) -> list[InterLanguageDiscipline]:
        disciplines = await InterLanguageDisciplineDB.all()
        return [self.to_entity(discipline) for discipline in disciplines]

    async def create(
        self, interlanguage_discipline: InterLanguageDiscipline
    ) -> InterLanguageDiscipline:
        fields = asdict(interlanguage_discipline)
        discipline_db = await InterLanguageDisciplineDB.create(**fields)
        return self.to_entity(discipline_db)
