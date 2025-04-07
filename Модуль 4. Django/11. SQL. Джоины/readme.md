## Урок 11

### Небольшие правки в проект

Ошибка `ManyRelatedManager object is not iterable` возникает потому, что вы пытаетесь итерировать по `ManyRelatedManager` напрямую,
вместо того чтобы использовать метод `.all()` для получения всех связанных объектов.

Чтобы исправить эту ошибку, вам нужно использовать `article.tags.all()` для получения всех тегов, связанных с конкретной статьей.

**commit: `Урок 11: исправили шаблоны карточек для отображения тегов новостей`**

1. **Обновление базового шаблона (base.html):**
   - **Изменения:**
     - Добавлены стили для фона и текста:
       ```html
       <style>
           body {
               background-color: #f8f9fa;
               color: #343a40;
           }
           .navbar {
               background-color: #343a40;
           }
           .navbar-nav .nav-link {
               color: #ffffff;
           }
           .navbar-nav .nav-link\:hover {
               color: #ffc107;
           }
           .card {
               margin-bottom: 20px;
           }
           .footer {
               background-color: #343a40;
               color: #ffffff;
               text-align: center;
               padding: 10px 0;
           }
       </style>
       ```
     - Обновлены структура и стили навигационного меню:
       ```html
       <nav class="navbar navbar-expand-lg navbar-dark">
           <div class="container-fluid">
               <a class="navbar-brand" href="#">Info to Go</a>
               <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                   <span class="navbar-toggler-icon"></span>
               </button>
               <div class="collapse navbar-collapse" id="navbarNav">
                   <ul class="navbar-nav ms-auto">
                       {% include "include/nav_menu.html" %}
                   </ul>
               </div>
           </div>
       </nav>
       ```
   - **Причина:**
     - Улучшение общего внешнего вида приложения и повышение удобства использования.

2. **Обновление шаблона about.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для центрирования текста и улучшения отступов:
       ```html
       <h1 class="text-center mb-4">О сайте</h1>
       <p class="text-center">Добро пожаловать на наш сайт!</p>
       <p class="text-center">На нашем сайте, новостей {{ news_count }}, пользователей {{ users_count }}.</p>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида страницы "О сайте".

3. **Обновление шаблона main.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для центрирования текста и улучшения отступов:
       ```html
       <h1 class="text-center mb-4">Главная страница</h1>
       <p class="text-center">Добро пожаловать на сайт!</p>
       <p class="text-center">На нашем сайте, новостей {{ news_count }}, пользователей {{ users_count }}.</p>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида главной страницы.

4. **Обновление шаблона catalog.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для центрирования текста и улучшения отступов:
       ```html
       <h1 class="text-center mb-4">Каталог новостей Info to Go</h1>
       <p class="text-center">Всего новостей: {{ news_count }}</p>
       <p class="text-center">Всего пользователей: {{ users_count }}</p>
       ```
     - Добавлены классы Bootstrap для создания сетки из двух колонок для карточек новостей:
       ```html
       <div class="row">
           {% for article in news %}
               <div class="col-md-6 mb-4">
                   {% include "include/article_preview.html" with article=article %}
               </div>
           {% endfor %}
       </div>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида страницы каталога новостей, а также улучшение отображения карточек новостей.

5. **Обновление шаблона article_detail.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для улучшения внешнего вида карточки новости:
       ```html
       <div class="card">
           <div class="card-body">
               <h5 class="card-title">{% upper_words article.title %}</h5>
               <p class="card-text">{{ article.content }}</p>
               <p class="card-text">{{ article.category }}</p>
               {% for tag in article.tags.all %}
                   <span class="badge bg-info">{{ tag }}</span>
               {% endfor %}
               <p class="card-text">{{ article.id_author }}</p>
               <p class="card-text">{{ article.id }}</p>
               <p class="card-text">{{ article.publication_date }}</p>
               <p class="card-text">{{ article.views }}</p>
               <p class="card-text">{{ article.favorites_count }}</p>
           </div>
       </div>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида страницы детального представления новости.

6. **Обновление шаблона article_preview.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для улучшения внешнего вида карточки новости:
       ```html
       <div class="card">
           <div class="card-body">
               <h5 class="card-title">{{ article.title }}</h5>
               <p class="card-text">{{ article.content|truncatechars:50 }}</p>
               <p class="card-text">{{ article.category }}</p>
               {% for tag in article.tags.all %}
                   <span class="badge bg-info">{{ tag }}</span>
               {% endfor %}
               <p class="card-text">{{ article.id_author }}</p>
               <p class="card-text">{{ article.id }}</p>
               <p class="card-text">{{ article.publication_date }}</p>
               <p class="card-text">{{ article.views }}</p>
               <p class="card-text">{{ article.favorites_count }}</p>
               <a href="{% url 'detail_article_by_id' article.id %}" class="btn btn-primary">Подробнее</a>
           </div>
       </div>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида краткого представления новости.

7. **Обновление шаблона nav_menu.html:**
   - **Изменения:**
     - Добавлены классы Bootstrap для улучшения внешнего вида навигационного меню:
       ```html
       <ul class="navbar-nav">
           {% for item in menu %}
               <li class="nav-item">
                   <a class="nav-link" href="{% url item.url_name %}">{{ item.title }}</a>
               </li>
               {% if not forloop.last %}
                   <li class="nav-item"><hr class="dropdown-divider"/></li>
               {% endif %}
           {% endfor %}
       </ul>
       ```
   - **Причина:**
     - Улучшение читаемости и внешнего вида навигационного меню.

**commit: `Урок 11: улучшили внешний вид и пользовательский интерфейса приложения`**

ссылка "Каталог" в приложении вела на заглушку

**commit: `Урок 11: поменяли маршруты`**

### добавление сортировки на страницу каталога

```python
# Считаем параметры из GET-запроса
sort = request.GET.get('sort', 'publication_date')  # по умолчанию сортируем по дате загрузки
order = request.GET.get('order', 'desc')  # по умолчанию сортируем по убыванию

# Проверяем, дали ли мы разрешение на сортировку по этому полю
valid_sort_fields = {'publication_date', 'views'}
if sort not in valid_sort_fields:
    sort = 'publication_date'

# Обрабатываем направление сортировки
if order == 'asc':
    order_by = sort
else:
    order_by = f'-{sort}'
```

1. **Считывание параметров из GET-запроса:**
   ```python
   sort = request.GET.get('sort', 'publication_date')  # по умолчанию сортируем по дате загрузки
   order = request.GET.get('order', 'desc')  # по умолчанию сортируем по убыванию
   ```
   - **Описание:**
     - Мы используем метод `request.GET.get()` для получения параметров `sort` и `order` из GET-запроса.
     - Если параметр `sort` не указан, по умолчанию используется `'publication_date'`.
     - Если параметр `order` не указан, по умолчанию используется `'desc'` (по убыванию).

2. **Проверка разрешенных полей для сортировки:**
   ```python
   valid_sort_fields = {'publication_date', 'views'}
   if sort not in valid_sort_fields:
       sort = 'publication_date'
   ```
   - **Описание:**
     - Мы определяем множество `valid_sort_fields`, которое содержит разрешенные поля для сортировки: `'publication_date'` и `'views'`.
     - Если значение `sort` не входит в множество `valid_sort_fields`, мы устанавливаем `sort` в `'publication_date'` по умолчанию.

3. **Обработка направления сортировки:**
   ```python
   if order == 'asc':
       order_by = sort
   else:
       order_by = f'-{sort}'
   ```
   - **Описание:**
     - Мы проверяем значение параметра `order`.
     - Если `order` равен `'asc'` (по возрастанию), мы устанавливаем `order_by` в `sort`.
     - В противном случае (по убыванию), мы устанавливаем `order_by` в `f'-{sort}'`, добавляя символ `-` перед полем сортировки, чтобы указать порядок по убыванию.

### Причина изменений:
- **Улучшение гибкости сортировки:**
  - Пользователи могут указывать параметры сортировки через GET-запрос, что делает интерфейс более гибким и удобным.
- **Безопасность и валидация:**
  - Проверка разрешенных полей для сортировки предотвращает использование недопустимых полей, что повышает безопасность и надежность приложения.
- **Улучшение пользовательского опыта:**
  - По умолчанию сортировка выполняется по дате загрузки и по убыванию, что соответствует ожиданиям большинства пользователей.

### Пример использования:
- **URL-запрос:**
  - `/news/?sort=views&order=asc` будет сортировать новости по количеству просмотров по возрастанию.
  - `/news/?sort=publication_date&order=desc` будет сортировать новости по дате загрузки по убыванию.

**commit: `Урок 11: добавили сортировку по датам или по просмотрам`**

### Подготовка базы данных для экспериментов с джоинами
**Изменение поля `category_id` в таблице `news_article`. Теперь поле может быть пустым:**
```sql
ALTER TABLE news_article ALTER COLUMN category_id DROP NOT NULL;
```

**Добавление двух новых категорий:**
```sql
INSERT INTO news_category (name) VALUES ('Погода');
INSERT INTO news_category (name) VALUES ('СРОЧНО');
```

**Очистка категории у некоторых статей**
Этот запрос обновляет таблицу `news_article`, устанавливая значение `category_id` в `NULL` для всех статей,
содержание которых не содержит слов 'городе' и 'довольны'.
Оператор `NOT LIKE` используется для проверки, что строка не содержит указанного шаблона.
```sql
UPDATE news_article
SET category_id = NULL
WHERE content NOT LIKE '%городе%'
  AND content NOT LIKE '%довольны%';
```

**commit: `Урок 11: изменили записи в БД чтобы посмотреть на работу джоинов`**