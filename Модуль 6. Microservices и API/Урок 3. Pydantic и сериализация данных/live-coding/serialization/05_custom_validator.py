from pydantic import BaseModel, field_validator


class User(BaseModel):
    id: int
    name: str
    email: str

    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Email должен содержать символ '@'")
        return value


user = User(id=1, name="Иван", email="ivan@example.com")
print(user.model_dump_json())
try:
    User(id=2, name="Петр", email="petrexample.com")
except ValueError as e:
    print(e)
