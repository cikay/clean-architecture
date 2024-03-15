from fastapi import APIRouter, Response

from factories.interlanguage_discipline import (
    CreateInterLanguageDisciplineControllerFactory,
    GetInterLanguageDisciplineControllerFactory,
    GetManyInterLanguageDisciplineControllerFactory,
)
from reber.api_types import InterLanguageDisciplineCreateAPI

router = APIRouter(prefix="/interlanguage_disciplines")


@router.get("/{id}")
async def get(id: int, response: Response):
    discipline_controller = GetInterLanguageDisciplineControllerFactory.create()
    body, status = await discipline_controller.get(id)
    response.status_code = status
    return body


@router.get("/")
async def get_many(response: Response):
    discipline_controller = GetManyInterLanguageDisciplineControllerFactory.create()
    body, status = await discipline_controller.get_many()
    response.status_code = status
    return body


@router.post("/")
async def create(
    interlanguage_discipline: InterLanguageDisciplineCreateAPI, response: Response
):
    discipline_controller = CreateInterLanguageDisciplineControllerFactory.create()
    body, status = await discipline_controller.create(interlanguage_discipline.dict())
    response.status_code = status
    return body
