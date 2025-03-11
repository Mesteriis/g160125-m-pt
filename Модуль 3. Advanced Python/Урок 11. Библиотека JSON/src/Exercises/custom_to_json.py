# Создайте класс Student, который имеет поля имени, возраста и курса.
# Напишите код сохранения и загрузки объектов данного класса в/из объектов JSON

import json

from pydantic import BaseModel, Field

data = [
    {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    },
    {
        'name': 'Anna',
        'age': 25,
        'city': 'London'
    },
    {
        'name': 'Mike',
        'age': None,
        'city': 'Chicago'
    }
]


class StudentPydantic(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    course: str | None = None
    city: str | None = None


def main():
    students = []
    for el in data:
        student_pydantic = StudentPydantic.model_validate(el)
        print(student_pydantic.model_dump_json())
        print(student_pydantic.model_dump())
        students.append(student_pydantic)
    print(students)


if __name__ == '__main__':
    main()
