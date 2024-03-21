import pytest

from reber.entities.author import Author
from reber.entities.discipline import Discipline
from reber.entities.interlanguage_discipline import InterLanguageDiscipline
from reber.entities.translator import Translator


@pytest.fixture
def interlanguage_discipline():
    return InterLanguageDiscipline(
        id=1,
        name="Computer Science",
        created_at="2024-03-15T19:33:59.997598",
        updated_at="2024-03-15T19:33:59.997598",
    )


@pytest.fixture
def discipline(interlanguage_discipline):
    return Discipline(
        id=1,
        name="Computer Science",
        interlanguage_discipline_id=interlanguage_discipline.id,
        interlanguage_discipline=interlanguage_discipline,
        created_at="2024-03-15T19:33:59.997598",
        updated_at="2024-03-15T19:33:59.997598",
    )


@pytest.fixture
def author():
    return Author(
        id=1,
        firstname="John",
        lastname="Doe",
        created_at="2024-03-15T19:33:59.997598",
        updated_at="2024-03-15T19:33:59.997598",
    )


@pytest.fixture
def translator():
    return Translator(
        id=1,
        firstname="John",
        lastname="Doe",
        created_at="2024-03-15T19:33:59.997598",
        updated_at="2024-03-15T19:33:59.997598",
    )
