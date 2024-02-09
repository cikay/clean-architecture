from fastapi import APIRouter, Response

from factories.discipline import (
    CreateDisciplineControllerFactory,
    GetDisciplineControllerFactory,
)


router = APIRouter(prefix="/disciplines")


@router.get("/{discipline_id}")
def get(discipline_id: int, response: Response):
    discipline_controller = GetDisciplineControllerFactory.create()
    body, status = discipline_controller.get(discipline_id)
    response.status_code = status
    return body


@router.post("/")
def create(discipline: dict, response: Response):
    discipline_controller = CreateDisciplineControllerFactory.create()
    body, status = discipline_controller.create(discipline)
    response.status_code = status
    return body
