# Тема: Обработка исключений (try/except/else/finally)

# Задача 1: Деление чисел
# Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# Обработайте исключения для случаев, когда:
# - деление на ноль
# - ввод не числовых значений.
#
# def divide_numbers(a, b):
#     try:
#         result = float(a) / float(b)
#     except ZeroDivisionError:
#         return "Ошибка: деление на ноль!"
#     except ValueError:
#         return "Ошибка: введены некорректные данные!"
#     else:
#         return f"Результат: {result}"
#     finally:
#         print("Операция деления завершена.")
#
# print(divide_numbers(10, 2))
# print(divide_numbers(10, 0))
# print(divide_numbers(10, "a"))

# Задача 2: Обработка пользовательского ввода
# Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# Обработайте исключения для случаев, когда ввод не является числом.

# def get_square():
#     try:
#         number = float(input("Введите число: "))
#         print(f"Квадрат числа: {number ** 2}")
#     except ValueError:
#         print("Ошибка: Введите корректное число.")
#
# get_square()


# Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# Проверьте, что ошибки обрабатываются на примере FileNotFoundError.

# try:
#     with open("exercise_1.txt", "r", encoding="utf-8") as file:
#         content = file.read()
#         print("Содержимое файла:")
#         print(content)
# except FileNotFoundError:
#     print("Ошибка: Файл не найден. Проверьте, существует ли файл exercise_1.txt.")
# except PermissionError:
#     print("Ошибка: Недостаточно прав для чтения файла.")
# except IOError:
#     print("Ошибка: Произошла ошибка ввода-вывода при работе с файлом.")


# Тема: Расространение исключения. Возбуждение исключения.

# Задача 1. Допишите код ниже.
#
# import math
#
# def calculate_square_root(number):
#     # Добавьте проверку на отрицательное число и возбуждение исключения
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

# import math
#
# def calculate_square_root(number):
#     if number < 0:
#         raise ValueError("Число должно быть положительным")
#     return math.sqrt(number)
#
# def safe_calculate_square_root(number):
#     try:
#         result = calculate_square_root(number)
#         print(f"Квадратный корень из {number} равен {result}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# safe_calculate_square_root(25)
# safe_calculate_square_root(-9)

# Задача 2. Допишите код ниже.
# def convert_to_number(string):
#     # Добавьте проверку на некорректное значение и возбуждение исключения
#
#     return int(string)
#
# def safe_convert_to_number(string):
#     try:
#         number = convert_to_number(string)
#         print(f"Конвертированное число: {number}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# # Тесты функции
# safe_convert_to_number("123")  # Ожидаемый результат: Конвертированное число: 123
# safe_convert_to_number("abc")  # Ожидаемый результат: Ошибка: Введенное значение не является числом

# def convert_to_number(string):
#     if not string.isdigit():
#         raise ValueError("Введенное значение не является числом")
#     return int(string)
#
# def safe_convert_to_number(string):
#     try:
#         number = convert_to_number(string)
#         print(f"Конвертированное число: {number}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# safe_convert_to_number("123")
# safe_convert_to_number("abc")

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

# import json
#
# DB_FILE = "inventory.json"
#
# def load_inventory():
#     try:
#         with open(DB_FILE, "r", encoding="utf-8") as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return {}
#
# def save_inventory(inventory):
#     with open(DB_FILE, "w", encoding="utf-8") as file:
#         json.dump(inventory, file, indent=4, ensure_ascii=False)
#
# def show_inventory(inventory):
#     print("Инвентарь пуст." if not inventory else "\n".join(f"{k}: {v['price']}€, {v['quantity']} шт." for k, v in inventory.items()))
#
# def add_product(inventory):
#     name = input("Название: ")
#     if name in inventory:
#         print("Товар уже существует.")
#         return
#     try:
#         inventory[name] = {"price": float(input("Цена: ")), "quantity": int(input("Количество: "))}
#         save_inventory(inventory)
#     except ValueError:
#         print("Ошибка ввода.")
#
# def remove_product(inventory):
#     inventory.pop(input("Название: "), None) or print("Товар не найден.")
#     save_inventory(inventory)
#
# def update_product(inventory):
#     name = input("Название: ")
#     if name not in inventory:
#         print("Товар не найден.")
#         return
#     try:
#         inventory[name] = {"price": float(input("Новая цена: ") or inventory[name]['price']), "quantity": int(input("Новое количество: ") or inventory[name]['quantity'])}
#         save_inventory(inventory)
#     except ValueError:
#         print("Ошибка ввода.")
#
# def search_product(inventory):
#     print(inventory.get(input("Название: "), "Товар не найден."))
#
# def filter_products(inventory, key, prompt):
#     try:
#         value = float(input(prompt))
#         show_inventory({k: v for k, v in inventory.items() if v[key] < value})
#     except ValueError:
#         print("Ошибка ввода.")
#
# def main():
#     inventory = load_inventory()
#     actions = {
#         "1": show_inventory,
#         "2": add_product,
#         "3": remove_product,
#         "4": update_product,
#         "5": search_product,
#         "6": lambda inv: filter_products(inv, "price", "Максимальная цена: "),
#         "7": lambda inv: filter_products(inv, "quantity", "Максимальное количество: ")
#     }
#     while (choice := input("\nМеню:\n1. Показать\n2. Добавить\n3. Удалить\n4. Обновить\n5. Найти\n6. Дешевле\n7. Меньше\n8. Выход\nВыбор: ")) != "8":
#         actions.get(choice, lambda _: print("Ошибка ввода."))(inventory)
#
# if __name__ == "__main__":
#     main()







