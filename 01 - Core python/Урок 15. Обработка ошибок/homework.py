# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.
# def num_divide(x, y):
#     try:
#         result = x / y
#         print(result)
#     except ValueError as a:
#         print(f"Value error!{a}")
#     except ZeroDivisionError as b:
#         print(f"Error! {b}")
#         return None
#
# num_divide(20, 0)

# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.
# def quadro():
#     try:
#         user_input = float(input("Enter your number: "))
#         result = user_input ** 2
#         print(f"Result is: {result}")
#     except ValueError as a:
#         print(f"Your input isnot a number! - {a}")
#
# quadro()


# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.
# try:
#     file_d = open('./text_files/data.txt')
#     content = file_d.read()
#     file_d.seek(0)
#     part_content = file_d.read(10)
#     file_d.seek(0)
#     str_content = file_d.readline()
#     file_d.seek(0)
#     all_str_content = file_d.readlines()
#     print(all_str_content)
#     file_d.close()
#
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("No access to file")
# except IOError:
#     print("Incorrect input"

# Тема: Расространение исключения. Возбуждение исключения.

# Задача 1. Допишите код ниже.
#
import math

# def calculate_square_root(number):
#     if number < 0:
#         raise ValueError(f"{number} is negative!")
#
#     return math.sqrt(number)
#
# def safe_calculate_square_root(number):
#     try:
#         result = calculate_square_root(number)
#         print(f"Квадратный корень из {number} равен {result}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# # Тесты функции
# safe_calculate_square_root(25)  # Ожидаемый результат: Квадратный корень из 25 равен 5.0
# safe_calculate_square_root(-9)  # Ожидаемый результат: Ошибка: Число должно быть положительным


# Задача 2. Допишите код ниже.
# def convert_to_number(string):
#     if not string.isnumeric():
#         raise ValueError(f"Entered value '{string}' is not number!")
#
#     return int(string)
#
# def safe_convert_to_number(string):
#     try:
#         number = convert_to_number(string)
#         print(f"Конвертированное число: {number}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
# #
# # # Тесты функции
# safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
# safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом


# Тема: Интеграционная практика. Мини-проект

 # Тема: Интеграционная практика. Мини-проект
import json

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


from json import JSONDecodeError

def save_inventory(inventory):
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file)


def load_inventory():
    try:
        with open('inventory.json') as file:
            return json.load(file)
    except (FileNotFoundError, IOError, JSONDecodeError) as e:
        print(f"Ошибка: {e}")
        return []


def show_inventory(inventory):
    for product in inventory:
        print_product(product)

def add_product(inventory):
    product = input("Enter product name: ")
    try:
        price = int(input("Enter product price: "))
        count = int(input("Enter product count: "))
    except ValueError as e:
        print(f"Ошибка: {e}")
        return add_product(inventory)
    inventory.append({'product': product.title(), 'price': price, 'count': count})
    return inventory

def remove_product(inventory):
    product = input("Enter product name: ")
    for item in inventory:
        if item['product'].lower() == product.lower():
            inventory.remove(item)
    return inventory

def edit_product(inventory):
    product = input("Enter product name: ")
    for item in inventory:
        if item['product'].lower() == product.lower():
            try:
                new_product = input(f"Enter new product name or {item['product']}: ")
                if new_product:
                    item['product'] = new_product.title()
                new_price = input(f"Enter new product price or {item['price']}: ")
                if new_price:
                    item['price'] = int(new_price) * 0.1
                new_count = input(f"Enter new product count or {item['count']}: ")
                if new_count:
                    item['count'] = int(new_count)
            except ValueError as e:
                print(f"Ошибка: {e}")
                return edit_product(inventory)
    return inventory

def find_product(inventory):
    product = input("Enter product name: ")
    for item in inventory:
        if item['product'].lower() == product.lower():
            print_product(item)

def find_product_min_cost(inventory):
    try:
        price = int(input("Enter price: "))
    except ValueError as e:
        print(f"Ошибка: {e}")
        return find_product_min_cost(inventory)
    for item in inventory:
        if item['price'] <= price:
            print_product(item)

def print_product(product):
    print(f"Product: {product['product']} Price: {product['price']} Count: {product['count']}")

def find_product_min_count(inventory):
    try:
        count = int(input("Enter count: "))
    except ValueError as e:
        print(f"Ошибка: {e}")
        return find_product_min_count(inventory)
    for item in inventory:
        if item['count'] <= count:
            print_product(item)

while True:
    inventory = load_inventory()
    user_input = input(
        "1. Показать список товаров.\n"
        "2. Добавить товар.\n"
        "3. Удалить товар.\n"
        "4. Обновить название товара, стоимость или количество.\n"
        "5. Найти товар по названию.\n"
        "6. Вывести список товаров меньше определнной стоимости.\n"
        "7. Вывести список товаров меньше определенного количества.\n"
        "8. Выйти.\n"
    )
    match user_input:
        case "1":
            show_inventory(inventory)
        case "2":
            inventory = add_product(inventory)
            save_inventory(inventory)
        case "3":
            inventory = remove_product(inventory)
            save_inventory(inventory)
        case "4":
            inventory = edit_product(inventory)
            save_inventory(inventory)
        case "5":
            find_product(inventory)
        case "6":
            find_product_min_cost(inventory)
        case "7":
            find_product_min_count(inventory)
        case "8":
            break
        case _:
            print("Invalid input")








