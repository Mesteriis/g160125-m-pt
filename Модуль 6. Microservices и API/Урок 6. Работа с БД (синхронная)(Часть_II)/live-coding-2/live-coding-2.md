# Live-Coding 2: Продвинутая работа с SQLAlchemy в FastAPI

## 1. Оптимизация SQL-запросов: `selectinload()` и `joinedload()`

### 1.1 Проблема N+1 запроса

В SQLAlchemy при загрузке связанных объектов (например, авторов и их книг) по умолчанию выполняется отдельный SQL-запрос для каждого объекта. Это приводит к проблеме **N+1 запроса**, когда при получении `N` записей отправляется `N+1` SQL-запрос.

Пример проблемы:
```python
# Получение всех книг
books = db.query(Book).all()
print([{ "id": b.id, "title": b.title, "author": b.author.name if b.author else None } for b in books])
```

### 1.2 Решение: `selectinload()` и `joinedload()`

**Как работают методы:**
- **`selectinload()`** – делает один дополнительный запрос с `IN ()`, загружая все связанные объекты разом.
- **`joinedload()`** – использует SQL JOIN, загружая данные в одном большом запросе.

Применение в консоли:
```python
from sqlalchemy.orm import selectinload, joinedload

# 1. Получение книг с авторами (selectinload)
books = db.query(Book).options(selectinload(Book.author)).all()
print([{ "id": b.id, "title": b.title, "author": b.author.name if b.author else None } for b in books])

# 2. Получение книг с тегами (joinedload)
books = db.query(Book).options(joinedload(Book.tags)).all()
print([{ "id": b.id, "title": b.title, "tags": [t.name for t in b.tags] } for b in books])
```

### 1.3 `selectinload()` vs `joinedload()` в сравнении с Django ORM

- **`selectinload()`** ≈ `prefetch_related()` в Django – делает несколько запросов, но загружает данные разом.
- **`joinedload()`** ≈ `select_related()` в Django – использует SQL JOIN, загружая всё в один запрос.

Когда использовать:
- `selectinload()` – если много связанных записей и база данных плохо работает с `JOIN`.
- `joinedload()` – если нужно сразу получить все данные в одном запросе.

---

## 2. Новые эндпоинты для работы с книгами, авторами и тегами

Эти эндпоинты размещаются в файле `routers/books.py`. Они позволяют управлять авторами, тегами и книгами в базе данных.

### 2.1 Список всех авторов
```python
@router.get("/authors/", response_model=list[AuthorSchema])
def get_authors(db: Session = Depends(get_db)):
    """Возвращает список всех авторов."""
    return db.query(Author).all()
```

### 2.2 Получение книг конкретного автора
```python
@router.get("/authors/{author_id}/books", response_model=list[BookResponse])
def get_books_by_author(author_id: int, db: Session = Depends(get_db)):
    """Возвращает список книг определенного автора."""
    return db.query(Book).filter(Book.author_id == author_id).all()
```

### 2.3 Список всех тегов
```python
@router.get("/tags/", response_model=list[TagSchema])
def get_tags(db: Session = Depends(get_db)):
    """Возвращает список всех тегов."""
    return db.query(Tag).all()
```

### 2.4 Получение книг по тегу
```python
@router.get("/tags/{tag_id}/books", response_model=list[BookResponse])
def get_books_by_tag(tag_id: int, db: Session = Depends(get_db)):
    """Возвращает список книг, относящихся к определенному тегу."""
    return db.query(Book).join(book_tag_association).filter(book_tag_association.c.tag_id == tag_id).all()
```

### 2.5 Поиск книги по названию
```python
@router.get("/books/search/", response_model=list[BookResponse])
def search_books(keyword: str, db: Session = Depends(get_db)):
    """Поиск книг по названию с использованием нечёткого поиска."""
    return db.query(Book).filter(Book.title.ilike(f"%{keyword}%")).all()
```
