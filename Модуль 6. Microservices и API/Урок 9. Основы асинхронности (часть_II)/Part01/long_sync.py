import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# Модели Pydantic
class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    author_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


# Хранилище данных
authors = [Author(id=1, name="Alex"), Author(id=2, name="Bob")]
books = []
author_id_counter = 3
book_id_counter = 1

# FastAPI приложение
app = FastAPI()


# CRUD для авторов
@app.post("/authors/", response_model=Author)
def create_author(author: AuthorCreate):
    global author_id_counter
    new_author = Author(id=author_id_counter, **author.model_dump())
    time.sleep(60)
    authors.append(new_author)
    author_id_counter += 1
    return new_author


@app.get("/authors/{author_id}", response_model=Author)
def read_author(author_id: int):
    for author in authors:
        if author.id == author_id:
            return author
    raise HTTPException(status_code=404, detail="Author not found")


@app.put("/authors/{author_id}", response_model=Author)
def update_author(author_id: int, author: AuthorCreate):
    for i, existing_author in enumerate(authors):
        if existing_author.id == author_id:
            updated_author = Author(id=author_id, **author.model_dump())
            authors[i] = updated_author
            return updated_author
    raise HTTPException(status_code=404, detail="Author not found")


@app.delete("/authors/{author_id}", response_model=Author)
def delete_author(author_id: int):
    for i, author in enumerate(authors):
        if author.id == author_id:
            deleted_author = authors.pop(i)
            return deleted_author
    raise HTTPException(status_code=404, detail="Author not found")


@app.get("/authors/", response_model=list[Author])
def list_authors():
    return authors


# CRUD для книг
@app.post("/books/", response_model=Book)
def create_book(book: BookCreate):
    global book_id_counter
    new_book = Book(id=book_id_counter, **book.model_dump())
    books.append(new_book)
    book_id_counter += 1
    return new_book


@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    for i, existing_book in enumerate(books):
        if existing_book.id == book_id:
            updated_book = Book(id=book_id, **book.model_dump())
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(i)
            return deleted_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/", response_model=list[Book])
def list_books():
    return books


# uvicorn long_sync:app --reload