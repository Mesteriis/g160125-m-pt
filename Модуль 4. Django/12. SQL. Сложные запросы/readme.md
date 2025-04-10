## Урок 12

### HAVING в SQL

`HAVING` в SQL используется для фильтрации групп на основе условий, применяемых к агрегационным функциям. `HAVING` работает аналогично `WHERE`, но применяется к группам, а не к отдельным строкам. Это позволяет фильтровать результаты после группировки и агрегации.

### Примеры использования HAVING

#### PostgreSQL

1. **Подсчет количества статей в каждой категории, где количество статей больше 5:**

```sql
SELECT category_id, COUNT(*)
FROM news_article
GROUP BY category_id
HAVING COUNT(*) > 5;
```

2. **Сумма просмотров статей в каждой категории, где сумма просмотров больше 1000:**

```sql
SELECT category_id, SUM(views)
FROM news_article
GROUP BY category_id
HAVING SUM(views) > 1000;
```

3. **Среднее количество просмотров статей в каждой категории, где среднее количество просмотров больше 200:**

```sql
SELECT category_id, AVG(views)
FROM news_article
GROUP BY category_id
HAVING AVG(views) > 200;
```

4. **Максимальное количество просмотров статьи в каждой категории, где максимальное количество просмотров больше 300:**

```sql
SELECT category_id, MAX(views)
FROM news_article
GROUP BY category_id
HAVING MAX(views) > 300;
```

5. **Минимальное количество просмотров статьи в каждой категории, где минимальное количество просмотров больше 100:**

```sql
SELECT category_id, MIN(views)
FROM news_article
GROUP BY category_id
HAVING MIN(views) > 100;
```

#### Django ORM

В Django ORM нет прямого эквивалента `HAVING`, но можно использовать `annotate` и `filter` для достижения аналогичного результата.

1. **Подсчет количества статей в каждой категории, где количество статей больше 5:**

```python
from django.db.models import Count

results = Article.objects.values('category').annotate(count=Count('id')).filter(count__gt=5)
for result in results:
    print(f"Category: {result['category']}, Count: {result['count']}")
```

2. **Сумма просмотров статей в каждой категории, где сумма просмотров больше 1000:**

```python
from django.db.models import Sum

results = Article.objects.values('category').annotate(total_views=Sum('views')).filter(total_views__gt=1000)
for result in results:
    print(f"Category: {result['category']}, Total Views: {result['total_views']}")
```

3. **Среднее количество просмотров статей в каждой категории, где среднее количество просмотров больше 200:**

```python
from django.db.models import Avg

results = Article.objects.values('category').annotate(avg_views=Avg('views')).filter(avg_views__gt=200)
for result in results:
    print(f"Category: {result['category']}, Average Views: {result['avg_views']}")
```

4. **Максимальное количество просмотров статьи в каждой категории, где максимальное количество просмотров больше 300:**

```python
from django.db.models import Max

results = Article.objects.values('category').annotate(max_views=Max('views')).filter(max_views__gt=300)
for result in results:
    print(f"Category: {result['category']}, Max Views: {result['max_views']}")
```

5. **Минимальное количество просмотров статьи в каждой категории, где минимальное количество просмотров больше 100:**

```python
from django.db.models import Min

results = Article.objects.values('category').annotate(min_views=Min('views')).filter(min_views__gt=100)
for result in results:
    print(f"Category: {result['category']}, Min Views: {result['min_views']}")
```

**commit: `Урок 12: рассмотрели работу агрегационных функций в SQL и в Django ORM`**