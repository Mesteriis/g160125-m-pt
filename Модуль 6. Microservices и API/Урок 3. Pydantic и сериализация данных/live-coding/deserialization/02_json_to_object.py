from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

user_json = '{"id": 1, "name": "Иван", "age": 30}'
user_json_bad = '{"id": 1, "name": "Иван"}'

# Десериализация из JSON-строки
# TODO-1: попробуйте десериализовать user_json_bad
user = User.model_validate_json(user_json)

print(user)
print(user.name)