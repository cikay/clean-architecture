import pytest

from reber.repositories.interlanguage_discipline import (
    InterLanguageDisciplineRepository,
)
from reber.use_cases.interlanguage_discipline import (
    CreateInterLanguageDisciplineUseCase,
)
from reber.entities.interlanguage_discipline import (
    InterLanguageDisciplineCreate,
    InterLanguageDiscipline,
)


@pytest.mark.asyncio
async def test_create_interlanguage_discipline(mocker):
    create_func = mocker.patch.object(InterLanguageDisciplineRepository, "create")
    expected_interlanguage_discipline = InterLanguageDiscipline(
        id=1,
        name="Computer Science",
        created_at="2024-03-15T19:33:59.997598",
        updated_at="2024-03-15T19:33:59.997598",
    )
    create_func.return_value = expected_interlanguage_discipline
    repo = InterLanguageDisciplineRepository()
    use_case = CreateInterLanguageDisciplineUseCase(repo)

    interlanguage_discipline_create = InterLanguageDisciplineCreate(
        name="Computer Science"
    )
    result_interlanguage_discipline = await use_case.execute(
        interlanguage_discipline_create
    )
    assert result_interlanguage_discipline == expected_interlanguage_discipline
