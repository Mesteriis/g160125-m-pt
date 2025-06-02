from fastapi import FastAPI
from routers.v1.users import router as users_v1_router
from routers.v1.items import router as items_v1_router
from routers.v2.users import router as users_v2_router
from routers.v2.items import router as items_v2_router


app = FastAPI()


# Подключаем роутеры с разными версиями API
app.include_router(users_v1_router, prefix="/api/v1/users", tags=["v1-users"])
app.include_router(items_v1_router, prefix="/api/v1/items", tags=["v1-items"])
app.include_router(users_v2_router, prefix="/api/v2/users", tags=["v2-users"])
app.include_router(items_v2_router, prefix="/api/v2/items", tags=["v2-items"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
