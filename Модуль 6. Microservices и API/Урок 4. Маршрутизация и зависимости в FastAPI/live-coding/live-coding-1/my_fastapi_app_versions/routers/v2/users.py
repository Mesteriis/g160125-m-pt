from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def get_all_users_v2():
    """
    Получение всех пользователей (v2).
    Теперь добавлено поле 'extra'.
    """
    return [{"user_id": 1, "name": "Alice v2", "extra": "info"}, {"user_id": 2, "name": "Bob v2", "extra": "details"}]


@router.get("/{user_id}")
def get_user_v2(user_id: int):
    """
    Получение одного пользователя по ID (v2).
    """
    return {"user_id": user_id, "name": f"User {user_id} v2", "extra": "more info"}
