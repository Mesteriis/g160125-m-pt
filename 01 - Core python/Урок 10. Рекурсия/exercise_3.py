# Тема: Дополнительная практика на функции
from Tools.scripts.make_ctype import values


# 1. Напишите функцию `multiply_all`, которая принимает
# произвольное количество числовых аргументов с помощью `*args`
# и возвращает их произведение.
# # Пример использования:
# def multiply_all(*args):
#     result = 1
#     for arg in args:
#         result *= arg
#     return result
# print(multiply_all(1, 2, 3, 4))  # Вывод: 24


# 2. Напишите функцию `merge_dicts`, которая принимает
# произвольное количество словарей с помощью `**kwargs`
# и возвращает один объединённый словарь.
# Пример использования:
  # Вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4}def merge_dicts(**kwargs):
# Пример использования:

# def merge_dicts(**kwargs):
#     return kwargs
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# print(merge_dicts(**dict1, **dict2))

# которая создаёт функцию `flatten`, превращающую вложенный
# список в одноуровневый.
# # Пример использования:
#   # Вывод: [1, 2, 3, 4, 5, 6]
# def make_flatten(nested_list):
#     flat_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flat_list.extend(flatten(item))
#         else:
#             flat_list.append(item)
#     return flat_list
# nested_list = [1, [2, 3], [4, [5, 6]]]
# print(make_flatten(nested_list))

# 4. Напишите функцию `show_info`, которая принимает произвольное
# количество именованных и неименованных аргументов
# с помощью `*args` и `**kwargs` и выводит их.
# Пример использования:

def show_info(*args, **kwargs):
    print(f"{args}")
    print(f"{kwargs}")

args = (1, 2, 3)
kwargs = {"name": "Alice", "age": 30}
show_info(*args, **kwargs)
