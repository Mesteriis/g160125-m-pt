### Тема: Рекурсия

# 1. Напишите функцию `sum_list(lst)`, которая возвращает сумму всех элементов списка `lst` с помощью рекурсии.
# Пример использования:

# def sum_list(lst):
#     sum_ = 0
#     for num in lst:
#         sum_ += num
#     return sum_
# print(sum_list([1, 2, 3, 4, 5]))  # Вывод: 15

# 2. Напишите функцию `is_palindrome(s)`, которая проверяет, является ли строка `s` палиндромом
# (порядок букв одинаковый при чтении слева направо и справа налево) с помощью рекурсии.
# Пример использования:
# def is_palindrome(s):
#     if len(s) <= 0:
#         return True
#     if s[0] != s[-1]:
#         return is_palindrome(s[1:-1])
#
# print(is_palindrome("radar"))  # Вывод: True
# print(is_palindrome("hello"))  # Вывод: False


# 3. Напишите функцию `find_max(lst)`, которая возвращает максимальный элемент в списке `lst` с помощью рекурсии.
# Пример использования:

# def find_max(lst):
#         if len(lst) == 1:
#             return lst[0]
#         else:
#             max_rest = find_max(lst[1:])
#             return lst[0] if lst[0] > max_rest else max_rest

# print(find_max([1, 5, 3, 9, 2]))  # Вывод: 9


# Тема: Дополнительная практика на рекурсию

# 1. Напишите функцию `sum_of_digits(n)`, которая возвращает сумму цифр числа `n` с помощью рекурсии.
# Пример использования:
# def sum_of_digits(n):
#     n = str(n)
#     if not n:
#         return 0
#     return int(n[0]) + sum_of_digits(int(n[1:])) if len(n) > 1 else int(n[0])
#
# print(sum_of_digits(12345))  # Вывод: 15


# 2. Напишите функцию `reverse_string(s)`, которая возвращает строку `s` в обратном порядке с помощью рекурсии.
# Пример использования:
# def reverse_string(s):
#     return s[::-1]
#
# print(reverse_string("hello"))  # Вывод: "olleh"

# 3. Напишите функцию `list_length(lst)`, которая возвращает длину списка `lst` с помощью рекурсии.
# Пример использования:
# def list_length(lst):
#     return len(lst)
#
# print(list_length([1, 2, 3, 4, 5]))  # Вывод: 5


# Тема: Дополнительная практика на функции

# 1. Напишите функцию `multiply_all`, которая принимает произвольное количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# Пример использования:
# def multiply_all(*args):
#     x = 1
#     for y in args:
#         x *= y
#     return x
#
# print(multiply_all(1, 2, 3, 4))  # Вывод: 24


# 2. Напишите функцию `merge_dicts`, которая принимает произвольное количество словарей с помощью `**kwargs`
# и возвращает один объединённый словарь.
# Пример использования:

# def merge_dicts(**kwargs):
#     return kwargs
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# print(merge_dicts(**dict1, **dict2))  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 3. Напишите функцию `make_flatten`, которая создаёт функцию `flatten`, превращающую вложенный список в одноуровневый.
# Пример использования:
# def make_flatten():
#     def flatten(list_):
#         flat_list = []
#         for item in list_:
#             if isinstance(item, list):
#                 flat_list.extend(flatten(item))
#             else:
#                 flat_list.append(item)
#         return flat_list
#     return flatten
#
# flatten = make_flatten()
# print(flatten([1, [2, [3, 4], 5], 6]))  # Вывод: [1, 2, 3, 4, 5, 6]


# 4. Напишите рекурсивную функцию `find_min`, которая возвращает минимальный элемент в списке `lst`.
# Пример использования:
# def find_min(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return min(lst[0], find_min(lst[1:]))
#
# print(find_min([4, 2, 8, 1, 5]))  # Вывод: 1


# 5. Напишите функцию `show_info`, которая принимает произвольное количество именованных и неименованных аргументов
# с помощью `*args` и `**kwargs` и выводит их.
# Пример использования:
# def show_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# args = (1, 2, 3)
# kwargs = {"name": "Alice", "age": 30}
# show_info(*args, **kwargs)

# Вывод:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
