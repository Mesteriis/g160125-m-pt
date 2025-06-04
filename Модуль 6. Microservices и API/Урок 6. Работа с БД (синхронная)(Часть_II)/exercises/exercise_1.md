# **Техническое задание 1**

## **Задача:**
Реализовать модели данных, загрузить `books.json` в базу данных, создать Pydantic-схемы и проверить API через Swagger и SQL-запросы.

---

## **1. Дописать модели данных**
### **1.1 Обновить `models.py`**
**Что нужно сделать:**
- Добавить модели **`Author`** и **`Tag`**
- Обновить модель **`Book`**
- Создать таблицу-посредник для связи `Book` и `Tag`

```python
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Ассоциативная таблица для связи многие ко многим (книги - теги)
book_tag_association = Table(
    "book_tag_association",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id")),
    Column("tag_id", Integer, ForeignKey("tags.id"))
)

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="author")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", secondary=book_tag_association, back_populates="tags")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    tags = relationship("Tag", secondary=book_tag_association, back_populates="books")
```

**После внесения изменений выполните:**
```sh
alembic revision --autogenerate -m "Add authors, books, and tags tables"
alembic upgrade head
```

---

## **2. Загрузить `books.json` в базу данных**
### **2.1 Разместить JSON-файл**
Сохраните `books.json` в папке `data/` проекта:
```
/fastapi_books/data/books.json
```

### **2.2 Создать миграцию для загрузки данных**
```sh
alembic revision --autogenerate -m "Load books data"
```

### **2.3 Добавить код в файл миграции**
```python
import json
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from models import Author, Book, Tag, book_tag_association

def upgrade():
    """Загружает данные из JSON в БД."""
    bind = op.get_bind()
    session = Session(bind=bind)

    # Очистка таблиц перед загрузкой новых данных
    session.execute(sa.text("DELETE FROM book_tag_association"))
    session.execute(sa.text("DELETE FROM books"))
    session.execute(sa.text("DELETE FROM authors"))
    session.execute(sa.text("DELETE FROM tags"))
    session.commit()

    with open("data/books.json", "r") as f:
        data = json.load(f)

    # Загружаем авторов
    for author in data["authors"]:
        session.execute(sa.insert(Author).values(id=author["id"], name=author["name"]))

    # Загружаем теги
    for tag in data["tags"]:
        session.execute(sa.insert(Tag).values(id=tag["id"], name=tag["name"]))

    # Загружаем книги
    for book in data["books"]:
        session.execute(sa.insert(Book).values(id=book["id"], title=book["title"], author_id=book["author_id"]))

    # Загружаем связи книг и тегов
    for book in data["books"]:
        for tag_id in book["tag_ids"]:
            session.execute(sa.insert(book_tag_association).values(book_id=book["id"], tag_id=tag_id))

    session.commit()

def downgrade():
    """Удаляет загруженные данные."""
    bind = op.get_bind()
    session = Session(bind=bind)
    session.execute(sa.text("DELETE FROM book_tag_association"))
    session.execute(sa.text("DELETE FROM books"))
    session.execute(sa.text("DELETE FROM authors"))
    session.execute(sa.text("DELETE FROM tags"))
    session.commit()
```

**После внесения изменений выполните:**
```sh
alembic upgrade head
```

---

## **3. Дописать `schemas.py`**
### **Что нужно сделать?**
- Определить **Pydantic-схемы** для валидации данных

```python
from pydantic import BaseModel
from typing import List, Optional

class TagSchema(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class AuthorSchema(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class BookCreate(BaseModel):
    title: str
    author_id: int
    tag_ids: List[int]
    class Config:
        orm_mode = True

class BookResponse(BookCreate):
    id: int
    class Config:
        orm_mode = True
```

---

## **4. Проверить в Swagger эндпоинты**

📌 Запустите FastAPI-сервер:
```sh
uvicorn main:app --reload
```

📌 Перейдите в Swagger UI:  
👉 `http://127.0.0.1:8000/docs`  
🔹 Проверьте эндпоинты для **создания, получения, удаления книг**.  

---

## **5. Написать 5 SQLAlchemy-запросов в Python-консоли**
📌 **Открываем интерактивную сессию:**
```sh
python
```
📌 **Выполняем запросы:**
```python
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Author, Book, Tag, book_tag_association

db = SessionLocal()

# 1. Список всех авторов
authors = db.query(Author).all()
print([{ "id": a.id, "name": a.name } for a in authors])

# 2. Получение книг конкретного автора
books = db.query(Book).filter(Book.author_id == 1).all()
print([{ "id": b.id, "title": b.title } for b in books])

# 3. Список всех тегов
tags = db.query(Tag).all()
print([{ "id": t.id, "name": t.name } for t in tags])

# 4. Получение книг по тегу
books_by_tag = db.query(Book).join(book_tag_association).filter(book_tag_association.c.tag_id == 3).all()
print([{ "id": b.id, "title": b.title } for b in books_by_tag])

# 5. Поиск книги по названию
books_search = db.query(Book).filter(Book.title.ilike("%War%")).all()
print([{ "id": b.id, "title": b.title } for b in books_search])
```