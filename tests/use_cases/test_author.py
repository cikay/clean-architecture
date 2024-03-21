import pytest

from reber.repositories.author import (
    AuthorRepository,
)
from reber.use_cases.author import (
    CreateAuthorUseCase,
    GetAuthorUseCase,
    GetManyAuthorUseCase,
)
from reber.entities.author import (
    AuthorCreate,
)


@pytest.mark.asyncio
async def test_create_author(mocker, author):
    create_func = mocker.patch.object(AuthorRepository, "create")
    create_func.return_value = author
    repo = AuthorRepository()
    use_case = CreateAuthorUseCase(repo)

    author_create = AuthorCreate(firstname=author.firstname, lastname=author.lastname)
    result_author = await use_case.execute(author_create)
    assert result_author == author


@pytest.mark.asyncio
async def test_get_author(mocker, author):
    get_func = mocker.patch.object(AuthorRepository, "get")
    get_func.return_value = author
    repo = AuthorRepository()
    use_case = GetAuthorUseCase(repo)

    result_author = await use_case.execute(1)
    assert result_author == author


@pytest.mark.asyncio
async def test_get_many_author(mocker, author):
    get_func = mocker.patch.object(AuthorRepository, "get_many")
    expected_authors = [author]
    get_func.return_value = expected_authors
    repo = AuthorRepository()
    use_case = GetManyAuthorUseCase(repo)

    result_authors = await use_case.execute()
    assert result_authors == expected_authors
