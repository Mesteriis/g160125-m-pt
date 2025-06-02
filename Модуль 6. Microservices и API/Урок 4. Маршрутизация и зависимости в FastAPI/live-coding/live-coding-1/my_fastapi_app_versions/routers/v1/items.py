from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def list_items_v1():
    """
    Получение списка товаров (v1).
    """
    return [{"item_id": 101, "title": "Item A v1"}, {"item_id": 102, "title": "Item B v1"}]


@router.post("/")
def create_item_v1(title: str):
    """
    Создание нового товара (v1).
    """
    return {"item_id": 999, "title": title, "version": "v1"}
