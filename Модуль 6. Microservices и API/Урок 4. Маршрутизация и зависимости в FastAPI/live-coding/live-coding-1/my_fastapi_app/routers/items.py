from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def list_items():
    """
    Получение списка товаров
    """
    return [{"item_id": 101, "title": "Item A"}, {"item_id": 102, "title": "Item B"}]


@router.post("/")
def create_item(title: str):
    """
    Создание нового товара
    """
    return {"item_id": 999, "title": title}
