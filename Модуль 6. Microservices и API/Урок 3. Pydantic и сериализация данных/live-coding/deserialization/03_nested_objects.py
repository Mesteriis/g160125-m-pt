from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Company(BaseModel):
    name: str
    address: Address
    employees: Optional[List[str]] = None

class Employee(BaseModel):
    id: int
    name: str
    company: Company

employee_data = {
    "id": 1,
    "name": "Алексей",
    "company": {
        "name": "ООО Рога и Копыта",
        "address": {
            "street": "Тверская",
            "city": "Москва",
            "zip_code": "123456"
        },
        "employees": ["Иван", "Петр"]
    }
}

# Десериализация из словаря с вложенными объектами
employee = Employee(**employee_data)

print(employee)
print(employee.company.address.city)