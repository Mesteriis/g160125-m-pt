from fastapi import FastAPI, Depends


app = FastAPI()


def get_db():
    db = {"connection": "fake_db_connection"}
    try:
        yield db  # Возвращаем подключение к БД
    finally:
        print("Closing database connection")


@app.get("/items")
def read_items(db=Depends(get_db)):
    return {"db_status": db["connection"], "items": ["Item1", "Item2"]}
