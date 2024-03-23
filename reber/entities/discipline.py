from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass, field

from reber.entities.interlanguage_discipline import InterLanguageDiscipline


@dataclass
class DisciplineCreate:
    name: str


@dataclass
class Discipline:
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    interlanguage_discipline_id: int
    interlanguage_discipline: InterLanguageDiscipline | None


@dataclass
class DisciplineQuery:
    pass
