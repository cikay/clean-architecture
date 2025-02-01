import pytest

from reber.repositories.discipline import (
    DisciplineRepository,
)
from reber.use_cases.discipline import (
    CreateDisciplineUseCase,
    GetDisciplineUseCase,
    GetManyDisciplineUseCase,
)
from reber.entities.discipline import (
    DisciplineCreate,
)


@pytest.mark.asyncio
async def test_create_discipline(mocker, discipline):
    create_func = mocker.patch.object(DisciplineRepository, "create")
    create_func.return_value = discipline
    repo = DisciplineRepository()
    use_case = CreateDisciplineUseCase(repo)

    discipline_create = DisciplineCreate(
        name="Computer Science", interlanguage_discipline_id=1
    )
    result_discipline = await use_case.execute(discipline_create)
    assert result_discipline == discipline


@pytest.mark.asyncio
async def test_get_discipline(mocker, discipline):
    get_func = mocker.patch.object(DisciplineRepository, "get")
    get_func.return_value = discipline
    repo = DisciplineRepository()
    use_case = GetDisciplineUseCase(repo)

    result_discipline = await use_case.execute(1)
    assert result_discipline == discipline


@pytest.mark.asyncio
async def test_get_many_discipline(mocker, discipline):
    get_func = mocker.patch.object(DisciplineRepository, "get_many")
    expected_disciplines = [discipline]
    get_func.return_value = expected_disciplines
    repo = DisciplineRepository()
    use_case = GetManyDisciplineUseCase(repo)

    result_disciplines = await use_case.execute()
    assert result_disciplines == expected_disciplines
