from datetime import datetime
from dataclasses import dataclass, field


from reber.base_entity import BaseCreateEntity


@dataclass
class AuthorCreate(BaseCreateEntity):
    firstname: str
    lastname: str


@dataclass
class Author:
    id: str
    firstname: str
    lastname: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    # domain business logic goes here


@dataclass
class AuthorQuery:
    pass
