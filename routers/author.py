from fastapi import APIRouter, Response
from api_types import AuthorCreateAPI

from factories.author import (
    CreateAuthorControllerFactory,
    GetAuthorControllerFactory,
)


router = APIRouter(prefix="/authors")


@router.get("/{author_id}")
async def get(author_id: int, response: Response):
    author_controller = GetAuthorControllerFactory.create()
    import ipdb; ipdb.set_trace()
    body, status = await author_controller.get(author_id)
    response.status_code = status
    return body


@router.post("/")
async def create(author: AuthorCreateAPI, response: Response):
    author_controller = CreateAuthorControllerFactory.create()
    body, status = await author_controller.create(author.dict())
    response.status_code = status
    return body
