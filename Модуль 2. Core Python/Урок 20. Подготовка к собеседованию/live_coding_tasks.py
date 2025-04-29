# Выберите задачи для лайвкодинга. Ранее все эти задачи давались для решения в сессионных залах.
# Можно давать свои задачи наподобие тех, что студенты решали во время уроков.

# Задача 1: Напишите программу с помощью генераторов списков,
# которая находит все числа от 1 до 1000, которые делятся на 7.

# numbers_divisible_by_7 = [num for num in range(1, 1001) if num % 7 == 0]
# print(numbers_divisible_by_7)


# Задача 2: Напишите программу с помощь генераторов списков,
# которая найдите все числа от 1 до 1000, в которых есть цифра 3.

# numbers_with_3 = [num for num in range(1, 1001) if '3' in str(num)]
# print(numbers_with_3)


# Задача 3: Напишите программу с помощь генераторов списков,
# которая посчитает количество пробелов в строке
# some_string = 'the slow solid squid swam sumptuously through the slimy swamp'.

# some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
#
# count_spaces = sum(1 for char in some_string if char == ' ')
#
# print("Количество пробелов в строке:", count_spaces)


# Задача 4: Напишите программу с помощь генераторов списков,
# которая создаст список всех гласных букв в строке
# some_string = 'the quick brown fox jumps over the lazy dog'.

# some_string = 'the quick brown fox jumps over the lazy dog'
# vowels = [char for char in some_string if char in 'aeiouAEIOU']
# print(vowels)


# Задача 5: Сумма элементов в каждом ряду матрицы
# С помощью генераторов списков создайте матрицу 3x3 из чисел от 20 до 28
# Ожидаемая матрица:
# [20, 21, 22]
# [23, 24, 25]
# [26, 27, 28]
#
# Напишите код для вычисления суммы элементов в каждом ряду (в каждом вложенном списке).
# Выведите получившиеся значения в консоль.

# matrix = [[i for i in range(j, j + 3)] for j in range(20, 29, 3)]
#
# row_sums = [sum(row) for row in matrix]
#
# print("Матрица 3x3:")
# for row in matrix:
#     print(row)
#
# print("\nСуммы элементов в каждом ряду:")
# for row_sum in row_sums:
#     print(row_sum)


# Задача 6: Подсчет количества четных и нечетных чисел в матрице
# Дана матрица
# matrix = [
#     [2, 5, 8, 11],
#     [14, 17, 20, 23],
#     [26, 29, 32, 35],
#     [38, 41, 44, 47]
# ]
#
# Напишите программу для посчета четных и нечетных чисел в каждом вложенном списке (строке матрицы).
# Выведите значения в констоль:
# print(f"Количество четных чисел: ")
# print(f"Количество нечетных чисел: ")
#
# for row in matrix:
#     for num in row:
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#
# print(f"Количество четных чисел: {even_count}")
# print(f"Количество нечетных чисел: {odd_count}")


# Задача 7: Поиск минимального и максимального значения в матрице
# Дана матрица
# matrix = [
#     [34, 23, 18],
#     [14, 55, 27],
#     [19, 42, 31]
# ]
#
# Напишите программу для вывода минимального и максимального значений в каждом ряду (вложенном списке) матрицы.

# matrix = [
#     [34, 23, 18],
#     [14, 55, 27],
#     [19, 42, 31]
# ]

# for row in matrix:
#     min_value = min(row)  # Находим минимальное значение в ряду
#     max_value = max(row)  # Находим максимальное значение в ряду
#     print(f"Минимальное значение в ряду: {min_value}, Максимальное значение в ряду: {max_value}")


# Задача 8. Напишите функцию increment_global, которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.
# increment_global()
# print(counter)  # Вывод: 1
# increment_global()
# print(counter)  # Вывод: 2

# counter = 0  # глобальная переменная

# def increment_global():
#     global counter  # указываем, что работаем с глобальной переменной
#     counter += 1
#
# increment_global()
# print(counter)  # Вывод: 1
# increment_global()
# print(counter)  # Вывод: 2


# Задача 9. Напишите функцию outer, которая содержит внутреннюю функцию inner. Внутренняя функция должна увеличивать
# значение переменной count, объявленной во внешней функции, на 1 каждый раз при её вызове.
# counter = outer()
# print(counter())  # Вывод: 1
# print(counter())  # Вывод: 2

# def outer():
#     count = 0  # Переменная count, которая будет увеличиваться при каждом вызове
#     def inner():
#         nonlocal count  # Указываем, что count - это переменная из внешней функции
#         count += 1
#         return count
#     return inner
#
# counter = outer()  # Создаем экземпляр функции inner через outer
# print(counter())  # Вывод: 1
# print(counter())  # Вывод: 2


# Задача 10. Напишите функцию make_multiplier, которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15

# def make_multiplier(factor):
#     def multiplier(x):
#         return x * factor
#     return multiplier
#
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))
#
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))


# Задача 11. Напишите функцию make_prefixer, которая принимает строку prefix и возвращает внутреннюю функцию prefixer.
# Внутренняя функция должна добавлять prefix к любому переданному ей аргументу.
# add_hello = make_prefixer("Hello, ")
# print(add_hello("Alice"))  # Вывод: Hello, Alice
# print(add_hello("Bob"))    # Вывод: Hello, Bob

# def make_prefixer(prefix):
#     def prefixer(name):
#         return prefix + name
#     return prefixer
#
# add_hello = make_prefixer("Hello, ")
# print(add_hello("Alice"))
# print(add_hello("Bob"))

# Задача 12. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.

# def create_user(username, email, **kwargs):
#     user_info = {
#         "username": username,
#         "email": email
#     }
#     user_info.update(kwargs)  # Добавляем дополнительные данные из kwargs
#     return user_info
#
# user = create_user("alice", "alice@example.com", age=30, city="Berlin", phone="123456789")
# print(user)


# Задача 13. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple

# def make_replacer(old, new):
#     def replacer(string):
#         return string.replace(old, new)
#     return replacer
#
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))
# print(replace_a_with_o("apple"))


# Задача 14. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!

# def make_suffixer(suffix):
#     def suffixer(word):
#         return word + suffix
#     return suffixer
#
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))
# print(add_exclamation("Wow"))

# Задача 15. Напишите функцию make_case_changer, которая принимает аргумент case (значения могут быть "upper" или "lower").
# Внутри этой функции создайте и верните функцию case_changer, которая изменяет регистр строки в зависимости от
# переданного аргумента (если передан аргумент с заглавными буквами, то делаете их строчными, если со строчными,
# то делает их заглавными).
# to_upper = make_case_changer("upper")
# print(to_upper("hello"))  # Вывод: HELLO
# to_lower = make_case_changer("lower")
# print(to_lower("WORLD"))  # Вывод: world

# def make_case_changer(case):
#     def case_changer(text):
#         if case == "upper":
#             return text.upper()
#         elif case == "lower":
#             return text.lower()
#         else:
#             raise ValueError("Invalid case argument, should be 'upper' or 'lower'")
#     return case_changer
#
# to_upper = make_case_changer("upper")
# print(to_upper("hello"))
#
# to_lower = make_case_changer("lower")
# print(to_lower("WORLD"))

# Задача 16. Напишите функцию make_trimmer, которая принимает аргумент length. Внутри этой функции создайте и
# верните функцию trimmer, которая обрезает строку до заданной длины.
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))  # Вывод: Hel
# print(trim_to_3("World"))  # Вывод: Wor

# def make_trimmer(length):
#     def trimmer(string):
#         return string[:length]
#     return trimmer
#
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))
# print(trim_to_3("World"))
