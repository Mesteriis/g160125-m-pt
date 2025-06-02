from fastapi import FastAPI, Depends


app = FastAPI()


def get_user_id() -> int:
    return 123


def get_db_connection():
    db = {"connection": "fake_db_connection_object"}
    try:
        yield db
    finally:
        print("Closing db connection")


@app.get("/multi-dep")
def multi_dep_example(
    user_id: int = Depends(get_user_id),
    db = Depends(get_db_connection)
):
    return {
        "user_id": user_id,
        "db_connection": db["connection"]
    }
