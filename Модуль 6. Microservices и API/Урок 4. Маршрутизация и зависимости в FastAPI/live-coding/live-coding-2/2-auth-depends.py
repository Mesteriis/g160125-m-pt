from fastapi import FastAPI, Depends, HTTPException, status


app = FastAPI()


def get_current_user(token: str = "fake_token"):
    if token != "secure_token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return {"username": "Alice"}


@app.get("/dashboard")
def read_dashboard(user: dict = Depends(get_current_user)):
    return {"message": f"Welcome, {user['username']}!"}
