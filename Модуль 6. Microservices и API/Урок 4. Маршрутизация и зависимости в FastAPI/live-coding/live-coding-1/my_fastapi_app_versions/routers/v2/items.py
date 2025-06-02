from fastapi import APIRouter
from typing import Optional


router = APIRouter()


@router.get("/")
def list_items_v2(search: Optional[str] = None):
    """
    Получение списка товаров (v2) с возможностью поиска.
    Теперь у товаров есть поле 'category'.
    """
    items = [
        {"item_id": 201, "title": "Item A v2", "category": "Tech"},
        {"item_id": 202, "title": "Item B v2", "category": "Home"},
        {"item_id": 203, "title": "Item C v2", "category": "Office"},
    ]
    if search:
        items = [i for i in items if search.lower() in i["title"].lower()]
    return {"items": items, "api_version": "v2"}


@router.post("/")
def create_item_v2(title: str, description: Optional[str] = None):
    """
    Создание нового товара (v2) с возможностью добавления описания.
    """
    return {"item_id": 2000, "title": title, "description": description, "version": "v2"}
