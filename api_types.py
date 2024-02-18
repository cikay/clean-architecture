from typing import get_type_hints

from pydantic import create_model
from entities.author import AuthorCreate

from entities.discipline import DisciplineCreate, DisciplineQuery
from entities.translator import TranslatorCreate


def create_api_type(entity_type, type_name):
    exclude_fields = {"created_at", "updated_at"}
    hints = get_type_hints(entity_type)
    api_hints = {
        key: (value, ...) for key, value in hints.items() if key not in exclude_fields
    }

    return create_model(type_name, **api_hints)


DisciplineCreateAPI = create_api_type(DisciplineCreate, "DisciplineCreateAPI")
AuthorCreateAPI = create_api_type(AuthorCreate, "AuthorCreateAPI")
TranslatorCreateAPI = create_api_type(TranslatorCreate, "TranslatorCreateAPI")
DisciplineQueryAPI = create_api_type(DisciplineQuery, "DisciplineQueryAPI")
