# Тема: Сортировка с использованием sort и sorted

# Задача 1: Сортировка списка чисел по возрастанию и убыванию
# Дан список чисел `[10, 3, 7, 1, 9, 4]`.
# 1. Отсортируйте список по возрастанию с помощью метода `sort`.
# Ожидаемый результат: [1, 3, 4, 7, 9, 10]
# 2. Отсортируйте список по убыванию с помощью функции `sorted`.
# Ожидаемый результат: [10, 9, 7, 4, 3, 1]

# numbers = [10, 3, 7, 1, 9, 4]
# numbers.sort()
# sorted_nums = sorted(numbers, reverse=True)
# print(numbers, sorted_nums)

# Задача 2: Сортировка списка строк по длине
# Дан список строк `["house", "cat", "elephant", "car", "building"]`.
# Отсортируйте список по длине строк с помощью функции `sorted`.
# Ожидаемый результат: ['cat', 'car', 'house', 'building', 'elephant']

# words = ["house", "cat", "elephant", "car", "building"]
# print(sorted(words, key=len))

# Задача 3: Сортировка списка кортежей по второму элементу
# Дан список кортежей `[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]`.
# Отсортируйте список по второму элементу кортежей с помощью метода `sort`.
# Ожидаемый результат: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# numbers = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
#
# ordered_numbers = sorted(numbers, key = lambda x: x[1])
# print(ordered_numbers)

# Задача 4: Сортировка списка словарей по значению ключа
# Дан список словарей `[{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]`.
# Отсортируйте список по значению ключа `age` с помощью функции `sorted`.
# Ожидаемый результат: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]

# users = [{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]
# sort_by_age = sorted(users, key= lambda item: item["age"])
# print(sort_by_age)

# Задача 5: Сортировка списка кортежей по сумме элементов
# Дан список кортежей `[(3, 5), (1, 7), (4, 2), (6, 3)]`.
# Отсортируйте кортежи по сумме их элементов с помощью метода `sort`.
# Ожидаемый результат: [(4, 2), (3, 5), (6, 3), (1, 7)]

# numbers = [(3, 5), (1, 7), (4, 2), (6, 3)]
# ordered = sorted(numbers, key=sum)
# print(ordered)

# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']

# my_list = ["tree", 3, "mountain", 1, "river", 2]
# words = list(filter(lambda x: isinstance(x, str), my_list))
# sorted_words = sorted(words)
# print(sorted_words)
# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}]
# books = [
#     { "title": "Book A", "price": 15.99 },
#     { "title": "Book B", "price": "free" },
#     { "title": "Book C", "price": 9.99 }
# ]
# sort_by_int = filter(lambda x: isinstance(x["price"], float), books)
# books_prices = sorted(sort_by_int, key=lambda x: x["price"])
# print(books_prices)
# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]
# my_list = [(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]
#
# filtered_list = list(filter(lambda x: all(sym.isalpha() or sym.isspace() for sym in x[1]), my_list))
#
# filtered_list.sort(key=lambda x:len(x[1]))
# print(filtered_list)

# Задача 4: Сортировка списка словарей по длине значений с использованием any
# Дан список словарей
# [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
#  { "country": "Australia", "capital": "Canberra" }].
# Отсортируйте словари по длине значений ключа `capital`, предварительно проверив,
# что хотя бы одна длина значения ключа `capital` больше 6, с помощью функции `any`.
# Ожидаемый результат: [{'country': 'UK', 'capital': 'London'}, {'country': 'Australia', 'capital': 'Canberra'}, {'country': 'USA', 'capital': 'Washington'}]

# countries = [
#     { "country": "USA", "capital": "Washington" },
#     { "country": "UK", "capital": "London" },
#     { "country": "Australia", "capital": "Canberra" }
# ]

# if any(len(country["capital"]) > 6 for country in countries):
#     countries.sort(key=lambda x: len(x["capital"]))
#     print(countries)

# Тема: Дополнительная практика

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineering", 2, "artificial", 3.14, "intelligence"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['artificial', 'engineering', 'intelligence']

# my_list = ["engineering", 2, "artificial", 3.14, "intelligence"]
#
# vowels = ["aeiou"]
# words_only = list(filter(lambda x: isinstance(x, str), my_list))
# # sort_by_len = sorted(words_only, key=lambda x: len(x))
# len_by_vowels = sorted(words_only, key=lambda x: sum(1 for char in x if char in vowels))
# print(len_by_vowels)

# Задача 2: Сортировка списка списков по минимальному значению элемента с использованием all
# Дан список списков `[[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]`.
# Отсортируйте списки по их минимальному значению, предварительно проверив,
# что все элементы списков являются положительными, с помощью функции `all`.
# Ожидаемый результат: [[3, 5, 1], [4, 4, 4]]

# my_lists = [[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]
# filt_lists = list(filter(lambda sublist: all(num > 0 for num in sublist), my_lists))
# sorted_by_min = sorted(filt_lists, key=lambda x: min(x))
# print(sorted_by_min)

# Задача 3: Сортировка списка словарей по статусу пользователя и преобразование с помощью map
# **Задание:**
# Дан список словарей, представляющих пользователей веб-приложения
# [{ "username": "alice", "status": "active" }, { "username": "bob", "status": "inactive" },
#  { "username": "charlie", "status": "active" }]`.
# Отсортируйте пользователей по статусу, а затем используйте функцию `map`,
# чтобы преобразовать статусы в верхний регистр.
# users = [
#     { "username": "alice", "status": "active" },
#     { "username": "bob", "status": "inactive" },
#     { "username": "charlie", "status": "active" }
# ]
# status_to_upper = list(map(lambda x: {**x, "status": x["status"].upper()}, users))
# sort_by_status = sorted(status_to_upper, key=lambda x: x["status"])

# print(sort_by_status)
# Ожидаемый результат:
# [{'username': 'alice', 'status': 'ACTIVE'},
# {'username': 'charlie', 'status': 'ACTIVE'},
# {'username': 'bob', 'status': 'INACTIVE'}]


# Задача 4: Сортировка списка URL по длине и фильтрация с помощью filter
# Дан список URL-адресов
# ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]`.
# Отсортируйте URL по длине, а затем используйте функцию `filter`,
# чтобы отобрать только те URL, которые содержат подстроку "example".
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']

# url_list = ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]
# keyword = "example"
# url_list.sort( key=len)
#
# only_with_example = list(filter(lambda x: keyword in x, url_list))
# print(only_with_example)

# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']

# Задача 5: Сортировка списка запросов по времени выполнения и объединение с URL с помощью zip
# Дан список времени выполнения запросов в миллисекундах `[120, 30, 150, 90]` и список соответствующих URL
# `["/home", "/login", "/profile", "/settings"]`. Отсортируйте время выполнения по возрастанию,
# а затем используйте функцию `zip`, чтобы объединить отсортированные времена выполнения с URL, и выведите результат.
# Ожидаемый результат: [(30, '/home'), (90, '/login'), (120, '/profile'), (150, '/settings')]

# url_list = ["/home", "/login", "/profile", "/settings"]
# timing = [120, 30, 150, 90]
# timing.sort()
# combined = list(zip(timing, url_list))
# print(combined)

# Задача 6: Сортировка списка API ответов по статус-коду и преобразование с помощью map и zip
# Дан список словарей, представляющих ответы от API
# [{ "url": "/api/user", "status": 200 },
#   { "url": "/api/admin", "status": 403 },
#   { "url": "/api/data", "status": 404 }]`.
# Отсортируйте ответы по статус-коду, а затем используйте функцию `zip` для объединения отсортированных ответов
# с их порядковыми номерами, и функцию `map` для преобразования в кортежи вида (номер, url, статус).
api_answers = [
    { "url": "/api/user", "status": 200 },
    { "url": "/api/admin", "status": 403 },
    { "url": "/api/data", "status": 404 }
]
api_answers = sorted(api_answers, key=lambda x: x["status"])
api_answers = list(map(lambda x: f"{x[0]}, {x[1]}", enumerate(api_answers, 0)))
print(api_answers)
# Ожидаемый результат: [(0, '/api/user', 200), (1, '/api/admin', 403), (2, '/api/data', 404)]