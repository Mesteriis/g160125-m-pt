from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int


user_data = {
    "id": 1,
    "name": "Иван",
    "age": 30
}

# Десериализация из словаря
user = User(**user_data)

print(user)
print(user.name)
