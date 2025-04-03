#
# ### Циклы
#
# 1. **Как работает цикл `for` в Python? Приведите пример.**
#    Цикл `for` используется для итерации по элементам в коллекции (например, списке, строке и т.д.).
#    ```python
#    for i in range(5):
#        print(i)
#    # Вывод: 0, 1, 2, 3, 4
#    ```
#
# 2. **Как работает цикл `while`? Приведите пример.**
#    Цикл `while` выполняет блок кода, пока условие истинно.
#    ```python
#    i = 0
#    while i < 5:
#        print(i)
#        i += 1
#    # Вывод: 0, 1, 2, 3, 4
#    ```
#
# 3. **Как использовать операторы `break` и `continue` в циклах?**
#    - `break` завершает выполнение цикла.
#    - `continue` пропускает текущую итерацию и переходит к следующей.
#    ```python
#    for i in range(5):
#        if i == 3:
#            break
#        print(i)
#    # Вывод: 0, 1, 2
#
#    for i in range(5):
#        if i == 3:
#            continue
#        print(i)
#    # Вывод: 0, 1, 2, 4
#    ```
#
# 4. **Как создавать вложенные циклы?**
#    Вложенные циклы могут быть использованы для работы с многомерными коллекциями.
#    ```python
#    for i in range(3):
#        for j in range(3):
#            print(i, j)
#    ```
#
# 5. **Как итерироваться по списку с использованием индексов?**
#    Можно использовать функцию `enumerate()`, чтобы получить индекс и значение в одной итерации.
#    ```python
#    fruits = ["apple", "banana", "orange"]
#    for index, value in enumerate(fruits):
#        print(index, value)
#    # Вывод: 0 apple, 1 banana, 2 orange
#    ```
#
# ---
#
# ### Итераторы и генераторы списков
#
# 1. **Что такое итератор и как он используется в Python?**
#    Итератор — это объект, который реализует методы `__iter__()` и `__next__()`, позволяя проходить по элементам коллекции.
#    ```python
#    lst = [1, 2, 3]
#    it = iter(lst)
#    print(next(it))  # 1
#    print(next(it))  # 2
#    ```
#
# 2. **Как создать генератор списка? Приведите пример.**
#    Генераторы списков позволяют создать новый список, применяя выражение к каждому элементу:
#    ```python
#    squares = [x**2 for x in range(5)]
#    print(squares)  # [0, 1, 4, 9, 16]
#    ```
#
# 3. **В чем разница между списковыми включениями и обычными циклами `for`?**
#    Генераторы списков создают новый список за одну строку, тогда как цикл `for` создает список вручную с помощью метода `append()`.
#    ```python
  # Выберите задачи для лайвкодинга. Ранее все эти задачи давались для решения в сессионных залах.
# Можно давать свои задачи наподобие тех, что студенты решали во время уроков.

# Задача 1: Напишите программу с помощью генераторов списков,
# которая находит все числа от 1 до 1000, которые делятся на 7.

# nums_gen = [num for num in range(1, 1001) if num % 7 == 0]
# print(nums_gen)

# Задача 2: Напишите программу с помощь генераторов списков,
# которая найдите все числа от 1 до 1000, в которых есть цифра 3.

# nums_gen = [num for num in range(1, 1001) if "3" in str(num)]
# print(nums_gen)

# Задача 3: Напишите программу с помощь генераторов списков,
# которая посчитает количество пробелов в строке

# some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
# space_count = [space for space in some_string if space == " " in str(some_string)]
# print(len(space_count))


# Задача 4: Напишите программу с помощь генераторов списков,
# которая создаст список всех гласных букв в строке
# some_string = 'the quick brown fox jumps over the lazy dog'
#
# vowels = "aeoiu"
#
# get_lowels = [vowel for vowel in some_string if vowel in vowels]
# print(len(get_lowels))

# Задача 5: Сумма элементов в каждом ряду матрицы
# С помощью генераторов списков создайте матрицу 3x3 из чисел от 20 до 28
# Ожидаемая матрица:
# [20, 21, 22]
# [23, 24, 25]
# [26, 27, 28]

# matrix = [[num for num in range(i, i+3)] for i in range(20, 29, 3)]
# for row in matrix:
#     print(row)
# row_sums = [sum(row) for row in matrix]
# print("Суммы элементов в каждом ряду:", row_sums)

# Напишите код для вычисления суммы элементов в каждом ряду (в каждом вложенном списке).
# Выведите получившиеся значения в консоль.


# Задача 6: Подсчет количества четных и нечетных чисел в матрице
# Дана матрица
# matrix = [
#     [2, 5, 8, 11],
#     [14, 17, 20, 23],
#     [26, 29, 32, 35],
#     [38, 41, 44, 47]
# ]
#
# for list in matrix:
#     even_counter = 0
#     odd_counter = 0
#     for num in list:
#         if num % 2 == 0:
#             even_counter += 1
#         else:
#             odd_counter += 1

# Напишите программу для посчета четных и нечетных чисел в каждом вложенном списке (строке матрицы).
# Выведите значения в констоль:
# print(f"Количество четных чисел: {even_counter} ")
# print(f"Количество нечетных чисел: {odd_counter}")


# Задача 7: Поиск минимального и максимального значения в матрице
# Дана матрица
# matrix = [
#     [34, 23, 18],
#     [14, 55, 27],
#     [19, 42, 31]
# ]
#
# max_num = matrix[0][0]
# min_num = matrix[0][0]
#
# for list in matrix:
#     for num in list:
#         if num > max_num:
#             max_num = num
#         if num < max_num:
#             min_num = num
#
# print(f"Max num: {max_num}, Min num: {min_num}")
#
# Напишите программу для вывода минимального и максимального значений в каждом ряду (вложенном списке) матрицы.


# Задача 8. Напишите функцию increment_global, которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.
# counter = 0
# def increment_global():
#     global counter
#     counter += 1
#     return counter
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
#     counter = 0
#     def inner():
#         nonlocal counter
#         counter += 1
#         print(counter)
#     return inner
#
# counter = outer()
# print(counter())  # Вывод: 1
# print(counter())  # Вывод: 2


# Задача 10. Напишите функцию make_multiplier, которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.
# def make_multiplier(factor):
#     def multiplier(x):
#         return x * factor
#     return multiplier
#
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15


# Задача 11. Напишите функцию make_prefixer, которая принимает строку prefix и возвращает внутреннюю функцию prefixer.
# Внутренняя функция должна добавлять prefix к любому переданному ей аргументу.
# def make_prefixer(prefix):
#     def prefixer(x):
#         return prefix + x
#     return prefixer
#
# add_hello = make_prefixer("Hello, ")
# print(add_hello("Alice"))  # Вывод: Hello, Alice
# print(add_hello("Bob"))    # Вывод: Hello, Bob


# Задача 12. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.
# users = {}
# def create_user(username, email, **kwargs):
#     global users
#     user_info = {
#        "username": username,
#         "email":email
#     }
#     user_info.update(kwargs)
#     users[username] = user_info
#
#     return user_info
#
# add_user = create_user("John", "mail@mail.com", married = True )
# # print(add_user)
# print(users)
# Задача 13. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.
# def make_replacer(old, new):
#     def replacer(text):
#         return text.replace(old, new)
#     return replacer
#
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple


# Задача 14. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.
# def make_suffixer(suffix):
#     def suffixer(x):
#         return x + suffix
#     return suffixer
#
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!


# Задача 15. Напишите функцию make_case_changer, которая принимает аргумент case (значения могут быть "upper" или "lower").
# Внутри этой функции создайте и верните функцию case_changer, которая изменяет регистр строки в зависимости от
# переданного аргумента (если передан аргумент с заглавными буквами, то делаете их строчными, если со строчными,
# то делает их заглавными).
# def make_case_changer(case):
#     def case_changer(text):
#         if case == "upper":
#             return text.upper()
#         if case == "lower":
#             return text.lower()
#         else:
#             return text
#
#     return case_changer
#
# to_upper = make_case_changer("upper")
# print(to_upper("hello"))  # Вывод: HELLO
# to_lower = make_case_changer("lower")
# print(to_lower("WORLD"))  # Вывод: world


# Задача 16. Напишите функцию make_trimmer, которая принимает аргумент length. Внутри этой функции создайте и
# верните функцию trimmer, которая обрезает строку до заданной длины.
# def make_trimmer(length):
#     def trimmer(text):
#         return text[:length]
#     return trimmer
#
#
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))  # Вывод: Hel
# print(trim_to_3("World"))  # Вывод: Wor