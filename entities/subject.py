from dataclasses import dataclass

from base_entity import BaseEntity


@dataclass
class SubjectCreate(BaseEntity):
    name: str


@dataclass
class Subject(SubjectCreate):
    id: str

    # domain business logic goes here
