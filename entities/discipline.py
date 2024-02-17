from datetime import datetime
from dataclasses import dataclass


@dataclass
class DisciplineCreate:
    name: str


@dataclass
class Discipline:
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    # domain business logic goes here


@dataclass
class DisciplineQuery:
    pass
