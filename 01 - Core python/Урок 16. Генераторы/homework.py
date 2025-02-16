# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration

# def num_gen():
#     for num in range(1, 15):
#         yield num
#
# num = num_gen()
#
# while True:
#     try:
#         print(next(num))
#     except StopIteration:
#         print("Collection is over!")
#         break

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration

# numbers_gen = (x * x for x in range(0,10))
#
# def numbers_generator():
#     for x in range(10):
#         yield x * x
#
# gen = numbers_generator()
#
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         print("Collection is over!")
#         break
# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration

# def text_divide(text):
#     for word in text.split(" "):
#         yield word
#
# text = "Okay, Google"
# word = text_divide(text)
#
# while True:
#     try:
#         print(next(word))
#     except StopIteration:
#         print("End of text")
#         break

# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.

# def number_gen(n):
#     for num in range(n):
#         if num % 2 == 0:
#             yield num * 2
#         yield num
#
# gen = number_gen(10)
#
# num_set = set(gen)
# print(num_set)

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
# def num_gen():
#     for num in range(20):
#         if num % 3 == 0:
#             yield num
#
# gen = num_gen()
# sum_values = sum(gen)
# print(f"Values sum:", sum_values)

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.

# def sent_length(sentence):
#     words = sentence.split()
#
#     shortest_word = min(words, key= len)
#     longest_word = max(words, key=len)
#
#     yield shortest_word, len(shortest_word)
#     yield longest_word, len(longest_word)
#
#
# sentence = "Write a generator that returns word lengths from a given sentence"
# result = sent_length(sentence)
#
# shortest_word, shortest_len = next(result)
# longest_word, longest_len = next(result)
#
# print(f"Your shortest word: {shortest_word} : {shortest_len} symbol(s)")
# print(f"Your longest word: {longest_word} : {longest_len} symbol(s)")

# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt

# def read_and_filter_lines(file_path, keyword):
#     with open(file_path, 'r') as file:
#         for line in file:
#             if x_word in line:
#                 yield line
#
# file_path = './text_files/data.txt'
# x_word = 'this'
# filtered_line_generator = read_and_filter_lines(file_path, x_word)
#
# for line in filtered_line_generator:
#     print(f"Your keyword '{x_word}' in", line.strip())

# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt

# def read_file(file_path, read_size=50):
#     with open(file_path, 'r') as file:
#
#         while True:
#             reader = file.read(read_size)
#             if not reader:
#                 break
#             yield reader
#
# file_path = './text_files/data.txt'
# text = read_file(file_path)
# for part in text:
#     print(part)

# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt

# def read_and_filter_lines(file_path):
#     with open(file_path, 'r') as file:
#
#         for line in file:
#             for symbols in line:
#
#                 if any(symbols.isdigit() for symbols in line):
#                     yield line.strip()
#
# file_path = './text_files/data.txt'
#
# for line in read_and_filter_lines(file_path):
#     print(line)
