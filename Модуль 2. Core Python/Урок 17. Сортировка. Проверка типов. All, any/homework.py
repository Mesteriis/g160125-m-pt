# Тема: map, filter, zip

# Задача 1: Применение функции map для преобразования чисел
# Напишите функцию `square`, которая принимает число и возвращает его квадрат.
# Используйте функцию `map`, чтобы применить эту функцию к списку чисел `[1, 2, 3, 4, 5]` и выведите результат.
#
# numbers = [1, 2, 3, 4, 5]
# Ожидаемый результат: [1, 4, 9, 16, 25]

# def square(x):
#     return x ** 2
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))
#
# print(squared_numbers)


# Задача 2: Применение функции filter для отбора четных чисел
# Напишите функцию `is_even`, которая принимает число и возвращает `True`, если число четное,
# и `False` в противном случае. Используйте функцию `filter`, чтобы отобрать четные числа из
# списка `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` и выведите результат.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ожидаемый результат: [2, 4, 6, 8, 10]

# def is_even(x):
#     return x % 2 == 0
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(is_even, numbers))
#
# print(even_numbers)


# Задача 3: Применение функции zip для объединения списков
# У вас есть два списка: `names = ["Alice", "Bob", "Charlie"]` и `ages = [25, 30, 35]`.
# Используйте функцию `zip`, чтобы создать список кортежей, где каждый кортеж содержит имя и возраст,
# и выведите результат.
#
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# Ожидаемый результат: [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
#
# combined = list(zip(names, ages))
#
# print(combined)


# Задача 4: Применение функции map для преобразования строк в числа
# Напишите функцию `to_int`, которая принимает строку и возвращает ее преобразование в целое число.
# Используйте функцию `map`, чтобы применить эту функцию к списку строк `["1", "2", "3", "4", "5"]`
# и выведите результат.
#
# str_numbers = ["1", "2", "3", "4", "5"]
# Ожидаемый результат: [1, 2, 3, 4, 5]

# def to_int(s):
#     return int(s)
#
# str_numbers = ["1", "2", "3", "4", "5"]
# int_numbers = list(map(to_int, str_numbers))
#
# print(int_numbers)


# Задача 5: Применение функции filter для отбора слов длиннее 3 символов
# Напишите функцию `longer_than_three`, которая принимает строку и возвращает `True`,
# если длина строки больше 3 символов, и `False` в противном случае. Используйте функцию `filter`,
# чтобы отобрать слова длиной больше 3 символов из списка `["apple", "kiwi", "banana", "pear"]` и выведите результат.
#
# words = ["apple", "kiwi", "banana", "pear"]
# Ожидаемый результат: ["apple", "banana", "pear"]

# def longer_than_three(word):
#     return len(word) > 3
#
# words = ["apple", "kiwi", "banana", "pear"]
# filtered_words = list(filter(longer_than_three, words))
#
# print(filtered_words)


# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями

# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# even_numbers = list(filter(lambda x: x % 2 == 0, (i for i in range(1, 21))))
# print(even_numbers)


# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов. Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']

# numbers = iter(range(1, 6))
# squares = iter(map(lambda x: x ** 2, range(1, 6)))
#
# zipped = zip(numbers, squares)
#
# result = list(map(lambda pair: f"{pair[0]}: {pair[1]}", zipped))
#
# print(result)


# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для преобразования этих строк в верхний регистр.
#
# def read_lines(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         for line in file:
#             yield line.strip()
#
# filtered_lines = filter(lambda line: "Python" in line, read_lines("example.txt"))
#
# uppercase_lines = map(lambda line: line.upper(), filtered_lines)
#
# print(list(uppercase_lines))


# Тема: Дополнительная практика

# Задача 1: Использование map с генератором и лямбда функцией для конвертации температур
# Напишите генератор, который возвращает температуры в Цельсиях от -10 до 10.
# Используйте функцию `map` с лямбда функцией для конвертации этих температур в Фаренгейты и выведите результат.
# Ожидаемый результат: [14.0, 15.8, 17.6, 19.4, 21.2, 23.0, 24.8, 26.6, 28.4, 30.2,
# 32.0, 33.8, 35.6, 37.4, 39.2, 41.0, 42.8, 44.6, 46.4, 48.2, 50.0]

# def celsius_generator():
#     for temp in range(-10, 11):
#         yield temp
#
# fahrenheit_temps = list(map(lambda c: round(c * 9/5 + 32, 1), celsius_generator()))
#
# print(fahrenheit_temps)


# Задача 2: Использование filter с итератором и лямбда функцией для фильтрации строк по длине
# Создайте итератор для списка строк `["hello", "world", "python", "is", "awesome"]`.
# Используйте функцию `filter` с лямбда функцией для отбора строк длиной более 5 символов и выведите результат.
# Ожидаемый результат: ['python', 'awesome']

# words = ["hello", "world", "python", "is", "awesome"]
#
# filtered_words = filter(lambda word: len(word) > 5, words)
#
# result = list(filtered_words)
# print(result)


# Задача 3: Использование zip и map для объединения и форматирования данных из двух генераторов
# Напишите два генератора: один для чисел от 1 до 3, другой для их кубов. Используйте функцию `zip`,
# чтобы объединить эти генераторы в список кортежей, и примените функцию `map` с лямбда функцией
# для вывода данных в формате строки "число: куб".
# Ожидаемый результат: ['1: 1', '2: 8', '3: 27']

# numbers = (i for i in range(1, 4))
# cubes = (i**3 for i in range(1, 4))
#
# zipped = zip(numbers, cubes)
#
# result = map(lambda x: f"{x[0]}: {x[1]}", zipped)
#
# print(list(result))


# Задача 4: Использование filter и map с файлом для преобразования данных
# Напишите генератор, который читает строки из файла `data.txt`.
# Используйте функцию `filter` с лямбда функцией для отбора строк, содержащих числа.
# Затем примените функцию `map` с лямбда функцией для преобразования этих строк в целые числа и выведите результат.

# def read_file(file_name):
#     with open(file_name, 'r') as file:
#         for line in file:
#             yield line.strip()  # Убираем лишние пробелы и символы новой строки
#
# def process_file(file_name):
#     lines = read_file(file_name)
#
#     filtered_lines = filter(lambda line: line.isdigit(), lines)
#
#     mapped_lines = map(int, filtered_lines)
#
#     for number in mapped_lines:
#         print(number)
#
# process_file('data.txt')


# Задача 5: Использование zip с итераторами для обработки данных из двух файлов
# Создайте два генератора, которые читают строки из файлов `file1.txt` и `file2.txt`.
# Используйте функцию `zip`, чтобы объединить данные из этих файлов, и примените лямбда функцию
# для вывода данных в формате "file1_line - file2_line".

# def read_file(file_name):
#     with open(file_name, 'r') as file:
#         for line in file:
#             yield line.strip()
#
# def process_files(file1_name, file2_name):
#     lines_file1 = read_file(file1_name)
#     lines_file2 = read_file(file2_name)
#
#     for line1, line2 in zip(lines_file1, lines_file2):
#         print(f"{line1} - {line2}")
#
# process_files('file1.txt', 'file2.txt')
