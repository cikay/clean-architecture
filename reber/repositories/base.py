import types
from typing import get_type_hints


def get_repository(model_name: str):
    from reber.repositories.discipline import DisciplineRepository
    from reber.repositories.interlanguage_discipline import (
        InterLanguageDisciplineRepository,
    )
    from reber.repositories.author import AuthorRepository

    model_name_to_repo_mapping = {
        "AuthorDB": AuthorRepository,
        "DisciplineDB": DisciplineRepository,
        "InterLanguageDisciplineDB": InterLanguageDisciplineRepository,
    }

    return model_name_to_repo_mapping[model_name]


class BaseRepository[Tdb, Tentity]:
    async def get(self, id: int) -> Tentity | None:
        db_type = self._get_db_type()
        db_instance = await db_type.filter(id=id).first()
        if not db_instance:
            return None

        return self.to_entity(db_instance)

    async def get_many(self, ids):
        db_type = self._get_db_type()
        objects = await db_type.filter(id__in=ids)
        return [self.to_entity(o) for o in objects]

    def to_entity(self, db_instance: Tdb) -> Tentity:
        fields_name = self._get_entity_fields()
        entity_type = self._get_entity_type()
        m2m_fields = db_instance.get_m2m_fields()
        foreign_key_fields = db_instance.get_foreign_key_fields()
        fields = {}
        for field_name in fields_name:
            if field_name in m2m_fields:
                m2m_instances = getattr(db_instance, field_name)
                fields[field_name] = self.convert_m2m_field(m2m_instances)
            elif field_name in foreign_key_fields:
                foreign_key_db_instance = getattr(db_instance, field_name)
                if foreign_key_db_instance:
                    fields[field_name] = self._convert_foreign_key_field(
                        foreign_key_db_instance
                    )
                else:
                    fields[field_name] = None
            else:
                fields[field_name] = getattr(db_instance, field_name)

        return entity_type(**fields)

    def convert_m2m_field(self, instances):
        if not instances:
            return []

        klass = instances[0].__class__
        klass_name = klass.__name__
        m2m_field_model_repo = get_repository(klass_name)
        m2m_field_model_fields_name = m2m_field_model_repo()._get_entity_fields()

        entities = []
        for instance in instances:
            entities.append(
                klass(**{f: getattr(instance, f) for f in m2m_field_model_fields_name})
            )

        return entities

    def _convert_foreign_key_field(self, instance):
        klass = instance.__class__
        klass_name = klass.__name__
        repo = get_repository(klass_name)
        foreign_key_field_instance_fields = repo()._get_entity_fields()
        return klass(
            **{f: getattr(instance, f) for f in foreign_key_field_instance_fields}
        )

    def _get_entity_fields(self) -> set[str]:
        entity_type = self._get_entity_type()
        hints = get_type_hints(entity_type)
        fields = hints.keys()
        return set(fields)

    @classmethod
    def _get_db_type(cls) -> Tdb:
        return types.get_original_bases(cls)[0].__args__[0]

    @classmethod
    def _get_entity_type(cls) -> Tentity:
        return types.get_original_bases(cls)[0].__args__[1]
