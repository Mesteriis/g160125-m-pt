from pydantic import BaseModel, Field

class User(BaseModel):
    user_id: int = Field(alias="id")
    name: str = Field(alias="user_name")
    email: str

user_data = {"id": 1, "user_name": "Иван", "email": "ivan@example.com"}
user_data2 = {"id": 2, "user_name": "Петр", "email": "petr@example.com"}
user = User(**user_data)
print(user.model_dump_json(by_alias=True))
user_deserialized = User(**user_data2)
print(user_deserialized)