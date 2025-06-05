import pytest
from add import add


def test_add():
    assert add(2, 4) == 6
    assert add(-3, 4) == 1
    assert add(12, 8) == 20


# Более компактный и удобный запуск тестов
@pytest.mark.parametrize("a, b, expected", [
    (2, 4, 6), (-3, 4, 1), (12, 8, 20)
])
def test_add_with_param(a, b, expected):
    assert add(a, b) == expected


def test_add_invalid_data():
    with pytest.raises(TypeError):
        add("hello", 10)


# pytest -v Part02