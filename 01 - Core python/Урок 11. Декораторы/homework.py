# Тема: Декораторы
#
#
# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.
# def validate(func):
#     def wrapper(*args,**kwargs):
#         for x in list(args) + list(kwargs.values()):
#             if x <= 0 :
#                 print(f"Ошибка: все аргументы должны быть положительными числами")
#                 break
#             else:
#                 return func(*args,**kwargs)
#     return wrapper
# @validate
# def add(a, b):
#     return a + b
#
# print(add(5, 3))
# # Вывод: 8
# #
# print(add(-1, 3))
# # Вывод: Ошибка: все аргументы должны быть положительными числами


# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.
# cache_list = {}
# def cache(func):
#     def wrapper(*args,**kwargs):
#         global cache_list
#         key = (args, frozenset(kwargs.items()))
#         if key in cache_list:
#             return cache_list[key]
#         result = func(*args,**kwargs)
#         cache_list[key] = result
#         return result
#     return wrapper
#
#
# @cache
# def fibonacci(n):
#     if n in (0, 1):
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(10))
# # # Вывод: 55
# #
# print(fibonacci(10))
# # # Вывод: 55 (использует кеш)



# Дополнительная практика


# 1. Создайте декоратор requires_auth, который проверяет
# наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.
#
# authenticated = True
# def requires_auth(func):
#     def wrapper(*args, **kwargs):
#         global authenticated
#         if authenticated:
#             return func(*args,**kwargs)
#         else:
#             print("Доступ запрещен: пользователь не аутентифицирован")
#     return wrapper
# @requires_auth
# def secret_function():
#     print("Секретная информация")
#
# secret_function()
# # Вывод: Доступ запрещен: пользователь не аутентифицирован
# authenticated = False
# secret_function()


# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
## func_name = {}
# def call_counter(func):
#     count = 0
#     global func_name
#     if func.__name__ not in func_name:
#         func_name[func.__name__] = 0
#     def wrapper(*args, **kwargs):
#         func_name[func.__name__] += 1
#         print(f"Функция {func.__name__} вызвана {func_name[func.__name__]} раз(а)")
#         return func(*args, **kwargs)
#
#     return wrapper
# @call_counter
# def greet(name):
#     print(f"Привет, {name}!")
#
# greet("Алиса")
# # Вывод:
# # Функция greet вызвана 1 раз(а)
# # Привет, Алиса!
#
# greet("Боб")
# # Вывод:
# # Функция greet вызвана 2 раз(а)
# # Привет, Боб!
# 1. Создайте декоратор to_upper, который преобразует
# строковый результат функции в верхний регистр.
# def to_upper(func):
# #     def wrapper(*args,**kwargs):
# #         return func(*args,**kwargs).upper()
# #     return wrapper
# @to_upper
# def get_greeting(name):
#     return f"Привет, {name}"
#
# print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА


# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
#
# counts = {}
# def limit_calls(n):
#     def decorator(func):
#         global counts
#         if func.__name__ not in counts:
#             counts[func.__name__] = {
#                 'counter': 0,
#                 'limit': n
#             }
#         def wrapper(*args, **kwargs):
#             if counts[func.__name__]['counter'] < counts[func.__name__]['limit']:
#                 counts[func.__name__]['counter'] += 1
#                 return func(*args, **kwargs)
#             else:
#                 print(f"Ошибка: функция {func.__name__} может быть вызвана не более {n} раз")
#         return wrapper
#     return decorator
# @limit_calls(3)
# def say_hello(name):
#     print(f"Привет, {name}!")
# #
# say_hello("Алиса")
# # # Вывод: Привет, Алиса!
# say_hello("Боб")
# # # Вывод: Привет, Боб!
# say_hello("Чарли")
# # # Вывод: Привет, Чарли!
# say_hello("Дейв")
# # # Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз