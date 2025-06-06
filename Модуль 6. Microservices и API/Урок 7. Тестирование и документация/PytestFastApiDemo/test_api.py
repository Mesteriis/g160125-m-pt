import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope='session')
def client():
    client = TestClient(app)
    try:
        yield client
    finally:
        # Здесь можно добавить код для очистки ресурсов, если это необходимо
        pass


def test_read_items(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [{"name": "Item 1"}, {"name": "Item 2"}]


def test_read_item(client):
    response = client.get("/items/0")
    assert response.status_code == 200
    assert response.json() == {"name": "Item 1"}


def test_create_item(client):
    response = client.post("/items", json={"name": "Item 3"})
    assert response.status_code == 200
    assert response.json() == {"name": "Item 3"}


def test_update_item(client):
    response = client.put("/items/0", json={"name": "Updated Item 1"})
    assert response.status_code == 200
    assert response.json() == {"name": "Updated Item 1"}


@pytest.mark.skip(reason="Функция еще не реализована")
def test_delete_item(client):
    # TODO: напишите тест для проверки delete_item()
    #  Уберите декоратор @pytest.mark.skip
    assert False


# Негативные тесты
def test_read_item_not_found(client):
    response = client.get("/items/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_update_item_not_found(client):
    response = client.put("/items/99", json={"name": "Updated Item 99"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_delete_item_not_found(client):
    response = client.delete("/items/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


