import pytest

from reber.repositories.translator import (
    TranslatorRepository,
)
from reber.use_cases.translator import (
    CreateTranslatorUseCase,
    GetTranslatorUseCase,
    GetManyTranslatorUseCase,
)
from reber.entities.translator import (
    TranslatorCreate,
)


@pytest.mark.asyncio
async def test_create_translator(mocker, translator):
    create_func = mocker.patch.object(TranslatorRepository, "create")
    create_func.return_value = translator
    repo = TranslatorRepository()
    use_case = CreateTranslatorUseCase(repo)

    translator_create = TranslatorCreate(
        firstname=translator.firstname, lastname=translator.lastname
    )
    result_translator = await use_case.execute(translator_create)
    assert result_translator == translator


@pytest.mark.asyncio
async def test_get_translator(mocker, translator):
    get_func = mocker.patch.object(TranslatorRepository, "get")
    get_func.return_value = translator
    repo = TranslatorRepository()
    use_case = GetTranslatorUseCase(repo)

    result_translator = await use_case.execute(1)
    assert result_translator == translator


@pytest.mark.asyncio
async def test_get_many_translator(mocker, translator):
    get_func = mocker.patch.object(TranslatorRepository, "get_many")
    expected_translators = [translator]
    get_func.return_value = expected_translators
    repo = TranslatorRepository()
    use_case = GetManyTranslatorUseCase(repo)

    result_translators = await use_case.execute()
    assert result_translators == expected_translators
