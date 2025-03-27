## Цель практики
# Освоение базовых навыков работы с шаблонами Django,
# включая создание и использование собственных шаблонных тегов,
# подключение статики и работу с фильтрами в шаблонах.

## Задачи

### 1. Собственные шаблонные теги через `simple_tag`

#### Описание
# Создайте собственный шаблонный тег `upper_words` через `simple_tag` и протестируйте
# его в представлении `article_detail` в шаблоне `article_detail.html`.

#### Шаги
# 1. Создайте файл `upper_words.py` в папке `news/templatetags`.
# 2. В файле `upper_words.py` создайте тег шаблона `upper_words` через `simple_tag`:
#    ```python
#    from django import template

#    register = template.Library()

#    @register.simple_tag
#    def upper_words(value):
#        return value.upper()
#    ```
# 3. Протестируйте тег `upper_words` в представлении `article_detail` в шаблоне `article_detail.html`:
#    ```html
#    {% load upper_words %}
#    <p>{{ article.title|upper_words }}</p>
#    ```
# 4. После создания тега и регистрации с помощью `template.Library()` перезапустите сервер.

### 2. Подключение статики в шаблоне `base.html`

#### Описание
# Создайте папку `static` в приложении `news` и подключите статику в шаблоне `base.html`.

#### Шаги
# 1. Создайте папку `static` в приложении `news`.
# 2. Внутри папки `static` создайте папку `news`.
# 3. В папке `news` создайте папку `css` и файл `main.css`, а также папку `js` и файл `main.js`.
# 4. В файле `main.css` создайте тестовые стили, а в файле `main.js` создайте тестовый скрипт.
# 5. Подключите статику в шаблоне `base.html` через тег `{% load static %}` и тег `{% static %}`:
#    ```html
#    {% load static %}
#    <link rel="stylesheet" type="text/css" href="{% static 'news/css/main.css' %}">
#    <script src="{% static 'news/js/main.js' %}"></script>
#    ```
# 6. Проверьте работу статики на всех страницах.
# 7. После создания и подключения статики перезапустите сервер.

### 3. Работа с фильтрами в шаблонах

#### Описание
# Изучите работу следующих фильтров в шаблоне `article_preview.html`: `length`, `truncatechars`, `join`.
# Добавьте цикл для вывода тегов новости.

#### Шаги
# 1. В шаблоне `article_preview.html` используйте фильтр `length` для отображения длины текста:
#    ```html
#    <p>Длина текста: {{ article.text|length }}</p>
#    ```
# 2. В шаблоне `article_preview.html` используйте фильтр `truncatechars` для обрезки текста:
#    ```html
#    <p>{{ article.text|truncatechars:50 }}</p>
#    ```
# 3. В шаблоне `article_preview.html` используйте фильтр `join` для объединения тегов новости:
#    ```html
#    <p>Теги: {{ article.tags|join:", " }}</p>
#    ```
# 4. Добавьте цикл для вывода тегов новости в шаблоне `article_preview.html`:
#    ```html
#    <ul>
#        {% for tag in article.tags %}
#            <li>{{ tag }}</li>
#        {% endfor %}
#    </ul>
#    ```

## Финальный результат:
# 1. Создание и использование собственного шаблонного тега `upper_words` через `simple_tag`.
# 2. Создание папки `static` в приложении `news` и подключение статики в шаблоне `base.html`.
# 3. Изучение и использование фильтров `length`, `truncatechars`, `join` в шаблоне `article_preview.html`.
# 4. Добавление цикла для вывода тегов новости в шаблоне `article_preview.html`.
