# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **

# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.
# numbers = [1,2,3,5]
# def sum_all(*args):
#     return sum(args)
# print(sum_all(*numbers))

# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.
# def combine_lists(*args):
#     combined_list = []
#     for lst in args:
#         combined_list.extend(lst)
#     return combined_list
#
# ll = (
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# )
#
# result = combine_lists(*ll)
# print(result)


# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.
# def print_details(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#
# person = {"name": "Karl", "age": 30}
#
# print_details(**person)

# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.
# def filter_numbers(*args):
#     return [num for num in args if num > 10]
#
# result = filter_numbers(5, 15, 20, 3, 12, 9)
# print(result)
#
#
# def filter_numbers(*args):
#     numbers = []
#     for num in args:
#         if num > 10:
#             numbers.append(num)
#     return numbers
# print(filter_numbers(10,20,30,5,7))
# numbers_ = (10,20,30,5,7,5)
# print(filter_numbers(*numbers_))