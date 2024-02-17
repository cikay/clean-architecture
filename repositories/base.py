import types
from typing import get_type_hints
from dataclasses import asdict


class BaseRepository[Tdb, Tentity]:
    def to_entity(self, db_instance: Tdb) -> Tentity:
        entity_type = types.get_original_bases(self.__class__)[0].__args__[1]
        hints = get_type_hints(entity_type)
        return entity_type(**{k: getattr(db_instance, k) for k in hints.keys()})

    async def create(self, fields: Tdb) -> Tentity:
        fields_dict = asdict(fields)
        db_type = types.get_original_bases(self.__class__)[0].__args__[0]
        db_instance = db_type(**fields_dict)
        await db_instance.save()
        return self.to_entity(db_instance)

    async def get(self, id: int) -> Tentity | None:
        db_type = types.get_original_bases(self.__class__)[0].__args__[0]
        db_instance = await db_type.filter(id=id).first()
        if not db_instance:
            return None

        return self.to_entity(db_instance)
