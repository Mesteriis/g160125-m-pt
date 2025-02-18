# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями

# Задача 1: Использование filter с генератором и лямбда функцией
# Напишите генератор, который возвращает числа от 1 до 20.
# Используйте функцию `filter` с лямбда функцией для отбора четных чисел и выведите результат.
# Ожидаемый результат: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# numbers = (n for n in range(1, 21))
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# Задача 2: Использование zip с итераторами и лямбда функцией
# Создайте два итератора: один для чисел от 1 до 5, другой для их квадратов.
# Используйте функцию `zip`,
# чтобы объединить эти итераторы в список кортежей, и примените лямбда функцию для их вывода
# в формате строки "число: квадрат".
# Ожидаемый результат: ['1: 1', '2: 4', '3: 9', '4: 16', '5: 25']
# numbers = (n for n in range(1, 6))
# squares = (n**2 for n in range(1, 6))
# combined = zip(numbers, squares)
# result = list(map(lambda x: f"{x[0]}: {x[1]}", combined))
# print(result)
# zipped = zip(range(1, 6), map(lambda x: x * x, range(1, 6)))
# print(list(zipped))
# Задача 3: Использование map и filter с файлом и лямбда функцией
# Напишите генератор, который читает строки из файла `example.txt`.
# Используйте функцию `filter` с лямбда функцией, чтобы отобрать
# строки, содержащие слово "Python",
# и затем примените функцию `map` с лямбда функцией для
# преобразования этих строк в верхний регистр.
def read_lines(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line.strip()

lines = read_lines("example.txt")

filtered_lines = filter(lambda line: "Python" in line, lines)

result = list(map(lambda line: line.upper(), filtered_lines))

print(result)

