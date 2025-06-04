from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Book, Author
from schemas import BookResponse, AuthorSchema


router = APIRouter()


@router.get("/", response_model=list[AuthorSchema])
def get_authors(db: Session = Depends(get_db)):
    """Возвращает список всех авторов."""
    return db.query(Author).all()


@router.get("/{author_id}/books", response_model=list[BookResponse])
def get_books_by_author(author_id: int, db: Session = Depends(get_db)):
    """Возвращает список книг определенного автора."""
    return db.query(Book).filter(Book.author_id == author_id).all()

