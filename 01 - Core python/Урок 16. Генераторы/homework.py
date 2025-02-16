# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор,
# возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
def next_num():
    for num in range (1,10):
        yield num
num = next_num()
while True:
    try:
        print(next(num))
    except StopIteration:
        print("Коллекция Завершена")
        break



# Задание 2: Напишите выражение-генератор,
# которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration

def quadrat():
    for num in range (1, 10):
        yield num**2
        print(num)
gen = quadrat()
while True:
    try:
        print(next(gen))
    except StopIteration:
        print("Коллекция Завершена")
        break


# Задание 3: Напишите функцию-генератор,
# которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
def one_word(sentence):
    for word in sentence.split():
        yield word

sentence = "Hello, world!"
word = one_word(sentence)
while True:
    try:
        print(next(word))
    except StopIteration:
        print("End of sentence")
        break

# Тема: Генераторы и встроенные функции

# Задача 1: Генератор и функция set()
# Задание: Напишите генератор,
# который возвращает числа от 1 до 10,
# но если число четное, возвратите его удвоенным.
# Используйте функцию set(), чтобы преобразовать результат генератора в множество и выведите его.
def number_generator(n):
    for i in range(n):
        if i%2 == 0:
            yield i*2
        else:
            yield i
gen = number_generator(10)
# Преобразование генератора в множество
num_set = set(gen)
print(num_set)

# Задача 2: Генератор и функция sum()
# Задание: Напишите генератор, который возвращает числа от 1 до 20, кратные 3. Используйте функцию sum(),
# чтобы найти сумму всех этих чисел и выведите результат.
def number_generator():
    for i in range(1, 21):
        if i%3 == 0:
            yield i

gen = number_generator()
# Преобразование генератора в множество
num_set = sum(gen)
print(num_set)

# Задача 3: Генератор и функции min() и max()
# Задание: Напишите генератор,
# который возвращает длины слов в заданной строке.
# Используйте функции min() и max(),
# чтобы найти минимальную и максимальную длину слов и выведите их.

# sentence = "Write a generator that returns word lengths from a given sentence"
def word_lengths_generator(sentence):
    for word in sentence.split():
        yield len(word)
sentence = "Write a generator that returns word lengths from a given sentence"
lengths_gen = word_lengths_generator(sentence)
lengths = list(lengths_gen)
while True:
    try:
        print(len(next(word)))
    except StopIteration:
        print("End of sentence")
        break
min_length = min(lengths)
max_length = max(lengths)
print(f"Минимальная длина слова: {min_length}")
print(f"Максимальная длина слова: {max_length}")
# Тема: Генераторы и файлы

# Задача 1: Чтение и фильтрация строк по ключевому слову
# Создайте генератор, который читает строки из файла и возвращает только те строки,
# которые содержат заданное ключевое слово (x_word).
# Программа должна одинаково реагировать на написание слова строчными и заглавными буквами.
# Файл: data.txt

# x_word = 'this'
def read_and_filter_lines(file_path, keyword):
    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line:
                yield line  # Возвращает строку, если она содержит ключевое слово

file_path = './text_files/data.txt'
x_word = 'this'
keyword = x_word
filtered_line_generator = read_and_filter_lines(file_path, keyword)

for line in filtered_line_generator:
    print(line.strip())

# Задача 2: Чтение файла по частям и подсчет строк
# Создайте генератор, который читает файл по частям заданного размера (например, 50 байт)
# и подсчитывает количество строк в каждой части.
# Файл: data.txt
def read_file(file_path, chunk_size=50):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)  # Читает часть файла
            if not chunk:
                break
            yield chunk  # Возвращает часть файла

file_path = './text_files/data.txt'
# Использование генератора
chunk_generator = read_file(file_path)

for chunk in chunk_generator:
    print(chunk)

# Задача 3: Поиск строк, содержащих числа
# Создайте генератор, который читает строки из файла и возвращает только те строки, которые содержат числа.
# Файл: data.txt
def read_and_filter_lines(file_path, keyword):
    with open(file_path, 'r') as file:
        for line in file:
            for num in line:
                if num.isnumeric():
                    yield line  # Возвращает строку, если она содержит ключевое слово

file_path = './text_files/data.txt'
# x_word = 'this'

filtered_line_generator = read_and_filter_lines(file_path, keyword)

for line in filtered_line_generator:
    print(line.strip())