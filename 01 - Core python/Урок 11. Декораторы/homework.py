# Тема: Декораторы


# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.

# def validate(func):
#     def wrapper(*args):
#         for num in args:
#             if num <= 0:
#                 print("Error value!")
#                 return None
#             return func(*args)
#     return wrapper
#
#
# @validate
# def add(a, b):
#     return a + b
#
# print(add(5, 3))
# # Вывод: 8
# #
# print(add(-1, 3))
# Вывод: Ошибка: все аргументы должны быть положительными числами


# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.
# cache_results = {}
# def cache(func):
#     def wrapper(*args):
#         global cache_results
#
#         if args in cache_results:
#             return cache_results[args]
#
#         result = func(*args)
#         cache_results[args] =result
#         return result
#
#     return wrapper
#
# @cache
# def fibonacci(n):
#     if n in (0, 1):
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(10))
# # # Вывод: 55
# #
# print(fibonacci(10))
# # # Вывод: 55 (использует кеш)


# Дополнительная практика


# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.

# def requires_auth(func):
#     def wrapper(*args, **kwargs):
#         if authenticated:
#             return func(*args, **kwargs)
#         else:
#             print("Access denied!")
#             return None
#     return wrapper
#
# authenticated = False
#
# @requires_auth
# def secret_function():
#     print("Секретная информация")
#
# secret_function()
# # Вывод: Доступ запрещен: пользователь не аутентифицирован
# #
# authenticated = True
# secret_function()
# Вывод: Секретная информация


# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
# def call_counter(func):
#     counter = 0
#     def wrapper(*args, **kwargs):
#         nonlocal counter
#         counter += 1
#         print(f"Function {func.__name__} was called: {counter} times")
#         return func(*args, **kwargs)
#     return wrapper
#
# @call_counter
# def greet(name):
#     print(f"Привет, {name}!")
#
# greet("Алиса")
# # # Вывод:
# # # Функция greet вызвана 1 раз(а)
# # # Привет, Алиса!
# #
# greet("Боб")
# # # Вывод:
# # # Функция greet вызвана 2 раз(а)
# # # Привет, Боб!


# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
# def to_upper(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result,str):
#             return result.upper()
#
#         return result
#
#     return wrapper
#
# @to_upper
# def get_greeting(name):
#     return f"Привет, {name}"
#
# print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА


# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
# def limit_calls(max_calls):
#
#     def decorator(func):
#         counter = 0
#
#         def wrapper(*args, **kwargs):
#             nonlocal counter
#             if counter >= max_calls:
#                 print(f"Error! Func {func.__name__} was called more then {max_calls} time")
#                 return
#
#             counter += 1
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
# @limit_calls(3)
# def say_hello(name):
#     print(f"Привет, {name}!")
#
# say_hello("Алиса")
# # # Вывод: Привет, Алиса!
# say_hello("Боб")
# # # Вывод: Привет, Боб!
# say_hello("Чарли")
# # # Вывод: Привет, Чарли!
# say_hello("Дейв")
# # # Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз
