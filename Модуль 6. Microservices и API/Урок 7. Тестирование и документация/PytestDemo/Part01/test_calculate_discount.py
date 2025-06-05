import pytest
from calculate_discount import calculate_discount

def test_valid_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(200, 0) == 200
    assert calculate_discount(100, 100) == 0

# Негативные тесты
def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, -10)
    with pytest.raises(ValueError):
        calculate_discount(100, 110)

def test_discount_with_float():
    assert calculate_discount(100.0, 10) == 90.0
    assert calculate_discount(50.0, 25) == 37.5