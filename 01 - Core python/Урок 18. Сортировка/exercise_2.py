# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']


# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}]
books = [
    {"title": "Book A", "price": 15.99},
    {"title": "Book B", "price": "free"},
    {"title": "Book C", "price": 9.99}
]
filtered_books = [book for book in books if isinstance(book["price"], (int, float))]
sorted_books = sorted(filtered_books, key=lambda x: x["price"])

print(sorted_books)

# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]
tuples = [(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]
filtered_tuples = [x for x in tuples if all(word.isalpha() for word in t[1].split())]
sorted_tuples = sorted(filtered_tuples, key=lambda x: len(x[1].split()))

print(sorted_tuples)


# Задача 4: Сортировка списка словарей по длине значений с использованием any
# Дан список словарей
# [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
#  { "country": "Australia", "capital": "Canberra" }].
# Отсортируйте словари по длине значений ключа `capital`, предварительно проверив,
# что хотя бы одна длина значения ключа `capital` больше 6, с помощью функции `any`.
# Ожидаемый результат: [{'country': 'UK', 'capital': 'London'}, {'country': 'Australia', 'capital': 'Canberra'}, {'country': 'USA', 'capital': 'Washington'}]
countries = [
    {"country": "USA", "capital": "Washington"},
    {"country": "UK", "capital": "London"},
    {"country": "Australia", "capital": "Canberra"}
]
if any(len(entry["capital"]) > 6 for entry in countries):
    sorted_countries = sorted(countries, key=lambda x: len(x["capital"]))
    print(sorted_countries)
else:
    print("No capital names longer than 6 characters.")


