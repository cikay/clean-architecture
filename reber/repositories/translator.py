from dataclasses import asdict

from reber.entities.translator import Translator
from reber.models.translator import TranslatorDB
from reber.repositories.base import BaseRepository


class TranslatorRepository(BaseRepository[TranslatorDB, Translator]):
    async def create(self, translator: Translator) -> Translator:
        fields = asdict(translator)
        discipline_db = await TranslatorDB.create(**fields)
        return self.to_entity(discipline_db)
