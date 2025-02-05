# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **
from itertools import count


# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.

# def sum_all(*args):
#     return sum(args)
# print(sum_all(1, 2))

# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.

# list = ([1,2,3], [4,5,6])
# def combine_lists(*args):
#
#     comb_list = []
#     for list_ in args:
#         comb_list.extend(list_)
#     return comb_list
#
# print(combine_lists(*list))


# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.

# def print_details(name, age):
#     print(name, age)
#
# pers_info = {"name": "John", "age": 40}
#
# print(print_details(**pers_info))

# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.

# def filter_numbers(*args):
#     numbers = []
#     for num in args:
#         if num > 10:
#             numbers.append(num)
#     return numbers
#
# print(filter_numbers(1,10,20, 40, 11))


# Тема: Глобальные и локальные переменные. Вложенные функции и замыкания.

# 1. Напишите функцию increment_global, которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.

# counter = 0
# def increment_global():
#     global counter
#     counter +=1
#
# increment_global()
# print(counter)
# increment_global()
# print(counter)
# increment_global()
# print(counter)

# 2. Напишите функцию outer, которая содержит внутреннюю функцию inner. Внутренняя функция должна увеличивать
# значение переменной count, объявленной во внешней функции, на 1 каждый раз при её вызове.

# def outer():
#     counter = 0
#     def inner():
#         nonlocal counter
#         counter +=1
#         return counter
#     return inner

# counter = outer()
# print(counter())  # Вывод: 1
# print(counter())  # Вывод: 2

# 3. Напишите функцию make_multiplier, которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.

# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15

# def make_multiplier(factor):
#     def multiplier(num):
#         return num * factor
#     return multiplier
#
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15


# 4. Напишите функцию make_prefixer, которая принимает строку prefix и возвращает внутреннюю функцию prefixer.
# Внутренняя функция должна добавлять prefix к любому переданному ей аргументу.

# def make_prefixer(prefix):
#     def prefixer_(num):
#         return f"{prefix}{num}"
#     return prefixer_
#
# add_hello = make_prefixer("Hello, ")
# print(add_hello("Alice"))  # Вывод: Hello, Alice
# print(add_hello("Bob"))    # Вывод: Hello, Bob

# Тема: Дополнительная практика

# 1. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.

# def create_user(username, email, **kwargs):
#     print(f"Name: {username}")
#     print(f"Email: {email}")
#     print(f"Other:", kwargs)

# print(create_user("Ivan", "p0@me.com", married =True))

# 2. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.

# def make_replacer(old, new):
#     def replacer(text):
#         return text.replace (old.lower(),  new.lower()).replace(old.upper(),    new.upper())
#     return replacer
#
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple


# 3. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.

# def make_suffixer(suffix):
#     def suffixer(text):
#         return f"{text}{suffix}"
#
#     return suffixer
#
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!

# 4. Напишите функцию make_case_changer, которая принимает аргумент case (значения могут быть "upper" или "lower").
# Внутри этой функции создайте и верните функцию case_changer, которая изменяет регистр строки в зависимости от
# переданного аргумента (если передан аргумент с заглавными буквами, то делаете их строчными, если со строчными,
# то делает их заглавными).

# def make_case_changer(case):
#     def case_changer(text):
#         return text.upper() if case == "upper" else text.lower()
#     return case_changer
#
# to_upper = make_case_changer("upper")
# print(to_upper("hello"))  # Вывод: HELLO
# to_lower = make_case_changer("lower")
# print(to_lower("WORLD"))  # Вывод: world


# 5. Напишите функцию make_trimmer, которая принимает аргумент length. Внутри этой функции создайте и
# верните функцию trimmer, которая обрезает строку до заданной длины.

# def make_trimmer(length):
#     def trimmer(text):
#         if len(text) > length:
#             return text[:length]
#     return trimmer
#
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))  # Вывод: Hel
# print(trim_to_3("World"))  # Вывод: Wor