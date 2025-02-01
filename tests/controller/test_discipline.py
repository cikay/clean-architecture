from dataclasses import asdict

import pytest

from reber.factories.discipline import (
    CreateDisciplineControllerFactory,
    GetDisciplineControllerFactory,
    GetManyDisciplineControllerFactory,
)
from reber.use_cases.discipline import (
    CreateDisciplineUseCase,
    GetDisciplineUseCase,
    GetManyDisciplineUseCase,
)


@pytest.mark.asyncio
async def test_create_discipline_controller(mocker, discipline):
    mock_execute_func = mocker.patch.object(CreateDisciplineUseCase, "execute")
    mock_execute_func.return_value = discipline

    controller = CreateDisciplineControllerFactory.create()

    result_discipline, status = await controller.execute(
        {"name": discipline.name, "interlanguage_discipline_id": 1}
    )
    expected_discipline = asdict(discipline)
    assert status == 201
    assert result_discipline == expected_discipline


@pytest.mark.asyncio
async def test_get_discipline_controller(mocker, discipline):
    mock_execute_func = mocker.patch.object(GetDisciplineUseCase, "execute")
    mock_execute_func.return_value = discipline

    controller = GetDisciplineControllerFactory.create()

    result_discipline, status = await controller.execute(1)
    discipline_dict = asdict(discipline)

    assert status == 200
    assert result_discipline == discipline_dict


@pytest.mark.asyncio
async def test_get_many_discipline_controller(mocker, discipline):
    mock_execute_func = mocker.patch.object(GetManyDisciplineUseCase, "execute")

    expected_disciplines = [asdict(discipline)]
    mock_execute_func.return_value = [discipline]

    controller = GetManyDisciplineControllerFactory.create()

    result_discipline, status = await controller.execute()

    assert status == 200
    assert result_discipline == expected_disciplines
