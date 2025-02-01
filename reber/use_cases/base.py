from abc import abstractmethod, ABC
from typing import Any


class GetUseCase(ABC):
    @abstractmethod
    def execute(self, id) -> dict:
        pass


class GetManyUseCase(ABC):
    @abstractmethod
    def execute(self, id) -> dict:
        pass


class BaseCreateUseCase(ABC):
    @abstractmethod
    def execute(self, create_type: Any):
        pass
