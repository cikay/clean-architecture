from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass, field

from reber.entities.interlanguage_discipline import InterLanguageDiscipline


@dataclass
class DisciplineCreate:
    name: str
    interlanguage_discipline_id: int
    parent_discipline_id: int | None = field(default=None)


@dataclass
class Discipline:
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    interlanguage_discipline_id: int
    interlanguage_discipline: InterLanguageDiscipline | None = field(default=None)
    parent_discipline: Discipline | None = field(default=None)
    parent_discipline_id: int | None = field(default=None)
    sub_disciplines: list[Discipline] = field(default_factory=list)


@dataclass
class DisciplineQuery:
    pass
