## Урок 9

### Если у вас установлен `pgAdmin` и вы хотите перенести базу данных из `SQLite` в `PostgreSQL`, выполните следующие шаги:

#### Шаг 1: Установите необходимые библиотеки
1. **Установите библиотеку `psycopg2` для Django**:
   ```sh
   pip install psycopg2-binary
   ```

#### Шаг 2: Настройте `PostgreSQL` через `pgAdmin`
1. **Откройте `pgAdmin` и подключитесь к вашему серверу `PostgreSQL`**.
2. **Создайте новую базу данных**:
   - В `pgAdmin`, щелкните правой кнопкой мыши на "Databases" и выберите "Create" > "Database".
   - Введите имя базы данных (например, `itg`) и выберите владельца (например, `postgres`).
   - Нажмите "Save".

#### Шаг 3: Настройте `Django` для использования `PostgreSQL`

1. **Обновите `settings.py`**:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'itg',
           'USER': 'postgres',
           'PASSWORD': 'admin',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

#### Шаг 4: Экспортируйте данные из `SQLite`

1. **Создайте дамп данных из `SQLite`**:
```sh
python manage.py dumpdata --format=json --indent=4 > db.json
```

#### Шаг 5: Примените миграции в `PostgreSQL`

1. **Создайте миграции**:
   ```sh
   python manage.py makemigrations
   ```

2. **Примените миграции**:
   ```sh
   python manage.py migrate
   ```

#### Шаг 6: Импортируйте данные в PostgreSQL

1. **Загрузите данные из JSON файла**:
```sh
python manage.py loaddata db.json
```
или из articles_4.json
```sh
python manage.py loaddata articles_4.json
```

#### Шаг 7: Проверьте данные

1. **Запустите сервер разработки и убедитесь, что все работает**:
```sh
python manage.py runserver
```

#### Шаг 8: Очистите старую базу данных SQLite (опционально)

1. **Удалите файл SQLite базы данных**:
```sh
del db.sqlite3
```

#### Примечания

- **Проверка данных**: Убедитесь, что все данные успешно перенесены и что приложение работает корректно с новой базой данных `PostgreSQL`.
- **Обработка ошибок**: Если возникнут ошибки при импорте данных, проверьте логи и исправьте проблемы в данных или в моделях `Django`.

**commit: `Урок 9: перенесли данные из SQLite в PostgreSQL`**

### Синтаксические конструкции для CRUD-запросов: Основы написания команд `INSERT`, `SELECT`, `UPDATE`, `DELETE`

`CRUD` (`Create`, `Read`, `Update`, `Delete`) — это основные операции, которые выполняются с базой данных.
В `SQL` эти операции соответствуют командам `INSERT`, `SELECT`, `UPDATE` и `DELETE`.
Рассмотрим синтаксис каждой из этих команд и приведем по два примера для каждой операции.

#### 1. Команда `INSERT`
Команда `INSERT` используется для добавления новых записей в таблицу.

**Синтаксис:**
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

**Примеры:**
1. Добавление новой категории:
   ```sql
   INSERT INTO news_category (name)
   VALUES ('Новая категория');
   ```

2. Добавление трех новых статей:
   ```sql
   INSERT INTO news_article (title, content, publication_date, views, category_id, slug, is_active)
   VALUES
   ('Новая статья 1', 'Содержание новой статьи 1', '2023-10-01T12:00:00Z', 0, 1, 'novaya-statya-1', TRUE),
   ('Новая статья 2', 'Содержание новой статьи 2', '2023-10-02T12:00:00Z', 0, 2, 'novaya-statya-2', TRUE),
   ('Новая статья 3', 'Содержание новой статьи 3', '2023-10-03T12:00:00Z', 0, 3, 'novaya-statya-3', TRUE);
   ```

#### 2. Команда `SELECT`
Команда `SELECT` используется для выборки данных из таблицы.

**Синтаксис:**
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Примеры:**
1. Выборка всех статей из категории "Технологии":
   ```sql
   SELECT *
   FROM news_article
   WHERE category_id = (SELECT id FROM news_category WHERE name = 'Технологии');
   ```

2. Выборка всех активных статей:
   ```sql
   SELECT *
   FROM news_article
   WHERE is_active = TRUE;
   ```

#### 3. Команда UPDATE
Команда `UPDATE` используется для обновления существующих записей в таблице.

**Синтаксис:**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**Примеры:**
1. Обновление заголовка статьи с `id` 2:
   ```sql
   UPDATE news_article
   SET title = 'Обновленный заголовок'
   WHERE id = 2;
   ```

2. Увеличение количества просмотров статьи с `id` 1 на 50:
   ```sql
   UPDATE news_article
   SET views = views + 50
   WHERE id = 1;
   ```

#### 4. Команда DELETE
Команда `DELETE` используется для удаления записей из таблицы.

**Синтаксис:**
```sql
DELETE FROM table_name
WHERE condition;
```

**Примеры:**
1. Удаление статьи с `id` 3:
   - Удаление связанных записей в таблице `news_article_tags`:
     ```sql
     DELETE FROM news_article_tags
     WHERE article_id = 3;
     ```
   - Удаление статьи из таблицы `news_article`:
     ```sql
     DELETE FROM news_article
     WHERE id = 3;
     ```

2. Удаление всех неактивных статей:
   - Удаление связанных записей в таблице `news_article_tags` для всех неактивных статей:
     ```sql
     DELETE FROM news_article_tags
     WHERE article_id IN (SELECT id FROM news_article WHERE is_active = FALSE);
     ```
   - Удаление всех неактивных статей из таблицы `news_article`:
     ```sql
     DELETE FROM news_article
     WHERE is_active = FALSE;
     ```

**commit: `Урок 9: посмотрели операции CRUD для SQL`**

### Синтаксические конструкции для CRUD-запросов: Основы написания команд INSERT, SELECT, UPDATE, DELETE с использованием Django ORM
CRUD (Create, Read, Update, Delete) — это основные операции, которые выполняются с базой данных. В Django ORM эти операции соответствуют методам `create()`, `filter()`, `update()` и `delete()`. Рассмотрим синтаксис каждого из этих методов и приведем по два примера для каждой операции.

#### 1. Метод `create()`
Метод `create()` используется для добавления новых записей в таблицу.

**Синтаксис:**
```python
Model.objects.create(field1=value1, field2=value2, ...)
```

**Примеры:**
1. Добавление новой категории:
   ```python
   from news.models import Category

   new_category = Category.objects.create(name='Новая категория')
   ```

2. Добавление трех новых статей:
   ```python
   from news.models import Article, Category

   category1 = Category.objects.get(name='Технологии')
   category2 = Category.objects.get(name='Наука')
   category3 = Category.objects.get(name='Спорт')

   Article.objects.create(
       title='Новая статья 1',
       content='Содержание новой статьи 1',
       publication_date='2023-10-01T12:00:00Z',
       views=0,
       category=category1,
       slug='novaya-statya-1',
       is_active=True
   )

   Article.objects.create(
       title='Новая статья 2',
       content='Содержание новой статьи 2',
       publication_date='2023-10-02T12:00:00Z',
       views=0,
       category=category2,
       slug='novaya-statya-2',
       is_active=True
   )

   Article.objects.create(
       title='Новая статья 3',
       content='Содержание новой статьи 3',
       publication_date='2023-10-03T12:00:00Z',
       views=0,
       category=category3,
       slug='novaya-statya-3',
       is_active=True
   )
   ```

#### 2. Метод `filter()`
Метод `filter()` используется для выборки данных из таблицы.

**Синтаксис:**
```python
Model.objects.filter(field1=value1, field2=value2, ...)
```

**Примеры:**
1. Выборка всех статей из категории "Технологии":
   ```python
   from news.models import Article, Category

   category = Category.objects.get(name='Технологии')
   articles = Article.objects.filter(category=category)
   ```

2. Выборка всех активных статей:
   ```python
   from news.models import Article

   active_articles = Article.objects.filter(is_active=True)
   ```

#### 3. Метод `update()`
Метод `update()` используется для обновления существующих записей в таблице.

**Синтаксис:**
```python
Model.objects.filter(condition).update(field1=value1, field2=value2, ...)
```

**Примеры:**
1. Обновление заголовка статьи с `id` 4:
   ```python
   from news.models import Article

   Article.objects.filter(id=4).update(title='Обновленный заголовок')
   ```

2. Увеличение количества просмотров статьи с `id` 5 на 50:
   ```python
   from news.models import Article
   from django.db.models import F

   Article.objects.filter(id=5).update(views=F('views') + 50)
   ```

#### 4. Метод `delete()`
Метод `delete()` используется для удаления записей из таблицы.

**Синтаксис:**
```python
Model.objects.filter(condition).delete()
```

**Примеры:**
1. Удаление статьи с `id` 6:
   - Удаление связанных записей в таблице `news_article_tags`:
     ```python
     from news.models import Article, Tag

     article = Article.objects.get(id=6)
     article.tags.clear()  # Удаление всех связанных тегов
     article.delete()  # Удаление статьи
     ```

2. Удаление всех неактивных статей:
   - Удаление связанных записей в таблице `news_article_tags` для всех неактивных статей:
     ```python
     from news.models import Article

     inactive_articles = Article.objects.filter(is_active=False)
     for article in inactive_articles:
         article.tags.clear()  # Удаление всех связанных тегов
     inactive_articles.delete()  # Удаление всех неактивных статей
     ```

**commit: `Урок 9: те же запросы, но в Django ORM`**
