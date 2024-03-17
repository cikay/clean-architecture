from dataclasses import asdict
from entities.translator import Translator
from reber.models.translator import TranslatorDB
from repositories.base import BaseRepository


class TranslatorRepository(BaseRepository[TranslatorDB, Translator]):
    pass
