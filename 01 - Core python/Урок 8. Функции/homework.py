# # Задача 1: Анализ чисел
# # Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# # и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
# # #
# # numbers = [1, 2, 3, 4, 5, 6]
# # # Вывод функции: (21, 3.5, 3)
# # def analyze_numbers(numbers):
# #     total_sum = sum(numbers)
# #     average = sum(numbers) / len(numbers)
# #     chet_numbers = sum(1 for num in numbers if num % 2 == 0)
# #     return total_sum, average, chet_numbers
# # print(analyze_numbers(numbers))
#
# # Задача 2: Работа со строками
# # Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# # # и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
# # #
# # def analyze_strings(strings):
# #     if not strings:
# #         return None, None, 0
# #
# #     big_string = strings[0]
# #     small_string = strings[0]
# #     letter_count = 0
# #
# #     for s in strings:
# #         if len(s) > len(big_string):
# #             big_string = s
# #         if len(s) < len(small_string):
# #             small_string = s
# #         if "a" in s:
# #             letter_count += 1
# #
# #     return big_string, small_string, letter_count
# #
# #
# # strings = ["apple", "banana", "cherry", "date"]
# # print(analyze_strings(strings))
#
# # Задача 3: Обработка словаря сотрудников
# # Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# # возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
# #
# # # employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# # # Вывод функции: (6000.0, 7000, 'Bob')
# # def analyze_salaries(employees):
# #     if not employees:
# #         return 0, 0, None
# #
# #     total_salary = sum(employees.values())
# #     average_salary = total_salary / len(employees)
# #
# #     max_employee = max(employees, key=employees.get)
# #     max_salary = employees[max_employee]
# #
# #     return average_salary, max_salary, max_employee
# #
# #
# # employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# # print(analyze_salaries(employees))
#
#
# # Задача 4: Фильтрация списка
# # Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# # возвращает кортеж из двух списков: четные числа и нечетные числа.
# #
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
# # def filter_numbers(numbers):
# #     even_numbers = [num for num in numbers if num % 2 == 0]
# #     odd_numbers = [num for num in numbers if num % 2 != 0]
# #     return even_numbers, odd_numbers
# #
# #
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(filter_numbers(numbers))
# #
#
# # Задача 5: Генерация словаря
# # Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# # и возвращает словарь, где ключи из первого списка, а значения из второго.
# #
# # keys = ["name", "age", "city"]
# # values = ["Alice", 30, "New York"]
# # Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# # def create_dict(keys, values):
# #     return dict(zip(keys, values))
# #
# #
# # keys = ["name", "age", "city"]
# # values = ["Alice", 30, "New York"]
# # print(create_dict(keys, values))
#
#
# # Задача 6: Подсчет символов в строке
# # Напишите функцию `count_characters(string)`, которая принимает строку и
# # возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
# #
# # # string = "hello world"
# # # Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# # def count_characters(string):
# #     char_count = {}
# #     for char in string:
# #         char_count[char] = char_count.get(char, 0) + 1
# #     return char_count
# #
# #
# # string = "hello world"
# # print(count_characters(string))
#
#
# # Задача 7: Обработка произвольного числа аргументов
# # Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# # и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
# #
# # sum_positive_negative(1, -2, 3, -4, 5)
# # # Вывод функции: (9, -6)
# # def sum_positive_negative(*args):
# #     positive_sum = sum(num for num in args if num > 0)
# #     negative_sum = sum(num for num in args if num < 0)
# #     return positive_sum, negative_sum
# #
# #
# # print(sum_positive_negative(1, -2, 3, -4, 5))
#
#
# # Задача 8: Генерация строки из именованных аргументов
# # Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
# #
# # generate_string(name="Alice", age=30, city="New York")
# # Вывод функции: name=Alice, age=30, city=New York
# # def generate_string(**kwargs):
# #     return ", ".join(f"{key}={value}" for key, value in kwargs.items())
# #
# #
# # print(generate_string(name="Alice", age=30, city="New York"))
#
#
# # Проект: Перепишите проект из урока 7 в функциональном стиле.
# # Управление инвентарем в интернет-магазине
# # Разработайте программу для управления инвентарем интернет-магазина.
# # Программа должна позволять добавлять новые товары и удалять имеющиеся,
# # обновлять наименование, цену и количество существующих товаров,
# # искать товары по названию, выводить список всех товаров и их количество,
# # а также выводить товары с количеством ниже заданного значения стоимости и количества.
# #
# # Меню:
# # 1. Показать список товаров.
# # 2. Добавить товар.
# # 3. Удалить товар.
# # 4. Обновить название товара, стоимость или количество.
# # 5. Найти товар по названию.
# # 6. Вывести список товаров меньше определнной стоимости.
# # 7. Вывести список товаров меньше определенного количества.
#
# # inventory = [
# #     {'product': "Laptop", 'price': 10, 'count': 13},
# #     {'product': "Mouse", 'price': 50, 'count': 1},
# #     {'product': "Keyboard", 'price': 30, 'count': 33},
# #     {'product': "Monitor", 'price': 20, 'count': 10}
# # ]
#
# def show_inventory(inventory):
#     if not inventory:
#         print("Инвентарь пуст.")
#     else:
#         for item in inventory:
#             print(f"{item['product']}: {item['price']}$, Количество: {item['count']}")
#
# def add_product(inventory, product, price, count):
#     if any(item["product"] == product for item in inventory):
#         print(f"Товар '{product}' уже существует.")
#         return inventory
#     return inventory + [{"product": product, "price": price, "count": count}]
#
# def remove_product(inventory, product):
#     new_inventory = [item for item in inventory if item["product"] != product]
#     if len(new_inventory) == len(inventory):
#         print(f"Товар '{product}' не найден.")
#     return new_inventory
#
# def update_product(inventory, product, new_name=None, new_price=None, new_count=None):
#     def update_item(item):
#         if item["product"] == product:
#             return {
#                 "product": new_name if new_name else item["product"],
#                 "price": new_price if new_price is not None else item["price"],
#                 "count": new_count if new_count is not None else item["count"],
#             }
#         return item
#
#     updated_inventory = list(map(update_item, inventory))
#     if inventory == updated_inventory:
#         print(f"Товар '{product}' не найден.")
#     return updated_inventory
#
# def find_product(inventory, product):
#     found = next((item for item in inventory if item["product"] == product), None)
#     return found if found else f"Товар '{product}' не найден."
#
# def filter_by_price(inventory, max_price):
#     return list(filter(lambda item: item["price"] < max_price, inventory))
#
# def filter_by_count(inventory, max_count):
#     return list(filter(lambda item: item["count"] < max_count, inventory))
#
# inventory = [
#     {"product": "Laptop", "price": 1000, "count": 13},
#     {"product": "Mouse", "price": 50, "count": 1},
#     {"product": "Keyboard", "price": 30, "count": 33},
#     {"product": "Monitor", "price": 200, "count": 10},
# ]
#
# while True:
#     print("\nМеню:")
#     print("1. Показать список товаров")
#     print("2. Добавить товар")
#     print("3. Удалить товар")
#     print("4. Обновить товар")
#     print("5. Найти товар")
#     print("6. Вывести список товаров дешевле заданной цены")
#     print("7. Вывести список товаров с количеством меньше заданного")
#     print("8. Выйти")
#
#     choice = input("Выберите действие: ")
#
#     match choice:
#         case "1":
#             show_inventory(inventory)
#         case "2":
#             name = input("Введите название товара: ")
#             price = float(input("Введите цену товара: "))
#             count = int(input("Введите количество товара: "))
#             inventory = add_product(inventory, name, price, count)
#         case "3":
#             name = input("Введите название товара для удаления: ")
#             inventory = remove_product(inventory, name)
#         case "4":
#             name = input("Введите название товара для обновления: ")
#             new_name = input("Введите новое название (Enter - оставить прежним): ") or None
#             new_price = input("Введите новую цену (Enter - оставить прежнюю): ")
#             new_price = float(new_price) if new_price else None
#             new_count = input("Введите новое количество (Enter - оставить прежнее): ")
#             new_count = int(new_count) if new_count else None
#             inventory = update_product(inventory, name, new_name, new_price, new_count)
#         case "5":
#             name = input("Введите название товара для поиска: ")
#             result = find_product(inventory, name)
#             print(result)
#         case "6":
#             max_price = float(input("Введите максимальную цену: "))
#             result = filter_by_price(inventory, max_price)
#             show_inventory(result)
#         case "7":
#             max_count = int(input("Введите максимальное количество: "))
#             result = filter_by_count(inventory, max_count)
#             show_inventory(result)
#         case "8":
#             print("Выход из программы.")
#             break
#         case _:
#             print("Неверный ввод. Попробуйте снова.")
#
#
