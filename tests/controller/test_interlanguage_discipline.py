from dataclasses import asdict

import pytest

from reber.factories.interlanguage_discipline import (
    CreateInterLanguageDisciplineControllerFactory,
    GetInterLanguageDisciplineControllerFactory,
    GetManyInterLanguageDisciplineControllerFactory,
)
from reber.use_cases.interlanguage_discipline import (
    CreateInterLanguageDisciplineUseCase,
    GetInterLanguageDisciplineUseCase,
    GetManyInterLanguageDisciplineUseCase,
)


@pytest.mark.asyncio
async def test_create_interlanguage_discipline_controller(
    mocker, interlanguage_discipline
):
    mock_execute_func = mocker.patch.object(
        CreateInterLanguageDisciplineUseCase, "execute"
    )
    mock_execute_func.return_value = interlanguage_discipline

    controller = CreateInterLanguageDisciplineControllerFactory.create()

    result_interlanguage_discipline, status = await controller.execute(
        {"name": interlanguage_discipline.name}
    )
    expected_interlanguage_discipline = asdict(interlanguage_discipline)

    assert status == 201
    assert result_interlanguage_discipline == expected_interlanguage_discipline


@pytest.mark.asyncio
async def test_get_interlanguage_discipline_controller(
    mocker, interlanguage_discipline
):
    mock_execute_func = mocker.patch.object(
        GetInterLanguageDisciplineUseCase, "execute"
    )
    mock_execute_func.return_value = interlanguage_discipline

    controller = GetInterLanguageDisciplineControllerFactory.create()

    result_interlanguage_discipline, status = await controller.execute(1)
    expected_interlanguage_discipline = asdict(interlanguage_discipline)

    assert status == 200
    assert result_interlanguage_discipline == expected_interlanguage_discipline


@pytest.mark.asyncio
async def test_get_many_interlanguage_discipline_controller(
    mocker, interlanguage_discipline
):
    mock_execute_func = mocker.patch.object(
        GetManyInterLanguageDisciplineUseCase, "execute"
    )

    expected_interlanguage_disciplines = [asdict(interlanguage_discipline)]
    mock_execute_func.return_value = [interlanguage_discipline]

    controller = GetManyInterLanguageDisciplineControllerFactory.create()

    result_interlanguage_discipline, status = await controller.execute()

    assert status == 200
    assert result_interlanguage_discipline == expected_interlanguage_disciplines
