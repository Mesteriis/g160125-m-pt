# Тема: Дополнительная практика
from urllib.parse import uses_relative

from pygments.lexer import words

# Задача 1: Сортировка списка строк по количеству гласных с использованием isinstance
# Дан список `["engineering", 2, "artificial", 3.14, "intelligence"]`.
# Отсортируйте только строки в списке по количеству гласных с помощью функции `sorted`,
# предварительно проверив тип данных с помощью функции `isinstance`.
# Ожидаемый результат: ['artificial', 'engineering', 'intelligence']

# words = ["engineering", 2, "artificial", 3.14, "intelligence"]
# vowels = "aeiou"
#
# words = list(filter(lambda x: isinstance(x, str), words))
# print(words)  # ['engineering', 'artificial', 'intelligence']
#
# word = 'engineering'
# my_list = []
# for el in word:
#     if el in vowels:
#         my_list.append(1)
# print(sum(my_list))
#
# print(sum(1 for char in word if char in vowels))  # 5
# words = sorted(words, key=lambda x: sum(1 for char in x if char in vowels))
#
# sorted_words = sorted(filter(lambda x: isinstance(x, str), words), key=lambda x: sum(1 for char in x if char in vowels))
# print(sorted_words)  # ['artificial', 'engineering', 'intelligence']

# Задача 2: Сортировка списка списков по минимальному значению элемента с использованием all
# Дан список списков `[[3, 5, 1], [0, -2, 3], [4, 4, 4], [-1, 3, 5]]`.
# Отсортируйте списки по их минимальному значению, предварительно проверив,
# что все элементы списков являются положительными, с помощью функции `all`.
# Ожидаемый результат: [[3, 5, 1], [4, 4, 4]]

# matrix = [
#     [3, 5, 1],
#     [0, -2, 3],
#     [4, 4, 4],
#     [-1, 3, 5]
# ]
#
# matrix = list(filter(lambda x: all(num > 0 for num in x), matrix))
# matrix.sort(key=lambda x: min(x))
# print(matrix)  # [[3, 5, 1], [4, 4, 4]]
#

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

# users = [
#     {"username": "alice", "status": "active"},
#     {"username": "bob", "status": "inactive"},
#     {"username": "charlie", "status": "active"}
# ]
#
# users.sort(key=lambda x: x["status"])
# users = list(map(lambda x: {**x, "status": x["status"].upper()}, users))
# print(users)
#
# users_ = []
# for user in users:
#     users_.append(
#         {
#             **user,
#             "status": user["status"].upper()
#         }
#     )
#     user_ = user
#     user_["status"] = user_["status"].upper()
#     users_.append(user_)



# Задача 4: Сортировка списка URL по длине и фильтрация с помощью filter
# Дан список URL-адресов
# ["https://example.com", "https://longexample.com/page", "http://short.io", "https://medium.com/article"]`.
# Отсортируйте URL по длине, а затем используйте функцию `filter`,
# чтобы отобрать только те URL, которые содержат подстроку "example".
# Ожидаемый результат: ['https://example.com', 'https://longexample.com/page']

# urls = [
#     "https://example.com",
#     "https://longexample.com/page",
#     "http://short.io",
#     "https://medium.com/article"
# ]
# urls = sorted(urls, key=len)
# urls = list(filter(lambda x: "example" in x, urls))
# print(urls)

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