# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
squares = (x ** 2 for x in range(11))
try:
    while True:
        print(next(squares))
except StopIteration:
    pass

# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration

def word_generator(sentence):
    words = sentence.split()
    for word in words:
        yield word

# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор, который возвращает числа от 1 до 10, но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
double_even_numbers = set(x * 2 if x % 2 == 0 else x for x in range(1, 11))
print(double_even_numbers)

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.

sum_of_multiples = sum(x for x in range(1, 21) if x % 3 == 0)
print(sum_of_multiples)

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор, который возвращает длины слов в заданной строке. Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.
# sentence = "Write a generator that returns word lengths from a given sentence"
sentence = "Write a generator that returns word lengths from a given sentence"
word_lengths = (len(word) for word in sentence.split())
print(min(word_lengths), max(word_lengths))

# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt
def filter_lines(filename, keyword):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword.lower() in line.lower():
                yield line.strip()
x_word = 'this'


# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt
def read_file_in_chunks(filename, chunk_size=50):
    with open(filename, 'r', encoding='utf-8') as file:
        while chunk := file.read(chunk_size):
            yield chunk.count('\n')

# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
def lines_with_numbers(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if any(char.isdigit() for char in line):
                yield line.strip()