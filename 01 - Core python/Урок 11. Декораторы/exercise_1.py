# Тема: Декораторы
from distutils.command.install import value


# 1. Создайте декоратор validate, который проверяет,
# что все переданные функции аргументы являются положительными
# числами.
# Если нет, выводит сообщение об ошибке.
#
# def validate(func):
#     def wrapper(*args,**kwargs):
#         for x in list(kwargs.values()) + list(args):
#             if x <= 0:
#                 print("Ошибка: все аргументы должны быть положительными числами")
#                 break
#         else:
#             return func(*args, **kwargs)
#
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
# # Вывод: Ошибка: все аргументы должны быть положительными числами


# 2. Создайте декоратор cache, который запоминает результаты
# выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции
# с теми же аргументами.
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

