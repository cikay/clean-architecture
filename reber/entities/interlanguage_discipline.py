from datetime import datetime
from dataclasses import dataclass


@dataclass
class InterLanguageDisciplineCreate:
    name: str


@dataclass
class InterLanguageDiscipline:
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    # domain business logic goes here


@dataclass
class InterLanguageDisciplineQuery:
    pass
