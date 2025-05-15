`context_processor` – это более гибкий и производительный вариант, особенно если данные (меню, категории, количество пользователей) нужны во **всех шаблонах**.

---

## **1. Создаём `context_processors.py`**
Создаём файл `context_processors.py` в одном из приложений, например, в `news`:

📂 `news/context_processors.py`
```python
from django.contrib.auth import get_user_model
from django.core.cache import cache
from news.models import Article, Category

def global_context(request):
    return {
        "users_count": get_user_model().objects.count(),
        "news_count": Article.objects.count(),
        "categories": cache.get_or_set("categories", list(Category.objects.all()), 60 * 15),
        "menu": [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "news:catalog"},
            {"title": "Добавить статью", "url": "/news/add/", "url_name": "news:add_article"},
            {"title": "Избранное", "url": "/news/favorites/", "url_name": "news:favorites"},
        ],
    }
```
**Что тут происходит?**
- `users_count`: количество пользователей.
- `news_count`: количество статей.
- `categories`: кешируем список категорий на 15 минут (`cache.get_or_set`).
- `menu`: статичный список (меняется редко, поэтому кешировать его не нужно).

---

## **2. Подключаем к Django**
Теперь нужно сказать Django, что наш `context_processor` нужно загружать во все шаблоны.

В `settings.py` в `TEMPLATES` добавляем путь к нему:

📂 `settings.py`
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "news.context_processors.global_context",  # Добавляем наш context_processor
            ],
        },
    },
]
```

**Теперь контекст автоматически доступен во всех шаблонах!**

---

## **3. Использование в шаблоне**
Раньше, если мы передавали `menu`, `users_count`, `news_count` через `get_context_data()`, теперь этого делать **не нужно**.

Просто используем переменные в шаблоне, например:

📂 `base.html`
```html
<ul>
    {% for item in menu %}
        <li><a href="{{ item.url }}">{{ item.title }}</a></li>
    {% endfor %}
</ul>

<p>Всего пользователей: {{ users_count }}</p>
<p>Всего новостей: {{ news_count }}</p>

<h3>Категории:</h3>
<ul>
    {% for category in categories %}
        <li>{{ category.name }}</li>
    {% endfor %}
</ul>
```

---

## **4. Удаляем `BaseMixin` из CBV**
Теперь `BaseMixin` больше не нужен, так как контекст уже автоматически передаётся. Можно удалить `BaseMixin` из `views.py` и убрать его наследование из CBV.

📂 `views.py` (обновленный)
```python
from django.views.generic import ListView
from news.models import Article

class NewsListView(ListView):
    model = Article
    template_name = "news_list.html"
```

Раньше это было:
```python
class NewsListView(BaseMixin, ListView):
    ...
```
Теперь `BaseMixin` можно просто удалить.

---

## **5. Проверяем кеширование**
Категории кешируются на **15 минут**, но если их часто обновляют (например, админ добавляет новые), можно очищать кеш после изменений.

В `models.py` можно добавить `post_save` сигнал:

📂 `models.py`
```python
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from news.models import Category

@receiver([post_save, post_delete], sender=Category)
def clear_category_cache(sender, **kwargs):
    cache.delete("categories")
```
Теперь кеш автоматически сбрасывается, когда добавляется или удаляется категория.

---

## **Вывод**
✅ **Теперь меню и статистика доступны во всех шаблонах** без передачи контекста в CBV.  
✅ **Кешируется список категорий** (ускоряет работу).  
✅ **Код стал чище** – можно убрать `BaseMixin`.  
