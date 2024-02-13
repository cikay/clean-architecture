from dataclasses import asdict
from entities.translator import Translator
from models.translator import TranslatorDB
from repositories.base import BaseRepository


class TranslatorRepository(BaseRepository[TranslatorDB, Translator]):
    def get(self, translator_id: int) -> Translator | None:
        translator_db = TranslatorDB.get_or_none(TranslatorDB.id == translator_id)
        if not translator_db:
            return None

        return self.to_entity(translator_db)

    def create(self, translator: Translator) -> Translator:
        translator_dict = asdict(translator)
        translator_db = TranslatorDB.create(**translator_dict)
        return self.to_entity(translator_db)
