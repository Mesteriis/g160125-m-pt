# Тема: Сортировка с использованием sort и sorted

# Задача 1: Сортировка списка чисел по возрастанию и убыванию
# Дан список чисел `[10, 3, 7, 1, 9, 4]`.
# 1. Отсортируйте список по возрастанию с помощью метода `sort`.
# Ожидаемый результат: [1, 3, 4, 7, 9, 10]
# 2. Отсортируйте список по убыванию с помощью функции `sorted`.
# Ожидаемый результат: [10, 9, 7, 4, 3, 1]
numbers = [10, 3, 7, 1, 9, 4]
numbers.sort()
print(numbers)
sorted_numbers = sorted(numbers, reverse = True)
print(sorted_numbers)

numbers = [10, 3, 7, 1, 9, 4]
numbers.sort()
print(numbers)  # [1, 3, 4, 7, 9, 10]
s = sorted(numbers, reverse=True)


# Задача 2: Сортировка списка строк по длине
# Дан список строк `["house", "cat", "elephant", "car", "building"]`.
# Отсортируйте список по длине строк с помощью функции `sorted`.
# Ожидаемый результат: ['cat', 'car', 'house', 'building', 'elephant']
strings = ["house", "cat", "elephant", "car", "building"]
sorted_strings = sorted(strings, key = len)
print(sorted_strings)

# Задача 3: Сортировка списка кортежей по второму элементу
# Дан список кортежей `[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]`.
# Отсортируйте список по второму элементу кортежей с помощью метода `sort`.
# Ожидаемый результат: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

strings = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_data = sorted(strings, key = lambda x: x[1])
print(sorted_data)


# Задача 4: Сортировка списка словарей по значению ключа
# Дан список словарей `[{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]`.
# Отсортируйте список по значению ключа `age` с помощью функции `sorted`.
# Ожидаемый результат: [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]

strings = [{ "name": "Alice", "age": 25 }, { "name": "Bob", "age": 20 }, { "name": "Charlie", "age": 23 }]
sorted_strings = sorted(strings, key=lambda item: ["age"])
print(sorted_strings)

# Задача 5: Сортировка списка кортежей по сумме элементов
# Дан список кортежей `[(3, 5), (1, 7), (4, 2), (6, 3)]`.
# Отсортируйте кортежи по сумме их элементов с помощью метода `sort`.
# Ожидаемый результат: [(4, 2), (3, 5), (6, 3), (1, 7)]

nummers = [(3, 5), (1, 7), (4, 2), (6, 3)]
nummers.sort(key=sum)
print(nummers)

# Тема: Cортировка с all, any, isinstance

# Задача 1: Сортировка списка строк с проверкой типов
# Дан список `["tree", 3, "mountain", 1, "river", 2]`.
# Отсортируйте только строки в списке по алфавиту с помощью функции `sorted`,
# Ожидаемый результат: ['mountain', 'river', 'tree']

my_list = ["tree", 3, "mountain", 1, "river", 2]
sorted_list = sorted(list(filter(lambda x: isinstance(x, str), my_list)))
print(sorted_list)

# Задача 2: Сортировка списка словарей по значению ключа с проверкой типов
# Дан список словарей
# [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }].
# Отсортируйте словари по значению ключа `price`, предварительно проверив, что значение является числом,
# с помощью функции `isinstance`.
# Ожидаемый результат: [{'title': 'Book C', 'price': 9.99}, {'title': 'Book A', 'price': 15.99}]

my_dict = [{ "title": "Book A", "price": 15.99 }, { "title": "Book B", "price": "free" }, { "title": "Book C", "price": 9.99 }]
sort_int = filter(lambda x: isinstance(x["price"], float), my_dict)
sort_by_price = sorted(sort_int, key = lambda item: ["price"])
print(sort_by_price)

# Задача 3: Сортировка списка кортежей по количеству слов с использованием all
# Дан список кортежей `[(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]`.
# Отсортируйте кортежи по количеству слов во втором элементе, предварительно проверив,
# что все строки содержат только алфавитные символы, с помощью функции `all`.
# Ожидаемый результат: [(1, 'low'), (3, 'high'), (4, 'medium'), (6, 'very high')]

my_list = [(3, "high"), (1, "low"), (4, "medium"), (6, "very high")]
my_list = list(filter(lambda x: all(char.isalpha() or char.isspace() for char in x[1]), my_list))
my_list.sort(key=lambda x: len(x[1].split()))
print(my_list)

# Задача 4: Сортировка списка словарей по длине значений с использованием any
# Дан список словарей
# [{ "country": "USA", "capital": "Washington" }, { "country": "UK", "capital": "London" },
#  { "country": "Australia", "capital": "Canberra" }].
# Отсортируйте словари по длине значений ключа `capital`, предварительно проверив,
# что хотя бы одна длина значения ключа `capital` больше 6, с помощью функции `any`.
# Ожидаемый результат: [{'country': 'UK', 'capital': 'London'}, {'country': 'Australia', 'capital': 'Canberra'}, {'country': 'USA', 'capital': 'Washington'}]

country = [
    {"country": "USA", "capital": "Washington"},
    {"country": "UK", "capital": "London"},
    {"country": "Australia", "capital": "Canberra"}
]

if any(len(x["capital"]) > 6 for x in country):
    country.sort(key=lambda x: len(x["capital"]))
    print(country)
country = list(filter(lambda x: any(len(x["capital"]) > 6 for x in country), country))
country.sort(key=lambda x: len(x["capital"]))
print(country)


# Тема: Дополнительная практика

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineering", 2, "artificial", 3.14, "intelligence"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['artificial', 'engineering', 'intelligence']

words = ["engineering", 2, "artificial", 3.14, "intelligence"]
vowels = "aeiou"

words = list(filter(lambda x: isinstance(x, str), words))
print(words)  # ['engineering', 'artificial', 'intelligence']

word = 'engineering'
my_list = []
for el in word:
    if el in vowels:
        my_list.append(1)
print(sum(my_list))

print(sum(1 for char in word if char in vowels))  # 5
words = sorted(words, key=lambda x: sum(1 for char in x if char in vowels))

sorted_words = sorted(filter(lambda x: isinstance(x, str), words), key=lambda x: sum(1 for char in x if char in vowels))
print(sorted_words)  # ['artificial', 'engineering', 'intelligence']

# Задача 2: Сортировка списка списков по минимальному значению элемента с использованием all
# Дан список списков `[[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]`.
# Отсортируйте списки по их минимальному значению, предварительно проверив,
# что все элементы списков являются положительными, с помощью функции `all`.
# Ожидаемый результат: [[3, 5, 1], [4, 4, 4]]

matrix = [
    [3, 5, 1],
    [0, -2, 3],
    [4, 4, 4],
    [-1, 3, 5]
]

matrix = list(filter(lambda x: all(num > 0 for num in x), matrix))
matrix.sort(key=lambda x: min(x))
print(matrix)  # [[3, 5, 1], [4, 4, 4]]


# Задача 3: Сортировка списка словарей по статусу пользователя и преобразование с помощью map
# **Задание:**
# Дан список словарей, представляющих пользователей веб-приложения
# [{ "username": "alice", "status": "active" }, { "username": "bob", "status": "inactive" },
#  { "username": "charlie", "status": "active" }]`.
# Отсортируйте пользователей по статусу, а затем используйте функцию `map`,
# чтобы преобразовать статусы в верхний регистр.
# Ожидаемый результат:
# [{'username': 'alice', 'status': 'ACTIVE'},
# {'username': 'charlie', 'status': 'ACTIVE'},
# {'username': 'bob', 'status': 'INACTIVE'}]

[{'username': 'alice', 'status': 'ACTIVE'},
{'username': 'charlie', 'status': 'ACTIVE'},
{'username': 'bob', 'status': 'INACTIVE'}]

users = [
    {"username": "alice", "status": "active"},
    {"username": "bob", "status": "inactive"},
    {"username": "charlie", "status": "active"}
]

users.sort(key=lambda x: x["status"])
users = list(map(lambda x: {**x, "status": x["status"].upper()}, users))
print(users)

users_ = []
for user in users:
    users_.append(
        {
            **user,
            "status": user["status"].upper()
        }
    )
    user_ = user
    user_["status"] = user_["status"].upper()
    users_.append(user_)

# Задача 4: Сортировка списка URL по длине и фильтрация с помощью filter
# Дан список URL-адресов
# ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]`.
# Отсортируйте URL по длине, а затем используйте функцию `filter`,
# чтобы отобрать только те URL, которые содержат подстроку "example".
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']

urls = [
    "https://example.com",
    "https://longexample.com/page",
    "http://short.io",
    "https://medium.com/article"
]
urls = sorted(urls, key=len)
urls = list(filter(lambda x: "example" in x, urls))
print(urls)

# Задача 5: Сортировка списка запросов по времени выполнения и объединение с URL с помощью zip
# Дан список времени выполнения запросов в миллисекундах `[120, 30, 150, 90]` и список соответствующих URL
# `["/home", "/login", "/profile", "/settings"]`. Отсортируйте время выполнения по возрастанию,
# а затем используйте функцию `zip`, чтобы объединить отсортированные времена выполнения с URL, и выведите результат.
# Ожидаемый результат: [(30, '/home'), (90, '/login'), (120, '/profile'), (150, '/settings')]

times = [120, 30, 150, 90]
urls = ["/home", "/login", "/profile", "/settings"]
urls =list(sorted(zip(times, urls), key=lambda x: x[0]))
print(urls)

# Задача 6: Сортировка списка API ответов по статус-коду и преобразование с помощью map и zip
# Дан список словарей, представляющих ответы от API
# [{ "url": "/api/user", "status": 200 },
#   { "url": "/api/admin", "status": 403 },
#   { "url": "/api/data", "status": 404 }]`.
# Отсортируйте ответы по статус-коду, а затем используйте функцию `zip` для объединения отсортированных ответов
# с их порядковыми номерами, и функцию `map` для преобразования в кортежи вида (номер, url, статус).
# Ожидаемый результат: [(0, '/api/user', 200), (1, '/api/admin', 403), (2, '/api/data', 404)]

responses = [
    {"url": "/api/user", "status": 200},
    {"url": "/api/admin", "status": 403},
    {"url": "/api/data", "status": 404}
]
responses = sorted(responses, key=lambda x: x["status"])
responses = list(map(lambda x: (responses.index(x), x["url"], x["status"]), responses))
responses = [
    response
    for i, response in enumerate(responses)
]
print(responses)
