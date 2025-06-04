# **Техническое задание: Live-Coding 2**

## **Задача:**
Реализовать новые эндпоинты для работы с книгами, авторами и тегами.

---

## **1. Реализация новых эндпоинтов в `routers/books.py`**

📌 **Что нужно сделать:**
- Дописать **5 новых эндпоинтов** для работы с книгами, авторами и тегами.

### **1.1 Эндпоинт для обновления книги по ID**
```python
@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated_book: BookCreate, db: Session = Depends(get_db)):
    """Обновляет книгу по ID."""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = updated_book.title
    book.author_id = updated_book.author_id
    db.commit()
    db.refresh(book)
    return book
```

### **1.2 Эндпоинт для удаления книги по ID**
```python
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Удаляет книгу по ID."""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
```

### **1.3 Эндпоинт для обновления тега**
```python
@router.put("/tags/{tag_id}", response_model=TagSchema)
def update_tag(tag_id: int, updated_tag: TagSchema, db: Session = Depends(get_db)):
    """Обновляет тег по ID."""
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    tag.name = updated_tag.name
    db.commit()
    db.refresh(tag)
    return tag
```

### **1.4 Эндпоинт для удаления тега**
```python
@router.delete("/tags/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    """Удаляет тег по ID."""
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()
    return {"message": "Tag deleted successfully"}
```

### **1.5 Эндпоинт для получения авторов с их книгами**
```python
@router.get("/authors_with_books/", response_model=list[AuthorSchema])
def get_authors_with_books(db: Session = Depends(get_db)):
    """Возвращает всех авторов и их книги."""
    return db.query(Author).options(selectinload(Author.books)).all()
```

---

## **2. Проверка эндпоинтов в Swagger**
📌 **Запустить сервер:**
```sh
uvicorn main:app --reload
```
📌 **Перейти в Swagger UI:**
👉 `http://127.0.0.1:8000/docs`  
📌 **Проверить работу новых эндпоинтов**

---