from abc import abstractmethod

from reber.use_cases.base import GetUseCase, GetManyUseCase


class GetController:
    def __init__(self, use_case: GetUseCase):
        self.use_case = use_case

    @abstractmethod
    async def execute(self, id: int) -> tuple[dict, int]:
        pass


class GetManyController:
    def __init__(self, use_case: GetUseCase):
        self.use_case = use_case

    @abstractmethod
    async def execute(self) -> tuple[dict, int]:
        pass
