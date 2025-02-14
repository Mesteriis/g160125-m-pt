# Пример 1
numbers = [1, 2, 3, 4, 5]  # Готовая коллекция элементов
iter_numbers = iter(numbers)  # Создается итератор

print(next(iter_numbers))  # Вывод по одному элементу

# Пример 2
def number_generator():  # Генератор
    for num in range(1, 6):  # Создание элементов
        yield num  # yield останавливает цикл, запоминает его состояние
                   # и отдает один элемент при каждом вызове

gen_numbers = number_generator()

print(next(gen_numbers))  # Вывод по одному элементу

# Пример 3
def num_gen():  # Функция-генератор
    for num in range(1, 6):
        yield num

gen = num_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# Пример 4
def num_ret():  # Обычная функция
    for num in range(1, 6):
        return num

ret = num_ret()
print(ret)
print(ret)
print(ret)

# Пример 5
def simple_generator_with_for():  # Генератор
    values = [1, 2, 3]
    for value in values:
        yield value

gen = simple_generator_with_for()
print(next(gen))  # Результат: 1
print(next(gen))  # Результат: 2
print(next(gen))  # Результат: 3

# Пример 6
squares_gen = (x * x for x in range(10))  # Выражение-генератор

def squares_generator():  # Функция-генератор
    for x in range(10):
        yield x * x

gen = squares_generator()
print(next(gen))
print(next(gen))
print(next(gen))

# Пример 7
numbers = [10, 20, 30, 40, 50]
iter_numbers = iter(numbers)

print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))

# Пример 8
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(next(gen))
print(next(gen))
print(next(gen))

# Пример 9
squares_gen = (x * x for x in range(4))
print(next(squares_gen))
print(next(squares_gen))
print(next(squares_gen))

# Пример 10
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

gen = even_numbers(5)
print(next(gen))
print(next(gen))
print(next(gen))


# Пример 11
# Генератор для создания последовательности чисел
def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(10)
# Преобразование генератора в список
num_list = list(gen)
print(num_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Пример 12
# Генератор для создания последовательности чисел
def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(10)
# Преобразование генератора в множество
num_set = set(gen)
print(num_set)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Пример 13
# Генератор для создания последовательности чисел
def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(10)
# Суммирование чисел из генератора
total = sum(gen)
print(total)  # 45

# Пример 14
# Генератор для создания последовательности чисел
def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(10)
# Нахождение максимального значения
max_value = max(gen)
print(max_value)  # 9

gen = number_generator(10)
# Нахождение минимального значения
min_value = min(gen)
print(min_value)  # 0

# Пример 15
# Генератор для создания последовательности чисел
def number_generator(n):
    for i in range(n):
        yield i

# Итерация с использованием цикла for
gen = number_generator(5)
for num in gen:
    print(num)

# Пример 16
def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line  # Возвращает одну строку за раз

file_path = 'large_file.txt'
# Использование генератора
line_generator = read_file(file_path)

for line in line_generator:
    print(line.strip())  # Выводит строку без пробелов в начале и конце

# Пример 17
def read_file(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)  # Читает часть файла
            if not chunk:
                break
            yield chunk  # Возвращает часть файла

file_path = 'large_file.txt'
# Использование генератора
chunk_generator = read_file(file_path)

for chunk in chunk_generator:
    print(chunk)  # Выводит часть файла

# Пример 18
def read_and_filter_lines(file_path, keyword):
    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line:
                yield line  # Возвращает строку, если она содержит ключевое слово

file_path = 'large_file.txt'
keyword = 'important'
filtered_line_generator = read_and_filter_lines(file_path, keyword)

for line in filtered_line_generator:
    print(line.strip())  # Обрабатывает и выводит строки, содержащие ключевое слово