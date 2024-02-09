from datetime import datetime
from dataclasses import dataclass, field


from base_entity import BaseCreateEntity


@dataclass
class DisciplineCreate(BaseCreateEntity):
    name: str


@dataclass
class Discipline:
    id: str
    name: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    # domain business logic goes here


@dataclass
class DisciplineQuery:
    pass
