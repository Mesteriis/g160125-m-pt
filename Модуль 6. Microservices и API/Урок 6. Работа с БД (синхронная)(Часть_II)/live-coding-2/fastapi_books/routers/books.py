from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Book
from schemas import BookCreate, BookResponse


router = APIRouter()

# Эндпоинт для добавления новой книги
@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# Эндпоинт для получения всех книг
@router.get("/")
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


# Эндпоинт для получения одной книги по ID
@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# Эндпоинт для обновления книги по ID
@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated_book: BookCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = updated_book.title
    book.author = updated_book.author
    db.commit()
    db.refresh(book)
    return book


# Эндпоинт для удаления книги по ID
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}


@router.get("/search", response_model=list[BookResponse])
def search_books(keyword: str, db: Session = Depends(get_db)):
    """Поиск книг по названию с использованием нечёткого поиска."""
    return db.query(Book).filter(Book.title.ilike(f"%{keyword}%")).all()
