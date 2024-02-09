from datetime import datetime
from dataclasses import dataclass, field


from base_entity import BaseCreateEntity


@dataclass
class SubjectCreate(BaseCreateEntity):
    name: str


@dataclass
class Subject:
    id: str
    name: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


    # domain business logic goes here
