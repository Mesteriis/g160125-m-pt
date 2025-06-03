# **Live-coding-2: Запросы SQLAlchemy vs Чистый SQL и Запуск API**

## **📌 Секция 5: Запросы SQLAlchemy vs Чистый SQL**
### **5.1. Добавление записей (CREATE)**

#### **SQLAlchemy ORM:**
📄 **Добавляем несколько записей в базу данных**
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

#### **Эквивалентный SQL-запрос:**
```sql
INSERT INTO books (title, author) VALUES ('FastAPI Guide', 'Alice Smith');
INSERT INTO books (title, author) VALUES ('SQLAlchemy Deep Dive', 'Bob Johnson');
INSERT INTO books (title, author) VALUES ('Advanced Python', 'Charlie Brown');
```
✅ **Теперь несколько записей успешно добавлены в базу!**

---

### **Объяснение методов SQLAlchemy**

- **`add(instance)`** – добавляет один объект в текущую сессию SQLAlchemy, но не записывает его в базу данных до вызова `commit()`.
- **`add_all([instances])`** – добавляет сразу несколько объектов в сессию.
- **`commit()`** – фиксирует изменения в базе данных. Без этого метода изменения не сохранятся.
- **`refresh(instance)`** – обновляет объект из базы данных после `commit()`, чтобы получить его ID или другие сгенерированные данные.
- **`query(Model)`** – создаёт запрос к таблице модели `Model`.
- **`all()`** – выполняет запрос и возвращает все результаты в виде списка.
- **`filter(condition)`** – добавляет условие к SQL-запросу (аналог `WHERE`).
- **`first()`** – возвращает первую найденную запись (аналог `LIMIT 1`).
- **`update({field: value})`** – обновляет одну или несколько записей в таблице.
- **`delete(instance)`** – удаляет конкретный объект из базы данных.

✅ **Теперь стало понятно, для чего нужны ключевые методы SQLAlchemy!**

---

## **📌 Секция 6: Реализация CRUD-операций через API**

### **6.1. Создание эндпоинтов в `routers/books.py`**
📄 **Добавляем эндпоинты для получения одной книги, обновления и удаления**
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import BookDB
from schemas import BookCreate, BookResponse

router = APIRouter()

# Эндпоинт для добавления новой книги
@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = BookDB(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Эндпоинт для получения всех книг
@router.get("/")
def get_books(db: Session = Depends(get_db)):
    return db.query(BookDB).all()

# Эндпоинт для получения одной книги по ID
@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Эндпоинт для обновления книги по ID
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

# Эндпоинт для удаления книги по ID
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
```

✅ **Теперь у нас есть полный CRUD для работы с книгами!**

---

### **6.2. Запуск и тестирование API**
📄 **Запускаем сервер FastAPI**
```sh
uvicorn main:app --reload
```

### **6.3. Проверка API в браузере**
- Открываем `http://127.0.0.1:8000/docs`
- Проверяем эндпоинты `/books` (GET, POST, PUT, DELETE)

✅ **Теперь API полностью рабочий!**


