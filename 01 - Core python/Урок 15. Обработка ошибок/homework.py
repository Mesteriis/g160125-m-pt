# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.
def division(x,y):
    try:
        result = x/y
        print(result)
    except ZeroDivisionError:
        print("Zero Dev Imp")
    except TypeError:
        print("введено не число")
division(10,5)



# Задача 2: Обработка пользовательского ввода
# Напишите программу,
# которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.
def quadrat():
    x = input("x: ")
    try:
        quad = x ** 2
        print(quad)
    except ValueError:
        print("Value Error")
    except TypeError:
        print("Type Error, do int input")
quadrat()



# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1
# и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами
# (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются
# на примере FileNotFoundError.
try:
    file_d = open('./text_files/data.txt')
    content = file_d.read()
    file_d.seek(0)
    part_content = file_d.read(10)
    file_d.seek(0)
    str_content = file_d.readline()
    file_d.seek(0)
    all_str_content = file_d.readlines()
    print(all_str_content)
    file_d.close()

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No access to file")
except IOError:
    print("Incorrect input")


# Тема: Расространение исключения. Возбуждение исключения.
#
# Задача 1. Допишите код ниже.

import math

def calculate_square_root(number):
    # Добавьте проверку на отрицательное число и возбуждение исключения
    if number < 0:
        raise ValueError ("Введено негативное число")
    return math.sqrt(number)

def safe_calculate_square_root(number):
    try:
        result = calculate_square_root(number)
        print(f"Квадратный корень из {number} равен {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

# Тесты функции
safe_calculate_square_root(25)  # Ожидаемый результат: Квадратный корень из 25 равен 5.0
safe_calculate_square_root(-9)  # Ожидаемый результат: Ошибка: Число должно быть положительным
safe_calculate_square_root(9)

# Задача 2. Допишите код ниже.
def convert_to_number(string):
    # Добавьте проверку на некорректное значение и возбуждение исключения
    if not string.isnumeric():
        raise ValueError("Введено некорректное значение, вызван raise")
    return int(string)

def safe_convert_to_number(string):
    try:
        number = convert_to_number(string)
        print(f"Конвертированное число: {number}")
    except ValueError as e:
        print(f"Ошибка: {e}")

# Тесты функции
safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом


# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8, 14, добавив в него обработку ошибок, где это необходимо.
#
# Используйте файл как базу данных проекта.
# Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
#
# Меню:
# 1. Показать список товаров.
# 2. Добавить товар.
# 3. Удалить товар.
# 4. Обновить название товара, стоимость или количество.
# 5. Найти товар по названию.
# 6. Вывести список товаров меньше определнной стоимости.
# 7. Вывести список товаров меньше определенного количества.
