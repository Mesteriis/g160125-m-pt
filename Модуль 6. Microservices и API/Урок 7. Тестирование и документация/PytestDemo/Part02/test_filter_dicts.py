import pytest
from filter_dicts import filter_dicts  # Замените your_module на имя вашего модуля

@pytest.fixture
def sample_data():
    """Создает список словарей для тестирования."""
    return [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "London"},
        {"name": "Charlie", "age": 30, "city": "Paris"},
        {"name": "David", "age": 25, "city": "New York"},
    ]

def test_filter_by_age(sample_data):
    """Проверяет фильтрацию по возрасту."""
    result = filter_dicts(sample_data, "age", 30)
    assert len(result) == 2
    assert all(item["age"] == 30 for item in result)

def test_filter_by_city(sample_data):
    """Проверяет фильтрацию по городу."""
    result = filter_dicts(sample_data, "city", "New York")
    assert len(result) == 2
    assert all(item["city"] == "New York" for item in result)

def test_filter_by_name(sample_data):
    """Проверяет фильтрацию по имени."""
    result = filter_dicts(sample_data, "name", "Bob")
    assert len(result) == 1
    assert result[0]["name"] == "Bob"

def test_filter_empty_result(sample_data):
    """Проверяет случай, когда результат фильтрации пустой."""
    result = filter_dicts(sample_data, "city", "Tokyo")
    assert len(result) == 0

def test_filter_invalid_key(sample_data):
    """Проверяет случай, когда ключ не существует."""
    result = filter_dicts(sample_data, "country", "USA")
    assert len(result) == 0