## Урок 6

### Задача: Получить все статьи, которые принадлежат категории "Технологии".
```python
# Получаем объект категории "Технологии"
technology_category = Category.objects.get(name="Технологии")

# Фильтруем статьи по этой категории
articles_in_technology = Article.objects.filter(category=technology_category)

# Выводим результат
for article in articles_in_technology:
    print(article.title)
```

### Задача: Получить все статьи, которые имеют тег "Инновации".
```python
# Получаем объект тега "Инновации"
innovation_tag = Tag.objects.get(name="Инновации")

# Фильтруем статьи по этому тегу
articles_with_innovation_tag = Article.objects.filter(tags=innovation_tag)

# Выводим результат
for article in articles_with_innovation_tag:
    print(article.title)
```

### Задача: Получить все статьи, отсортированные по заголовку в порядке убывания
```python
# Сортируем статьи по заголовку в порядке убывания
articles_sorted_by_title = Article.objects.all().order_by('-title')

# Выводим результат
for article in articles_sorted_by_title:
    print(article.title, article.id)
```

### Задача: Получить все статьи, у которых количество просмотров больше 10, отсортированные по количеству просмотров в порядке возрастания.
Для начала можно изменить у некоторых статей количество просмотров, чтобы выборка имела смысл
```python
# Фильтруем статьи, у которых id больше 30, и обновляем их количество просмотров
Article.objects.filter(id__gt=30).update(views=20)
```
```python
# Фильтруем статьи по количеству просмотров и сортируем их
articles_filtered_and_sorted = Article.objects.filter(views__gt=10).order_by('views')

# Выводим результат
for article in articles_filtered_and_sorted:
    print(article.title, article.views)
```

**commit: `Урок 6: Рассмотрели операции на фильтрацию и сортировку данных, а так же лукапы`**

### Решение первой практики

### Задание 1: Фильтрация статей по категории
**Задача:** Получить все статьи, которые принадлежат категории "Технологии".

**Решение:**
```python
# Получаем объект категории "Технологии"
technology_category = Category.objects.get(name="Технологии")

# Фильтруем статьи по этой категории
articles_in_technology = Article.objects.filter(category=technology_category)

# Выводим результат
for article in articles_in_technology:
    print(article.title)
```
**Пояснение:**
1. Получаем объект категории "Технологии".
2. Фильтруем статьи, которые принадлежат этой категории.
3. Выводим заголовки всех статей, которые соответствуют этой категории.

### Задание 2: Фильтрация статей по тегу
**Задача:** Получить все статьи, которые имеют тег "Инновации".

**Решение:**
```python
# Получаем объект тега "Инновации"
innovation_tag = Tag.objects.get(name="Инновации")

# Фильтруем статьи по этому тегу
articles_with_innovation_tag = Article.objects.filter(tags=innovation_tag)

# Выводим результат
for article in articles_with_innovation_tag:
    print(article.title)
```
**Пояснение:**
1. Получаем объект тега "Инновации".
2. Фильтруем статьи, которые имеют этот тег.
3. Выводим заголовки всех статей, которые соответствуют этому тегу.

### Задание 3: Сортировка статей по дате публикации
**Задача:** Получить все статьи, отсортированные по дате публикации в порядке убывания.

**Решение:**
```python
# Сортируем статьи по дате публикации в порядке убывания
articles_sorted_by_date = Article.objects.all().order_by('-publication_date')

# Выводим результат
for article in articles_sorted_by_date:
    print(article.title, article.publication_date)
```
**Пояснение:**
1. Сортируем статьи по дате публикации в порядке убывания.
2. Выводим заголовки и даты публикации всех статей.

### Задание 4: Фильтрация и сортировка статей по количеству просмотров
**Задача:** Получить все статьи, у которых количество просмотров больше 10, отсортированные по количеству просмотров в порядке возрастания.

**Решение:**
```python
# Фильтруем статьи по количеству просмотров и сортируем их
articles_filtered_and_sorted = Article.objects.filter(views__gt=10).order_by('views')

# Выводим результат
for article in articles_filtered_and_sorted:
    print(article.title, article.views)
```
**Пояснение:**
1. Фильтруем статьи, у которых количество просмотров больше 10.
2. Сортируем эти статьи по количеству просмотров в порядке возрастания.
3. Выводим заголовки и количество просмотров всех статей, которые соответствуют условию.

### Задание 5: Фильтрация статей по содержанию
**Задача:** Получить все статьи, у которых содержание содержит слово "кошки".

**Решение:**
```python
# Фильтруем статьи по содержанию
articles_with_cats_in_content = Article.objects.filter(content__icontains="кошки")

# Выводим результат
for article in articles_with_cats_in_content:
    print(article.title)
```
**Пояснение:**
1. Фильтруем статьи, у которых заголовок содержит слово "кошки" без учета регистра.
2. Выводим заголовки всех статей, которые соответствуют этому условию.

### Задание 6: Фильтрация статей по диапазону дат
**Задача:** Получить все статьи, опубликованные в октябре 2023 года.

**Решение:**
```python
# Фильтруем статьи по диапазону дат
articles_in_october_2023 = Article.objects.filter(publication_date__range=(datetime(2023, 10, 1), datetime(2023, 10, 31)))

# Выводим результат
for article in articles_in_october_2023:
    print(article.title, article.publication_date)
```
**Пояснение:**
1. Фильтруем статьи, опубликованные в октябре 2023 года.
2. Выводим заголовки и даты публикации всех статей, которые соответствуют этому условию.

### Задание 7: Фильтрация статей по году публикации
**Задача:** Получить все статьи, опубликованные в 2023 году.

**Решение:**
```python
# Фильтруем статьи по году публикации
articles_in_2023 = Article.objects.filter(publication_date__year=2023)

# Выводим результат
for article in articles_in_2023:
    print(article.title, article.publication_date)
```
**Пояснение:**
1. Фильтруем статьи, опубликованные в 2023 году.
2. Выводим заголовки и даты публикации всех статей, которые соответствуют этому условию.

### Задание 8: Фильтрация статей по наличию тегов
**Задача:** Получить все статьи, у которых есть хотя бы один тег.

**Решение:**
```python
# Фильтруем статьи, у которых есть хотя бы один тег
articles_with_tags = Article.objects.filter(tags__isnull=False)

# Выводим результат
for article in articles_with_tags:
    print(article.title)
```
**Пояснение:**
1. Фильтруем статьи, у которых есть хотя бы один тег.
2. Выводим заголовки всех статей, которые соответствуют этому условию.

### Задание 9: Фильтрация статей по количеству тегов
**Задача:** Получить все статьи, у которых количество тегов больше 3.

**Решение:**
```python
# Фильтруем статьи по количеству тегов
articles_with_more_than_three_tags = Article.objects.annotate(num_tags=Count('tags')).filter(num_tags__gt=3)

# Выводим результат
for article in articles_with_more_than_three_tags:
    print(article.title, article.num_tags)
```
**Пояснение:**
1. Аннотируем статьи, подсчитывая количество тегов для каждой статьи.
2. Фильтруем статьи, у которых количество тегов больше 3.
3. Выводим заголовки и количество тегов всех статей, которые соответствуют этому условию.

### Задание 10: Фильтрация статей по наличию определенного слова в контенте
**Задача:** Получить все статьи, у которых контент содержит слово "ученые".

**Решение:**
```python
# Фильтруем статьи по наличию слова "открыли" в заголовке
articles_with_open_in_title = Article.objects.filter(title__icontains="открыли")

# Выводим результат
for article in articles_with_open_in_title:
    print(article.title)
```
**Пояснение:**
1. Фильтруем статьи, у которых заголовок содержит слово "открыли" без учета регистра.
2. Выводим заголовки всех статей, которые соответствуют этому условию.

**commit: `Урок 6: Разобрали первое практическое задание`**

### Новое поле `slug` в модели данных `Article`
#### Сначала нужно очистить БД
`python manage.py flush`

#### Добавляем `slug` и переопределяем метод сохранения
```python
from django.utils.text import slugify


class Article(models.Model):
    ...
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

```

#### Создаём миграцию
`python manage.py makemigrations`

#### Применяем миграцию
`python manage.py migrate`

#### Записываем новый дамп данных
`python manage.py loaddata articles_3.json`

**commit: `Урок 6: Добавили slug в Article`**

#### Проверяем работу slug

```python
# Создаем категорию, если она еще не существует
category, created = Category.objects.get_or_create(name="Технологии")

# Создаем теги, если они еще не существуют
tag1, created = Tag.objects.get_or_create(name="Технологии")
tag2, created = Tag.objects.get_or_create(name="Инновации")

# Создаем статью
article = Article.objects.create(
    title="Новая статья о технологиях",
    content="Это тестовая статья для проверки работы поля slug.",
    category=category,
)

# Добавляем теги к статье
article.tags.add(tag1, tag2)

# Сохраняем статью, чтобы убедиться, что slug был сгенерирован
article.save()

# Выводим информацию о статье, чтобы убедиться, что slug был сгенерирован
print(f"Title: {article.title}")
print(f"Slug: {article.slug}")
print(f"Content: {article.content}")
print(f"Category: {article.category.name}")
print(f"Tags: {', '.join([tag.name for tag in article.tags.all()])}")
```

**commit: `Урок 6: Проверили работу slug`**

### Добавление слага в маршруты и представления
```python
# news/urls.py
urlpatterns = [
    ...
    path('catalog/<slug:slug>/', views.get_detail_article_by_slag, name='detail_article_by_slag'),
]
```
```python
# news/views.py
def get_detail_article_by_slag(request, slug):
    article = get_object_or_404(Article, slug=slug)
    ...
    return render(request, 'news/article_detail.html', context=context)
```

**commit: `Урок 6: Добавление slug в маршруты и представления`**

### Добавление пользовательского менеджера модели

#### Создание пользовательского менеджера
```python
class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def sorted_by_title(self):
        return self.get_queryset().all().order_by('-title')
```

#### Добавление пользовательского менеджера в модель
```python
class Article(models.Model):
    ...
    is_active = models.BooleanField(default=True)

    objects = ArticleManager()
```

#### Создание миграции
`python manage.py makemigrations`

#### Применение миграции
`python manage.py migrate`

#### Проверка пользовательского менеджера модели в shell_plus
```python
published_articles = Article.objects.sorted_by_title()
for i in published_articles:
    print(i.title)
```

**commit: `Урок 6: Добавление пользовательского менеджера модели Article`**