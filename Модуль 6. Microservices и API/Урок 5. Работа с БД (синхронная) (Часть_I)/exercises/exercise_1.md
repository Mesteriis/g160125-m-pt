# **Техническое задание: Live-coding-1 (Внедрение SQLAlchemy в FastAPI)**

## **🎯 Цель задания**
Реализовать базовый API на FastAPI с использованием SQLAlchemy и PostgreSQL. API должен уметь:
- Подключаться к базе данных PostgreSQL.
- Создавать таблицы с помощью Alembic.
- Реализовывать CRUD-операции для сущности "Книга" (Book).

---

## **📌 Шаг 1: Создание проекта и установка зависимостей**
1. Создайте новую директорию для проекта и перейдите в неё:
    ```sh
    mkdir fastapi_books && cd fastapi_books
    ```
2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```
3. Установите необходимые зависимости:
    ```sh
    pip install fastapi uvicorn sqlalchemy psycopg2 alembic
    ```
4. Создайте папку `routers` для маршрутов API:
    ```sh
    mkdir routers
    ```

---

## **📌 Шаг 2: Настройка базы данных**
1. Создайте файл `database.py` в корне проекта.
2. Реализуйте подключение к PostgreSQL и настройте сессии SQLAlchemy:
    ```python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, declarative_base, Session
    
    DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/books_db"
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    ```
3. Проверьте подключение к базе данных:
    ```python
    from database import engine
    print(engine.connect())
    ```

✅ **Результат:** Должно быть установлено соединение с базой данных.

---

## **📌 Шаг 3: Создание моделей SQLAlchemy**
1. Создайте файл `models.py` в корне проекта.
2. Определите модель `BookDB`:
    ```python
    from sqlalchemy import Column, Integer, String
    from database import Base
    
    class BookDB(Base):
        __tablename__ = "books"
        id = Column(Integer, primary_key=True, index=True)
        title = Column(String, index=True)
        author = Column(String, nullable=True)
    ```

✅ **Результат:** Определена модель книги с полями `id`, `title`, `author`.

---

## **📌 Шаг 4: Настройка Alembic и миграции**
1. Инициализируйте Alembic:
    ```sh
    alembic init alembic
    ```
2. Откройте файл `alembic.ini` и настройте строку подключения:
    ```ini
    sqlalchemy.url = postgresql+psycopg2://user:password@localhost:5432/books_db
    ```
3. В файле `alembic/env.py` добавьте поддержку моделей:
    ```python
    from database import DATABASE_URL
    config.set_main_option("sqlalchemy.url", DATABASE_URL)
    from database import Base
    from models import *
    target_metadata = Base.metadata
    ```
4. Создайте и примените миграции:
    ```sh
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    ```
✅ **Результат:** В базе данных создана таблица `books`.

---

## **📌 Шаг 5: Реализация API (CRUD-операции)**
### **1. Создание схем Pydantic (`schemas.py`)**
```python
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str | None = None

class BookResponse(BookCreate):
    id: int
    
    class Config:
        orm_mode = True
```
✅ **Результат:** Определены схемы для валидации данных API.

---

### **2. Реализация маршрутов API (`routers/books.py`)**
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
```
✅ **Результат:** API теперь может добавлять и получать книги из базы.

---

### **3. Подключение маршрутов в FastAPI (`main.py`)**
```python
from fastapi import FastAPI
from routers.books import router as books_router

app = FastAPI()
app.include_router(books_router, prefix="/books", tags=["books"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}
```
✅ **Результат:** Приложение FastAPI готово к запуску.

---

## **📌 Шаг 6: Запуск и тестирование API**
1. Запустите сервер FastAPI:
    ```sh
    uvicorn main:app --reload
    ```
2. Перейдите в браузере по адресу `http://127.0.0.1:8000/docs`.
3. Протестируйте доступные маршруты (`POST /books`, `GET /books`).

✅ **Результат:** API полностью функционирует!

---

🎯 **Финальный результат:** Рабочий API на FastAPI, использующий SQLAlchemy и PostgreSQL для хранения данных! 🚀

