from fastapi import APIRouter, Response
from reber.api_types import BookCreateAPI

from reber.factories.book import (
    CreateBookControllerFactory,
    GetBookControllerFactory,
)


router = APIRouter(prefix="/books")


@router.get("/")
async def get(book_id: int, response: Response):
    book_controller = GetBookControllerFactory.create()
    body, status = await book_controller.get(book_id)
    response.status_code = status
    return body


@router.get("/{id}")
async def get_many(book_id: int, response: Response):
    book_controller = GetManyBookControllerFactory.create()
    body, status = await book_controller.get(book_id)
    response.status_code = status
    return body


@router.post("/")
async def create(book: BookCreateAPI, response: Response): 
    book_controller = CreateBookControllerFactory.create()
    body, status = await book_controller.create(book.dict())
    response.status_code = status
    return body
