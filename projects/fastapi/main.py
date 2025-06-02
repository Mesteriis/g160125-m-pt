from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = []
class Author(BaseModel):
   name: str
   bio: str = None

class Book(BaseModel):
   title: str
   author: Author
   year: int
   genre: str

@app.get("/")
def book_list() -> list[Book]:
    return books


@app.post("/")
def add_book(book: Book) -> Book:
    books.append(book)
    return book

@app.get("/{book_id}")
def get_book(book_id: int) -> Book:
    if 0 <= book_id < len(books):
        return books[book_id]
    raise HTTPException(status_code=404, detail="Book not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
