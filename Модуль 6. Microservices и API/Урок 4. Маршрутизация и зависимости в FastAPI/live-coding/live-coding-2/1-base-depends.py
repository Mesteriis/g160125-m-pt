from fastapi import FastAPI, Depends


app = FastAPI()


def get_username():
    return "Alice"




@app.get("/profile")
def read_profile(username: str = Depends(get_username)):
    return {"message": f"Hello, {username}!"}
