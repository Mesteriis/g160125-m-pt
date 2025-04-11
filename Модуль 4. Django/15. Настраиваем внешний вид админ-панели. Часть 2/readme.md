## Урок 15

### Добавление неизменяемых полей

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    readonly_fields = ('publication_date', 'views')
```

**commit: `Урок 15: пометили часть полей как неизменяемые`**

### Добавление вывода объектов по датам

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    date_hierarchy = 'publication_date'
```

**commit: `Урок 15: добавили иерархическое отображение по дате публикации`**

### Добавление редатированя полей в общем списке объектов

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    list_editable = ('title', 'category')
```

**commit: `Урок 15: добавили возможность изменения заголовка из списка объектов`**

### Перенос кнопок сохранения в верхнюю часть формы редактирования

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    list_editable = ('title', 'category')
```

**commit: `Урок 15: перенесли кнопки сохранения в верхнюю часть формы`**

### Включение возможности сохранения объекта как нового

#### admin.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    list_editable = ('title', 'category')
```

**commit: `Урок 15: включили возможность сохранения объекта как нового`**

### установка `django-jazzmin`
```shell
pip install django-jazzmin
```

### настройка `django-jazzmin`

#### settings.py
```python
INSTALLED_APPS = [
    'jazzmin',
    ...
]
```
```python
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
            ],
        'builtins': ['news.templatetags.customtags']
        },
    },
]
```

**commit: `Урок 15: установили django-jazzmin`**

### настройка интерфейса `django-jazzmin`

#### settings.py
```python
JAZZMIN_SETTINGS = {
    "site_title": "My Blog Admin",  # Заголовок административной панели
    "site_header": "My Blog",  # Заголовок окна браузера
    "site_brand": "My Blog",  # Бренд сайта
    "welcome_sign": "Welcome to My Blog Admin",  # Приветственное сообщение
    "copyright": "My Blog Ltd",  # Информация о копирайте
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    "show_sidebar": True,  # Показать боковую панель
    "navigation_expanded": True,  # Развернуть навигацию
    "hide_apps": [],  # Скрыть приложения
    "hide_models": [],  # Скрыть модели
    "default_icon_parents": "fas fa-chevron-circle-right",  # Иконка для родительских элементов
    "default_icon_children": "fas fa-circle",  # Иконка для дочерних элементов
    "related_modal_active": False,  # Включить модальные окна для связанных объектов
    "custom_css": None,  # Пользовательский CSS
    "custom_js": None,  # Пользовательский JS
    "use_google_fonts_cdn": True,  # Использовать Google Fonts CDN
    "show_ui_builder": True,  # Показать конструктор интерфейса
}
```

**commit: `Урок 15: настроили интерфейс django-jazzmin`**