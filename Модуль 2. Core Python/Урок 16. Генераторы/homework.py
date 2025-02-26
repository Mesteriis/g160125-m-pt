# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration

# class NumberIterator:
#     def __init__(self, n):
#         self.n = n
#         self.current = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.n:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value
#
#
# try:
#     n = 5
#     iterator = NumberIterator(n)
#     for num in iterator:
#         print(num)
# except StopIteration:
#     print("Итерация завершена.")

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration

# gen = (x**2 for x in range(11))
#
# try:
#     while True:
#         print(next(gen))
# except StopIteration:
#     print("Генератор завершил работу.")


# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration

# def word_generator(sentence):
#     words = sentence.split()
#     for word in words:
#         yield word
#
# sentence = "Это тестовое предложение для генератора"
# gen = word_generator(sentence)
#
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         print("Все слова закончились.")
#         break


# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.

# def number_generator():
#     for num in range(1, 11):
#         yield num * 2 if num % 2 == 0 else num
#
# # Преобразуем результат генератора в множество
# result_set = set(number_generator())
#
# # Выводим результат
# print(result_set)

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.

# def multiples_of_three():
#     for num in range(1, 21):
#         if num % 3 == 0:
#             yield num
#
# result = sum(multiples_of_three())
#
# print("Сумма чисел от 1 до 20, кратных 3:", result)

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"

# def word_lengths(sentence):
#     for word in sentence.split():
#         yield len(word)
#
# sentence = "Write a generator that returns word lengths from a given sentence"
#
# lengths = list(word_lengths(sentence))
#
# print("Минимальная длина слова:", min(lengths))
# print("Максимальная длина слова:", max(lengths))

# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt

# def filter_lines_by_keyword(file_name, x_word):
#     with open(file_name, 'r') as file:
#         for line in file:
#             if x_word.lower() in line.lower():  # Игнорируем регистр
#                 yield line.strip()
#
# x_word = 'this'
#
# file_name = 'data.txt'
# for line in filter_lines_by_keyword(file_name, x_word):
#     print(line)


# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt

# def read_file_in_chunks(file_name, chunk_size):
#     with open(file_name, 'r') as file:
#         chunk = ''
#         for line in file:
#             chunk += line  # Добавляем строку в текущий кусок
#             if len(chunk) >= chunk_size:  # Если длина части больше или равна размеру
#                 yield len(chunk.splitlines()), chunk  # Возвращаем количество строк в части и саму часть
#                 chunk = ''  # Очищаем текущий кусок для следующего
#         if chunk:  # Для последнего фрагмента, который может быть меньше chunk_size
#             yield len(chunk.splitlines()), chunk
#
# file_name = 'data.txt'
# chunk_size = 50  # Размер части в байтах

# Пример использования генератора
# for line_count, chunk in read_file_in_chunks(file_name, chunk_size):
#     print(f"Количество строк в части: {line_count}")


# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt

# import re
#
# def find_lines_with_numbers(file_name):
#     with open(file_name, 'r') as file:
#         for line in file:
#             if re.search(r'\d', line):  # Проверяем, содержит ли строка цифры
#                 yield line.strip()  # Возвращаем строку, если она содержит числа
#
# file_name = 'data.txt'
#
# # Пример использования генератора
# for line in find_lines_with_numbers(file_name):
#     print(line)
