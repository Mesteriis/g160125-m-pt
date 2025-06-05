import pytest
from add import add


def test_add():
    assert add(2, 4) == 6
    assert add(-3, 4) == 1
    assert add(12, 8) == 20
    assert add(-2, -8) == -10
    assert add(0, 0) == 0
    assert add(-5, 0) == -5
