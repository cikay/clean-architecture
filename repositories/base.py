import types
from typing import get_type_hints


class BaseRepository[Tdb, Tentity]:
    def to_entity(self, db_instance: Tdb) -> Tentity:
        entity_type = types.get_original_bases(self.__class__)[0].__args__[1]
        hints = get_type_hints(entity_type)
        return entity_type(**{k: getattr(db_instance, k) for k in hints.keys()})
