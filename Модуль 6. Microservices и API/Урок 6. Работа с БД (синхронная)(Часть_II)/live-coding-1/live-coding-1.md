# Live-Coding 1: Работа с SQLAlchemy и Alembic в FastAPI

## 1. Добавление таблиц `Author` и `Tag`

### 1.1 Разбор ключевых понятий

- **`book_tag_association`** – таблица-посредник для связи книг и тегов (M:N).
- **`Base.metadata`** – содержит все модели SQLAlchemy и управляет схемой БД.
- **`ForeignKey()`** – внешний ключ для связи таблиц.
- **`back_populates`** – двусторонняя связь между таблицами.
- **`secondary`** – указывает промежуточную таблицу для связи M:N.
- **`relationship()`** – устанавливает связи между таблицами.

### 1.2 Определение моделей

Создайте или обновите `models.py`:

```python
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Ассоциативная таблица для связи книги и тегов
book_tag_association = Table(
    "book_tag_association",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id")),
    Column("tag_id", Integer, ForeignKey("tags.id"))
)

class Author(Base):
    """Модель автора."""
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="author")

class Tag(Base):
    """Модель тега."""
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", secondary=book_tag_association, back_populates="tags")

class Book(Base):
    """Модель книги."""
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    tags = relationship("Tag", secondary=book_tag_association, back_populates="books")
```

### 1.3 Генерация и применение миграций Alembic

Выполните команды:

```sh
alembic revision --autogenerate -m "add authors and tags"
alembic upgrade head
```

---

## 2. ТЕОРИЯ: Миграции в Alembic: структура и принципы работы

Миграции в Alembic позволяют изменять структуру базы данных без её полного удаления и пересоздания. Они используются для добавления новых таблиц, изменения схемы данных и других операций. Автоматические миграции генерируются при помощи `--autogenerate`, но иногда требуется вручную писать код миграции. Самописные миграции могут понадобиться, если:
- Автогенерация не поддерживает сложные изменения структуры БД.
- Требуется загрузка данных из внешних источников.
- Нужно выполнить специфические SQL-команды, которые нельзя выразить через SQLAlchemy ORM.

### 2.1 Где находятся файлы миграции?

Все файлы миграции находятся в `alembic/versions/`. Каждая миграция имеет уникальный идентификатор.

### 2.2 Структура файла миграции

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    """Добавляет таблицы авторов и тегов."""
    op.create_table("authors",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False))

    op.create_table("tags",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False))

    op.create_table("book_tag_association",
        sa.Column("book_id", sa.Integer(), sa.ForeignKey("books.id"), primary_key=True),
        sa.Column("tag_id", sa.Integer(), sa.ForeignKey("tags.id"), primary_key=True))

def downgrade():
    """Удаляет таблицы."""
    op.drop_table("book_tag_association")
    op.drop_table("tags")
    op.drop_table("authors")
```

---

## 3. Загрузка JSON-файла в базу данных

### 3.1 Подготовка JSON-файла

Разместите `books.json` в папке `data/`.

### 3.2 Создание миграции для загрузки данных

```sh
alembic revision --autogenerate -m "Load books data"
```

### 3.3 Код для вставки в миграцию

```python
from typing import Sequence, Union
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

### Разбор кода

1. **Очистка таблиц перед загрузкой данных**
   - Используется `DELETE FROM` для удаления всех данных из связанных таблиц перед вставкой новых записей.
   - Это предотвращает дублирование и ошибки нарушения уникальности.

2. **Чтение JSON-файла**
   - Файл `books.json` открывается и загружается в Python с помощью `json.load()`.

3. **Загрузка авторов**
   - Цикл проходит по `data["authors"]` и вставляет каждую запись в таблицу `authors`.

4. **Загрузка тегов**
   - Аналогично, теги добавляются в таблицу `tags`.

5. **Загрузка книг**
   - Каждая книга записывается в таблицу `books`, используя `id`, `title`, и `author_id`.

6. **Загрузка связей книг и тегов**
   - Так как книги могут иметь несколько тегов, создаются записи в `book_tag_association`.

7. **Откат изменений (downgrade)**
   - В случае отката миграции (`alembic downgrade`), все загруженные данные удаляются из базы.

Выполните команду для применения миграции:

```sh
alembic upgrade head
```

---

## 4. Разбор `schemas.py`

Файл `schemas.py` определяет Pydantic-модели, используемые для валидации входных и выходных данных. Каждая схема соответствует модели SQLAlchemy и используется в API:

- `TagSchema` – схема для тегов.
- `AuthorSchema` – схема для авторов.
- `BookSchema` – включает `AuthorSchema` и `TagSchema` для отображения связей.

### Код `schemas.py`

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
    author: Optional[AuthorSchema]
    tags: List[TagSchema] = []
    class Config:
        orm_mode = True

class BookResponse(BookCreate):
    id: int
    class Config:
        orm_mode = True
```

### Разбор `schemas.py`

1. **`BaseModel`** – основа всех Pydantic-моделей, обеспечивает автоматическую валидацию данных.
2. **`orm_mode = True`** – позволяет преобразовывать ORM-объекты SQLAlchemy в Pydantic-модели.
3. **Классы данных:**
   - `TagSchema` и `AuthorSchema` представляют теги и авторов, включают `id` и `name`.
   - `BookCreate` используется для создания книги. Включает `title`, `author` и список тегов.
   - `BookResponse` расширяет `BookCreate`, добавляя `id`, чтобы вернуть полные данные книги.

Эта структура позволяет корректно передавать данные между клиентом и сервером, сохраняя типизацию и связи между объектами. 🚀

---

## 5. Разбор SQLAlchemy-запросов

Каждый SQL-запрос в консоли разбирается подробно:

```python
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Author, Book, Tag, book_tag_association

db = SessionLocal()

# 1. Список всех авторов
authors = db.query(Author).all()
print([{ "id": a.id, "name": a.name } for a in authors])

# 2. Получение книг конкретного автора
author_id = 1  # Укажи нужного автора
books = db.query(Book).filter(Book.author_id == author_id).all()
print([{ "id": b.id, "title": b.title } for b in books])

# 3. Список всех тегов
tags = db.query(Tag).all()
print([{ "id": t.id, "name": t.name } for t in tags])

# 4. Получение книг по тегу
tag_id = 3  # Укажи нужный тег
books_by_tag = db.query(Book).join(book_tag_association).filter(book_tag_association.c.tag_id == tag_id).all()
print([{ "id": b.id, "title": b.title } for b in books_by_tag])

# 5. Поиск книги по названию (нечёткий поиск)
keyword = "War"  # Укажи ключевое слово
books_search = db.query(Book).filter(Book.title.ilike(f"%{keyword}%")).all()
print([{ "id": b.id, "title": b.title } for b in books_search])
```

---

## Методы запросов в SQLAlchemy

1. **`query()`** – выполняет запрос к таблице.
   ```python
   db.query(Book).all()  # Получить все книги
   ```
2. **`filter()`** – фильтрует результаты.
   ```python
   db.query(Book).filter(Book.author_id == 1).all()  # Книги автора с id=1
   ```
3. **`join()`** – соединяет таблицы.
   ```python
   db.query(Book).join(book_tag_association).filter(book_tag_association.c.tag_id == 3).all()
   ```
4. **`order_by()`** – сортировка данных.
   ```python
   db.query(Book).order_by(Book.title).all()  # Сортировать книги по названию
   ```
5. **`limit()`** и **`offset()`** – пагинация.
   ```python
   db.query(Book).limit(10).offset(20).all()  # Вернуть 10 книг, пропустив 20
   ```
6. **`count()`** – количество записей.
   ```python
   db.query(Book).count()  # Получить количество книг
   ```
7. **`first()`** и **`one()`** – получение одной записи.
   ```python
   db.query(Book).first()  # Первая запись
   db.query(Book).filter(Book.id == 1).one()  # Одна запись с id=1
   ```
8. **`delete()`** – удаление записей.
   ```python
   db.query(Book).filter(Book.id == 1).delete()
   db.commit()
   ```
9. **`update()`** – обновление записей.
   ```python
   db.query(Book).filter(Book.id == 1).update({"title": "New Title"})
   db.commit()
   ```
10. **`group_by()`** – группировка данных.
   ```python
   db.query(Book.author_id, sa.func.count(Book.id)).group_by(Book.author_id).all()
   ```

