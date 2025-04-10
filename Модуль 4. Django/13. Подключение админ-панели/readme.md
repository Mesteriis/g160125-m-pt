## Урок 13

### Создание суперпользователя

`python manage.py createsuperuser`

**commit: `Урок 13: создали суперпользователя`**

### Регистрация моделей в админ-панели

#### models.py
```python
from .models import Article, Category, Tag


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
```

**commit: `Урок 13: зарегистрировали модели в админ-панели`**

### Изменение заголовка, подзаголовка и тд в админ-панели

#### models.py
```python
admin.site.site_header = "My Blog Admin"
admin.site.site_title = "My Blog Admin Portal"
admin.site.index_title = "Welcome to My Blog Admin Portal"
```

**commit: `Урок 13: изменили заголовки в административной панели`**

### Настроили полей в отображении статей в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active')

admin.site.register(Article, ArticleAdmin)
```

**commit: `Урок 13: настроили поля в отображении статей в админ-панели`**

### Добавление фильтров в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active')
    list_filter = ('category', 'is_active')

admin.site.register(Article, ArticleAdmin)
```

**commit: `Урок 13: добавили фильтры в админ-панель`**

### Добавление поиска в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'content')

admin.site.register(Article, ArticleAdmin)
```

**commit: `Урок 13: добавили поиск в админ-панель`**

### Добавление пользовательского поля в админ-панели

#### models.py
```python
from django.utils.html import format_html

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'views', 'is_active', 'colored_status')

    def colored_status(self, obj):
        return format_html('<span style="color: {};">{}</span>', 'green' if obj.is_active else 'red', obj.is_active)
    colored_status.short_description = 'Статус'

admin.site.register(Article, ArticleAdmin)
```

**commit: `Урок 13: добавили пользовательское поле в админ-панель`

### Добавление дополнительных действий в админ-панели (сделать неактивными выбранные статьи)

#### models.py
```python
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)
    make_inactive.short_description = "Сделать неактивными выбранные статьи

class ArticleAdmin(admin.ModelAdmin):
    ...
    actions = [make_inactive]

    ...
```

**commit: `Урок 13: добавили дополнительные действия в админ-панель`

### Настройка отображения полей в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):
    ...
    fields = ('title', 'content', 'category', 'tags', 'is_active')
    ...
```

**commit: `Урок 13: настроили отображение полей в админ-панели`

### Добавление группировки в админ-панели

#### models.py
```python
class ArticleAdmin(admin.ModelAdmin):   
    ...
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Дополнительные параметры', {
            'fields': ('category', 'tags', 'is_active')
        }),
    )
    ...
```

**commit: `Урок 13: добавили группировку в админ-панель`**      

### Добавлние гибкого редактирования тегов в админ-панели

#### models.py
```python
class TagInline(admin.TabularInline):
    model = Tag.article.through
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    ...
    inlines = [TagInline]
    ...
```

**commit: `Урок 13: добавили гибкое редактирование тегов в админ-панели`**