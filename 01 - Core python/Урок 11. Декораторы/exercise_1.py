# Тема: Декораторы


# 1. Создайте декоратор validate, который проверяет, что все переданные функции аргументы являются положительными числами.
# Если нет, выводит сообщение об ошибке.
#
# @validate
# def add(a, b):
#     return a + b
#
# print(add(5, 3))
# Вывод: 8
#
# print(add(-1, 3))
# Вывод: Ошибка: все аргументы должны быть положительными числами


# 2. Создайте декоратор cache, который запоминает результаты выполнения функции для заданных аргументов и возвращает
# этот результат при повторном вызове декорируемой функции с теми же аргументами.
cache_store = {}
def cache(func):
    global cache_store
    if func.__name__ not in cache_store:
        cache_store[func.__name__] = {}

    def wrapper(*args, **kwargs):
        global cache_store

        key = args + tuple(kwargs.items())

        if key not in cache_store[func.__name__]:
            cache_store[func.__name__][key] = func(*args, **kwargs)

        return cache_store[func.__name__][key]

    return wrapper

@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
# # Вывод: 55
#
print(fibonacci(10))
# Вывод: 55 (использует кеш)

