from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Book, Tag, book_tag_association
from schemas import BookResponse, TagSchema


router = APIRouter()

@router.get("/", response_model=list[TagSchema])
def get_tags(db: Session = Depends(get_db)):
    """Возвращает список всех тегов."""
    return db.query(Tag).all()


@router.get("/{tag_id}/books", response_model=list[BookResponse])
def get_books_by_tag(tag_id: int, db: Session = Depends(get_db)):
    """Возвращает список книг, относящихся к определенному тегу."""
    return db.query(Book).join(book_tag_association).filter(book_tag_association.c.tag_id == tag_id).all()
