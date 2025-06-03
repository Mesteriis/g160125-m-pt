# **Live-coding-1: Внедрение SQLAlchemy в FastAPI**

## **📌 Секция 1: Настройка проекта и БД**
### **1.1. Создание структуры проекта**
```sh
mkdir fastapi_books && cd fastapi_books
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy psycopg2 alembic
mkdir routers
```

### **1.2. Создание файла `database.py`**
📄 **Создаём `database.py` в корне проекта:**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# URL для подключения к базе данных PostgreSQL
DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/books_db"

# Создаём объект подключения к БД
engine = create_engine(DATABASE_URL)

# Создаём сессию для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для определения моделей
Base = declarative_base()

# Функция-зависимость для работы с БД
# Используется в эндпоинтах для получения сессии

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### **1.3. Проверка соединения с БД**
```python
from database import engine
print(engine.connect())
```
✅ **Если ошибок нет, соединение установлено!**

---

## **📌 Секция 2: Создание моделей SQLAlchemy**
### **2.1. Создание `models.py`**
📄 **Создаём `models.py` в корне проекта:**
```python
from sqlalchemy import Column, Integer, String
from database import Base

# Определение модели книги
class BookDB(Base):
    __tablename__ = "books"  # Название таблицы в БД
    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    title = Column(String, index=True)  # Название книги
    author = Column(String, nullable=True)  # Автор книги (может быть пустым)
```

✅ **Теперь у нас есть модель таблицы!**

---

## **📌 Секция 3: Настройка Alembic и миграции**
### **3.1. Инициализация Alembic**
```sh
alembic init alembic
```

### **3.2. Настройка Alembic**
📄 **Редактируем `alembic.ini`:**
- Открываем файл `alembic.ini`
- Находим строку:
  ```ini
  sqlalchemy.url = driver://user:pass@localhost/dbname
  ```
- Меняем на:
  ```ini
  sqlalchemy.url = postgresql+psycopg2://user:password@localhost:5432/books_db
  ```

📄 **Редактируем `alembic/env.py`:**
- Добавляем в конец файла перед `run_migrations_online():`
  ```python
  from database import DATABASE_URL
  config.set_main_option("sqlalchemy.url", DATABASE_URL)
  from database import Base
  from models import *
  target_metadata = Base.metadata
  ```

### **3.3. Генерация миграции**
```sh
alembic revision --autogenerate -m "Initial migration"
```

### **3.4. Применение миграции**
```sh
alembic upgrade head
```
✅ **Теперь таблица `books` создана в базе данных!**

---

## **📌 Секция 4: Реализация CRUD-операций**

### **4.1.1 Создание `schemas.py`**
📄 **Создаём `schemas.py` в корне проекта:**
```python
from pydantic import BaseModel

# Модель для валидации входящих данных
class BookCreate(BaseModel):
    title: str
    author: str | None = None

# Модель для ответа API, включает ID книги
class BookResponse(BookCreate):
    id: int

    class Config:
        orm_mode = True  # Позволяет SQLAlchemy моделям работать с Pydantic
```

Этот код определяет **Pydantic-схемы**, которые используются для валидации данных в API FastAPI и их корректного преобразования при передаче между клиентом и сервером.

### **4.1.2. Подробный разбор кода**
```python
from pydantic import BaseModel
```
📌 **Импортируем `BaseModel`** из Pydantic — это базовый класс, от которого наследуются схемы данных. Он позволяет автоматически проверять входные данные и сериализовать объекты в JSON.

#### **4.1.2.1. Класс `BookCreate`**
```python
class BookCreate(BaseModel):
    title: str
    author: str | None = None
```
📌 **Эта схема используется для создания книг в API**.  

##### **Разбор полей:**
- **`title: str`** – обязательное поле, передаваемое пользователем. FastAPI автоматически проверит, что `title` — это строка.
- **`author: str | None = None`** – поле автора книги. Оно необязательное (`None` по умолчанию).

##### **Где используется?**
- При создании книги (`POST /books`):
```python
@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = BookDB(**book.dict())  
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
```
- **FastAPI автоматически проверит** данные, отправленные клиентом, прежде чем передать их в `BookDB`.

#### **4.1.2.2. Класс `BookResponse`**
```python
class BookResponse(BookCreate):
    id: int

    class Config:
        orm_mode = True
```
📌 **Эта схема используется для формирования ответа API** (например, когда клиент запрашивает список книг).  

##### **Разбор полей:**
- **`id: int`** – добавляется к `BookCreate`, так как ID создаётся базой данных и не передаётся пользователем.
- **`class Config:`**  
  - **`orm_mode = True`** – позволяет FastAPI правильно работать с SQLAlchemy-моделями и автоматически конвертировать их в JSON-ответ.

##### **Где используется?**
- В `response_model=BookResponse`, например:
```python
@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book  # ✅ FastAPI автоматически преобразует SQLAlchemy-объект в Pydantic-модель
```
- **Без `orm_mode = True`** FastAPI не смог бы правильно сериализовать объект `BookDB`.

#### **4.1.2.3. Итог**
🔹 **`BookCreate`** – для валидации входных данных при создании книги.  
🔹 **`BookResponse`** – для формирования ответа API с добавлением `id`.  
🔹 **`orm_mode = True`** – позволяет FastAPI преобразовывать SQLAlchemy-модели в Pydantic.  

Этот код помогает нам **гарантировать, что API получает и возвращает только корректные данные**. 🚀

✅ **Теперь у нас есть схемы для валидации данных!**

### **4.2. Создание `routers/books.py`**
📄 **Создаём `routers/books.py`:**
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
```

### **4.3. Добавление роутеров в `main.py`**
📄 **Создаём `main.py`:**
```python
from fastapi import FastAPI
from routers.books import router as books_router

app = FastAPI()
app.include_router(books_router, prefix="/books", tags=["books"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}
```

✅ **Теперь у нас есть API с базовыми CRUD-операциями!**
