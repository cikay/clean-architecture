from fastapi import APIRouter, Response

from factories.subject import (
    CreateSubjectControllerFactory,
    GetSubjectControllerFactory,
)


router = APIRouter(prefix="/subjects")


@router.get("/{subject_id}")
def get(subject_id: int, response: Response):
    subject_controller = GetSubjectControllerFactory.create()
    body, status = subject_controller.get(subject_id)
    response.status_code = status
    return body


@router.post("/")
def create(subject: dict, response: Response):
    subject_controller = CreateSubjectControllerFactory.create()
    body, status = subject_controller.create(subject)
    response.status_code = status
    return body
