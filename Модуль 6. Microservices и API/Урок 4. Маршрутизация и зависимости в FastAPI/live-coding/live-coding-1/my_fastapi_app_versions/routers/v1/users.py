from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def get_all_users():
    """
    Получение всех пользователей (v1).
    """
    return [{"user_id": 1, "name": "Alice v1"}, {"user_id": 2, "name": "Bob v1"}]


@router.get("/{user_id}")
def get_user(user_id: int):
    """
    Получение одного пользователя по ID (v1).
    """
    return {"user_id": user_id, "name": f"User {user_id} v1"}
