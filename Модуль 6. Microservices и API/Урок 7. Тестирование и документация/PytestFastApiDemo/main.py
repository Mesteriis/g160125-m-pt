from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()


class Item(BaseModel):
    name: str


items = [{"name": "Item 1"}, {"name": "Item 2"}]


@app.get("/items")
def read_items():
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int):
    # TODO: исправьте реализацию методы, чтобы проходили все тесты
    return items[item_id]


@app.post("/items")
def create_item(item: Item):
    items.append(item.model_dump())
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # TODO: исправьте реализацию методы, чтобы проходили все тесты
    items[item_id] = item.model_dump()
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: напишите реализацию метода
    return Response(status_code=204, deteil='')  # Удаление элемента не возвращает содержимого
    raise NotImplemented("Method not implemented")
    ApiEcxception(status_code=404, detail="Item not found")  # Если элемент не найден, возвращаем 404