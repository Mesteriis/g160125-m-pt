# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы
# Покажите в режиме live-coding и объясните:
# - Создание и использование итератора
from icecream import ic as print
# numbers = [1, 2, 3, 4, 5]
#
# iterator = iter(numbers)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# - Создание и использование функции-генератора
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
# it_s = simple_generator()
# print(next(it_s))
# print(next(it_s))
# print(next(it_s))
#
# def simple_generator():
#     for i in range(1, 4):
#         yield i
# it_s = simple_generator()
# print(next(it_s))
# print(next(it_s))
# print(next(it_s))
# # - Создание и использование выражения-генератора
#
# it_s = (i for i in range(1, 4))
# print(next(it_s))
# print(next(it_s))
# print(next(it_s))











# Тема: Генераторы и встроенные функции
# Покажите в режиме live-coding и объясните:
# - Использование генератора вместе с встроенными функциями list, set, min, max, sum.
# def simple_generator():
#     for i in range(1, 4):
#         yield i
#
# print(list(simple_generator()))
# print(set(simple_generator()))
# print(min(simple_generator()))
# print(max(simple_generator()))
# print(sum(simple_generator()))
#
# # - Использование генератора вместе с циклом for.
#
# for i in simple_generator():
#     print(i)
#
# it_ = simple_generator()
# while True:
#     try:
#         print(next(it_))
#     except StopIteration:
#         break
#
#







# Тема: Генераторы и файлы
# Покажите в режиме live-coding и объясните:
# - Чтение файлов построчно через генераторы
# - Чтение файлов по частям через генераторы
# - Фильтрацию с файлами через генераторы

def read_string_in_file(path):
    with open(path) as file:
        for line in file:
            yield line

def read_chunk_in_file(path, chunk_size):
    with open(path) as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def filter_file(path, word):
    with open(path) as file:
        for line in file:
            if word in line:
                yield line

path_file = './text_files/data.txt'

# for line in read_string_in_file(path_file):
#     print(line.strip())

# for chunk in read_chunk_in_file(path_file, 10):
#     print(chunk)

# for line in filter_file(path_file, 'word'):
#     print(line)


