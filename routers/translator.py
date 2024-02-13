from fastapi import APIRouter, Response
from api_types import TranslatorCreateAPI

from factories.translator import (
    CreateTranslatorControllerFactory,
    GetTranslatorControllerFactory,
)


router = APIRouter(prefix="/translators")


@router.get("/{translator_id}")
def get(translator_id: int, response: Response):
    translator_controller = GetTranslatorControllerFactory.create()
    body, status = translator_controller.get(translator_id)
    response.status_code = status
    return body


@router.post("/")
def create(translator: TranslatorCreateAPI, response: Response):
    translator_controller = CreateTranslatorControllerFactory.create()
    body, status = translator_controller.create(translator.dict())
    response.status_code = status
    return body
