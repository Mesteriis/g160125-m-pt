from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    name: str
    age: int


users_data = [
    {"id": 1, "name": "Иван", "age": 30},
    {"id": 2, "name": "Петр", "age": 25}
]

# Десериализация списка словарей
users = [User(**user_data) for user_data in users_data]

for user in users:
    print(user)
