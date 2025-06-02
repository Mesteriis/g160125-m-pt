from fastapi import FastAPI
from routers.users import router as users_router
from routers.items import router as items_router


app = FastAPI()

# Подключаем маршруты из отдельных файлов
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(items_router, prefix="/items", tags=["items"])


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
