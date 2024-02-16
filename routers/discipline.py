from fastapi import APIRouter, Response

from factories.discipline import (
    CreateDisciplineControllerFactory,
    GetDisciplineControllerFactory,
)
from api_types import DisciplineCreateAPI

router = APIRouter(prefix="/disciplines")


@router.get("/{discipline_id}")
async def get(discipline_id: int, response: Response):
    discipline_controller = GetDisciplineControllerFactory.create()
    body, status = await discipline_controller.get(discipline_id)
    response.status_code = status
    return body


@router.post("/")
async def create(discipline: DisciplineCreateAPI, response: Response):
    discipline_controller = CreateDisciplineControllerFactory.create()
    body, status = await discipline_controller.create(discipline.dict())
    response.status_code = status
    return body
