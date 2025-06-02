from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def list_users():
    """
    Получение списка всех пользователей
    """
    return [{"user_id": 1, "name": "Alice"}, {"user_id": 2, "name": "Bob"}]


@router.get("/{user_id}")
def get_user(user_id: int):
    """
    Получение информации о конкретном пользователе по user_id
    """
    return {"user_id": user_id, "name": f"User {user_id}"}
