# **Техническое задание: Live-coding-2 (Запросы SQLAlchemy vs Чистый SQL и Запуск API)**

## **🎯 Цель задания**
Реализовать CRUD-операции для работы с базой данных в FastAPI с использованием SQLAlchemy и сравнить их с аналогичными SQL-запросами. API должен поддерживать:
- Создание записей в базе данных.
- Чтение всех книг и одной книги по ID.
- Обновление книги по ID.
- Удаление книги по ID.

---

## **📌 Шаг 1: Запросы SQLAlchemy vs Чистый SQL**
### **1.1. Добавление записей (CREATE)**
📄 **Добавляем несколько записей через SQLAlchemy**
```python
from database import SessionLocal
from models import BookDB

db = SessionLocal()

# Создаём несколько объектов книг
book1 = BookDB(title="FastAPI Guide", author="Alice Smith")
book2 = BookDB(title="SQLAlchemy Deep Dive", author="Bob Johnson")
book3 = BookDB(title="Advanced Python", author="Charlie Brown")

# Добавляем книги в сессию
# add() - добавляет один объект, add_all() - сразу несколько объектов
db.add_all([book1, book2, book3])

# Фиксируем изменения в базе данных
db.commit()

# Обновляем объекты, чтобы получить их ID из БД
db.refresh(book1)
db.refresh(book2)
db.refresh(book3)

print(f"Добавлены книги с ID: {book1.id}, {book2.id}, {book3.id}")
```

📄 **Аналогичный SQL-запрос:**
```sql
INSERT INTO books (title, author) VALUES ('FastAPI Guide', 'Alice Smith');
INSERT INTO books (title, author) VALUES ('SQLAlchemy Deep Dive', 'Bob Johnson');
INSERT INTO books (title, author) VALUES ('Advanced Python', 'Charlie Brown');
```
✅ **Результат:** В базу данных добавлены три книги.

---

### **1.2. Получение записей (READ)**
📄 **Получаем все книги через SQLAlchemy**
```python
books = db.query(BookDB).all()
for book in books:
    print(f"Книга: {book.title}, Автор: {book.author}")
```
📄 **Аналогичный SQL-запрос:**
```sql
SELECT * FROM books;
```
✅ **Результат:** Выведены все книги из базы данных.

---

### **1.3. Обновление записей (UPDATE)**
📄 **Обновляем данные книги через SQLAlchemy**
```python
book_to_update = db.query(BookDB).filter(BookDB.id == 1).first()
if book_to_update:
    book_to_update.author = "Updated Author"
    db.commit()
    print("Автор книги обновлён!")
```
📄 **Аналогичный SQL-запрос:**
```sql
UPDATE books SET author = 'Updated Author' WHERE id = 1;
```
✅ **Результат:** Данные книги обновлены в базе данных.

---

### **1.4. Удаление записей (DELETE)**
📄 **Удаляем книгу через SQLAlchemy**
```python
book_to_delete = db.query(BookDB).filter(BookDB.id == 1).first()
if book_to_delete:
    db.delete(book_to_delete)
    db.commit()
    print("Книга удалена!")
```
📄 **Аналогичный SQL-запрос:**
```sql
DELETE FROM books WHERE id = 1;
```
✅ **Результат:** Книга удалена из базы данных.

---

## **📌 Шаг 2: Реализация CRUD-операций в API**
### **2.1. Создание маршрутов API (`routers/books.py`)**
📄 **Добавьте эндпоинты CRUD-операций**
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import BookDB
from schemas import BookCreate, BookResponse

router = APIRouter()

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = BookDB(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/")
def get_books(db: Session = Depends(get_db)):
    return db.query(BookDB).all()

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated_book: BookCreate, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = updated_book.title
    book.author = updated_book.author
    db.commit()
    db.refresh(book)
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
```
✅ **Результат:** Теперь API поддерживает полный CRUD.

---

## **📌 Шаг 3: Запуск и тестирование API**
1. Запустите сервер FastAPI:
    ```sh
    uvicorn main:app --reload
    ```
2. Перейдите в браузере по адресу `http://127.0.0.1:8000/docs`.
3. Протестируйте маршруты (`POST /books`, `GET /books`, `PUT /books/{id}`, `DELETE /books/{id}`).

✅ **Результат:** API полностью функционирует!

---

🎯 **Финальный результат:** API на FastAPI, реализующий CRUD-операции с SQLAlchemy и поддерживающий сравнение с SQL-запросами. 🚀

