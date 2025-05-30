from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str | None = None


# TODO-1: поменяйте значение name:  "Alice" -> 100. Запустите код.
# TODO-2: поменяйте значение id:  123 -> "123". Запустите код.
user_data = {"id": 123, "name": "Alice", "email": "alice@example.com"}
user = User(**user_data)

user_json = user.model_dump_json(indent=4)
print(user_json)
