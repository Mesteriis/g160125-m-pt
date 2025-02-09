# Упражнение 1: Напишите программу с помощью генераторов списков,
# которая находит все числа от 1 до 1000, которые делятся на 7.


# for num in range(1, 1001):
#     if num % 7 == 0:
#         print(num)
# numbers = [num for num in range(1,1001) if num % 7 == 0]
# print(numbers)
# [x for x in range(1, 1001) if x % 7 ==0]

# Упражнение 2: Напишите программу с помощь генераторов списков,
# которая найдите все числа от 1 до 1000, в которых есть цифра 3.

# numbers = [num for num in range(1,1001) if num "3"]
numbers_with_3 = [num for num in range(1,1001) if "3" in str(num)]
print(numbers_with_3)
# Упражнение 3: Напишите программу с помощь генераторов списков,
# которая посчитает количество пробелов в строке
# some_string = 'the slow solid squid swam sumptuously through the slimy swamp'.
# count_spaces = sum(item for some_string in some_string if item ==" ")
# some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
# string_with_space = sum(1 for space in some_string if space == " ")
# print(string_with_space)

# Упражнение 4: Напишите программу с помощь генераторов списков,
# которая создаст список всех гласных букв в строке
some_string = 'the quick brown fox jumps over the lazy dog'
vocals = "a,e,i,u,o"

some_string_with = sum(1 for x in some_string if x in vocals)
print(some_string_with)

some_string = 'the quick brown fox jumps over the lazy dog'
vocals = "a","i","e","u","o"

letter_count = sum(1 for letter in some_string if letter in vocals)
print(letter_count)

# Упражнение 5: Сумма элементов в каждом ряду матрицы
# С помощью генераторов списков создайте матрицу
# 3x3 из чисел от 20 до 28
# Ожидаемая матрица:
# [20, 21, 22]
# [23, 24, 25]
# [26, 27, 28]

matrix1 = [[(i*3) + j + 20 for j in range(3)]for i in range(3)]
print(matrix1)
row_sums = [sum(row) for row in matrix1]
print(row_sums)

#
# Напишите код для вычисления суммы элементов в каждом ряду (в каждом вложенном списке).
# Выведите получившиеся значения в консоль.
# Создаем матрицу 3x3 с числами от 20 до 28
matrix = [[20 + j + i * 3 for j in range(3)] for i in range(3)]

# Вычисляем сумму элементов в каждом ряду
row_sums = [sum(row) for row in matrix]

# Вывод матрицы и суммы по рядам
print("Matrix:")
for row in matrix:
    print(row)

print("\nRow sums:")
for s in row_sums:
    print(s)

# Упражнение 6: Подсчет количества четных и нечетных чисел в матрице
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


# Упражнение 7: Поиск минимального и максимального значения в матрице
# Дана матрица
# matrix = [
#     [34, 23, 18],
#     [14, 55, 27],
#     [19, 42, 31]
# ]
#
# Напишите программу для вывода минимального и максимального значений в каждом ряду (вложенном списке) матрицы.