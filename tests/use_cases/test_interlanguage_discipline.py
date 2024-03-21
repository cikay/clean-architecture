import pytest

from reber.repositories.interlanguage_discipline import (
    InterLanguageDisciplineRepository,
)
from reber.use_cases.interlanguage_discipline import (
    CreateInterLanguageDisciplineUseCase,
    GetInterLanguageDisciplineUseCase,
    GetManyInterLanguageDisciplineUseCase,
)
from reber.entities.interlanguage_discipline import (
    InterLanguageDisciplineCreate,
)


@pytest.mark.asyncio
async def test_create_interlanguage_discipline(mocker, interlanguage_discipline):
    create_func = mocker.patch.object(InterLanguageDisciplineRepository, "create")
    create_func.return_value = interlanguage_discipline
    repo = InterLanguageDisciplineRepository()
    use_case = CreateInterLanguageDisciplineUseCase(repo)

    interlanguage_discipline_create = InterLanguageDisciplineCreate(
        name="Computer Science"
    )
    result_interlanguage_discipline = await use_case.execute(
        interlanguage_discipline_create
    )
    assert result_interlanguage_discipline == interlanguage_discipline


@pytest.mark.asyncio
async def test_get_interlanguage_discipline(mocker, interlanguage_discipline):
    get_func = mocker.patch.object(InterLanguageDisciplineRepository, "get")
    get_func.return_value = interlanguage_discipline
    repo = InterLanguageDisciplineRepository()
    use_case = GetInterLanguageDisciplineUseCase(repo)

    result_interlanguage_discipline = await use_case.execute(1)
    assert result_interlanguage_discipline == interlanguage_discipline


@pytest.mark.asyncio
async def test_get_many_interlanguage_discipline(mocker, interlanguage_discipline):
    get_func = mocker.patch.object(InterLanguageDisciplineRepository, "get_many")
    expected_interlanguage_disciplines = [interlanguage_discipline]
    get_func.return_value = expected_interlanguage_disciplines
    repo = InterLanguageDisciplineRepository()
    use_case = GetManyInterLanguageDisciplineUseCase(repo)

    result_interlanguage_disciplines = await use_case.execute()
    assert result_interlanguage_disciplines == expected_interlanguage_disciplines
