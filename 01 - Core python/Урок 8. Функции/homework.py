# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)
from functools import total_ordering
from itertools import count

# def analyze_numbers(numbers):
#
#     total_sum = sum(numbers)
#
#     avarage_num = sum(numbers) / len(numbers)
#
#     count_even = 0
#     for num in numbers:
#         if num % 2 == 0:
#             count_even += 1
#
#     return total_sum, avarage_num, count_even
#
# print(analyze_numbers(numbers))

# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
# strings = ["apple", "banana", "cherry", "date"]
# Вывод функции: ('banana', 'date', 3)

# def analyze_strings(strings):
#     max_len = ""
#     min_len = ""
#     count_a = 0
#     for string in strings:
#         if len(string) > len(max_len):
#             max_len = string
#         if len(string) < len(max_len):
#             min_len = string
#         if "a" in string:
#             count_a += 1
#
#     return max_len, min_len, count_a
# print(analyze_strings(strings))


# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# # Вывод функции: (6000.0, 7000, 'Bob')
#
# def analyze_salaries(employees):
#     total_salary = sum(employees.values())
#     quan_employ = len(employees)
#     avag_salary = total_salary / quan_employ
#
#     max_salary = max(employees.values())
#     max_salary_emp = ""
#
#     max_salary_emp = max(employees, key=employees.get)
#     max_salary = employees[max_salary_emp]
#
#     return avag_salary, max_salary, max_salary_emp
#
# print(analyze_salaries(employees))

# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])

# def filter_numbers(numbers):
#     even_num = []
#     odd_num = []
#
#     for num in numbers:
#         if num % 2 == 0:
#             even_num.append(num)
#         else:
#             odd_num.append(num)
#
#     return even_num, odd_num
#
# print(filter_numbers(numbers))

# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# # Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}
#
# def create_dict(keys, values):
#
#     comb = dict(zip(keys, values))
#
#     return comb
# print(create_dict(keys, values))

# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# def count_characters(string):
#     words_count = {}
#     for word in string:
#         if word in words_count:
#             words_count[word] += 1
#         else:
#             words_count[word] = 1
#
#     return words_count
# print(count_characters(string))


# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
# #
# sum_positive_negative = (1, -2, 3, -4, 5)
# Вывод функции: (9, -6)

# def sum_positive_negative(*args):
#     sum_pos = 0
#     sum_neg = 0
#     for num in args:
#
#         if num > 0:
#             sum_pos += num
#
#         else:
#             sum_neg < 0
#             sum_neg += num
#
#     return sum_neg, sum_pos
# print(sum_positive_negative(1, -2, 3, -4, 5))


# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string = (name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York

# def generate_string(**kwargs):
#
#     return
# print(generate_string(name="Alice", age=30, city="New York"))

# Проект: Перепишите проект из урока 7 в функциональном стиле.
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
# 6. Вывести список товаров меньше определенной стоимости.
# 7. Вывести список товаров меньше определенного количества.

# inventory = [
#     {'product': "Laptop", 'price': 10, 'count': 13},
#     {'product': "Mouse", 'price': 50, 'count': 1},
#     {'product': "Keyboard", 'price': 30, 'count': 33},
#     {'product': "Monitor", 'price': 20, 'count': 10}
# ]
#
# def show_all_item(inventory):
#             for product in inventory:
#                 print(f"Product: {product['product']}, Price: {product['price']}, Count: {product['count']}")
#
# def add_new_item(inventory):
#     product = input("Enter product name: ")
#     price = int(input("Enter product price: "))
#     count = int(input("Enter product count: "))
#     inventory.append({'product': product.title(), 'price': price, 'count': count})
#
# def remove_item(inventory):
#     product = input("Enter product name: ")
#     for item in inventory:
#         if item['product'].lower() == product.lower():
#             inventory.remove(item)
#
# def update_item(inventory):
#     product = input("Enter product name: ")
#     for item in inventory:
#         if item['product'].lower() == product.lower():
#             new_product = input(f"Enter new product name or {item['product']}: ")
#             if new_product:
#                 item['product'] = new_product.title()
#         new_price = input(f"Enter new product price or {item['price']}: ")
#         if new_price:
#             item['price'] = int(new_price)
#         new_count = input(f"Enter new product count or {item['count']}: ")
#         if new_count:
#             item['count'] = int(new_count)
#
# def find_item(inventory):
#     product = input("Enter product name: ")
#     for item in inventory:
#         if item['product'].lower() == product.lower():
#             print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")
#
# def sort_by_price(inventory):
#     price = int(input("Enter price: "))
#     for item in inventory:
#         if item['price'] <= price:
#             print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")
#
# def sort_by_quantity(inventory):
#     count = int(input("Enter count: "))
#     for item in inventory:
#         if item['count'] <= count:
#             print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")
#
#
# while True:
#         user_input = input(
#         "1. Показать список товаров.\n"
#         "2. Добавить товар.\n"
#         "3. Удалить товар.\n"
#         "4. Обновить название товара, стоимость или количество.\n"
#         "5. Найти товар по названию.\n"
#         "6. Вывести список товаров меньше определенной стоимости.\n"
#         "7. Вывести список товаров меньше определенного количества.\n"
#         "8. Выйти.\n"
#     )
#         match user_input:
#             case "1":
#                 show_all_item(inventory)
#             case "2":
#                 add_new_item(inventory)
#             case "3":
#                 remove_item(inventory)
#             case "4":
#                 update_item(inventory)
#             case "5":
#                 find_item(inventory)
#             case "6":
#                 sort_by_price(inventory)
#             case "7":
#                 sort_by_quantity(inventory)
#             case "8":
#                 break
#             case _:
#                 print("Invalid input")