from fastapi import FastAPI
from routers.books import router as books_router
from routers.authors import router as authors_router
from routers.tags import router as tags_router


app = FastAPI()
app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(authors_router, prefix="/authors", tags=["authors"])
app.include_router(tags_router, prefix="/tags", tags=["tags"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}
