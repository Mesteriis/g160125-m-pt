# Тема: Модуль datetime

# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45

# from datetime import datetime
#
# current_time = datetime.now()
#
# formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_time)


# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.

# from datetime import datetime
#
# birth_date_str = input("Введите дату рождения (YYYY-MM-DD): ")
#
# birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
#
# current_date = datetime.today()
#
# age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
#
# print(f"Ваш возраст: {age} лет")

# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.

# from datetime import datetime
#
# event_date_str = input("Введите дату мероприятия (YYYY-MM-DD): ")
#
# event_date = datetime.strptime(event_date_str, "%Y-%m-%d").date()
#
# current_date = datetime.today().date()
#
# days_left = (event_date - current_date).days
#
# if days_left > 0:
#     print(f"До мероприятия осталось {days_left} дней.")
# elif days_left == 0:
#     print("Мероприятие сегодня!")
# else:
#     print("Мероприятие уже прошло.")

# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.

# from datetime import datetime
#
# date_str = input("Введите дату (YYYY-MM-DD): ")
#
# date_obj = datetime.strptime(date_str, "%Y-%m-%d")
#
# day_of_week = date_obj.strftime("%A")
# days_ru = {
#     "Monday": "Понедельник",
#     "Tuesday": "Вторник",
#     "Wednesday": "Среда",
#     "Thursday": "Четверг",
#     "Friday": "Пятница",
#     "Saturday": "Суббота",
#     "Sunday": "Воскресенье"
# }
# day_of_week_ru = days_ru[day_of_week]
#
# print(f"День недели: {day_of_week_ru}")

# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.

# from datetime import datetime
#
# date1_str = input("Введите первую дату (YYYY-MM-DD): ")
# date2_str = input("Введите вторую дату (YYYY-MM-DD): ")
#
# date1 = datetime.strptime(date1_str, "%Y-%m-%d")
# date2 = datetime.strptime(date2_str, "%Y-%m-%d")
#
# if date1 > date2:
#     print(f"Первая дата ({date1_str}) позже второй ({date2_str}).")
# elif date1 < date2:
#     print(f"Вторая дата ({date2_str}) позже первой ({date1_str}).")
# else:
#     print("Обе даты одинаковые.")

# Тема: Модуль os

# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.

# import os
#
# dir_name = "test_directory"
#
# os.mkdir(dir_name)
# print(f"Директория '{dir_name}' создана.")
#
# print("Список директорий в текущем каталоге:")
# for item in os.listdir():
#     if os.path.isdir(item):
#         print(item)
#
# os.rmdir(dir_name)
# print(f"Директория '{dir_name}' удалена.")

# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.

# import os
#
# file_name = "temp_file.txt"
# with open(file_name, "w") as file:
#     file.write("Temporary content")
#
# new_file_name = "renamed_file.txt"
# os.rename(file_name, new_file_name)
#
# print("Files in current directory:")
# print(os.listdir())

# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".

# import os
#
# filename = "example.txt"
#
# if os.path.exists(filename):
#     print(f"Размер файла: {os.path.getsize(filename)} байт")
# else:
#     print("Файл не найден")


# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".

# import os
#
#
# def compare_file_sizes(file1, file2):
#     try:
#         size1 = os.path.getsize(file1)
#         size2 = os.path.getsize(file2)
#
#         if size1 > size2:
#             print(f"Файл '{file1}' больше файла '{file2}'")
#         elif size1 < size2:
#             print(f"Файл '{file2}' больше файла '{file1}'")
#         else:
#             print("Файлы имеют одинаковый размер")
#     except FileNotFoundError as e:
#         print(f"Ошибка: {e}")
#
#
# file1 = input("Введите имя первого файла: ")
# file2 = input("Введите имя второго файла: ")
#
# compare_file_sizes(file1, file2)

# Тема: Интеграционная практика.

# Проект: Перепишите проект из уроков 7-8, 14-15, добавив в него фичи 1 - 3 на основе модулей datetime и os.
#
# Фича 1. Добавьте в каждый товар дату и время его создания,
# а также дату и время обновления данных о товаре или количества товара.
#
# Фича 2: Логирование действий с товарами
# Создайте лог-файл, куда будет записываться история всех действий с товарами (добавление, удаление, обновление).
# Используйте модуль datetime для добавления временных меток к каждому действию с товарами.
#
# Фича 3. Резервное копирование данных:
# Используйте модуль os для создания резервных копий файла с товарами.
# Например, при каждом запуске программы создается копия файла с добавлением текущей даты и времени.
#
#
# Управление инвентарем в интернет-магазине
# Разработайте программу для управления инвентарем интернет-магазина.
# Программа должна позволять добавлять новые товары и удалять имеющиеся,
# обновлять наименование, цену и количество существующих товаров,
# искать товары по названию, выводить список всех товаров и их количество,
# а также выводить товары с количеством ниже заданного значения стоимости и количества.
# Используйте файл как базу данных проекта.
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
# import os
# import shutil
# import datetime
#
# DB_FILE = "inventory.json"
# LOG_FILE = "inventory.log"
# BACKUP_DIR = "backups"
#
# def log_action(action, details=""):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(LOG_FILE, "a", encoding="utf-8") as log:
#         log.write(f"[{timestamp}] {action}: {details}\n")
#
# def create_backup():
#     if not os.path.exists(BACKUP_DIR):
#         os.makedirs(BACKUP_DIR)
#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     backup_file = os.path.join(BACKUP_DIR, f"inventory_{timestamp}.json")
#     if os.path.exists(DB_FILE):
#         shutil.copy(DB_FILE, backup_file)
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
#     return "Инвентарь пуст." if not inventory else "\n".join(
#         f"{k}: {v['price']}€, {v['quantity']} шт. (Создан: {v['created_at']}, Обновлен: {v['updated_at']})"
#         for k, v in inventory.items()
#     )
#
# def add_product(inventory, name, price, quantity):
#     if name in inventory:
#         return "Товар уже существует."
#     try:
#         price = float(price)
#         quantity = int(quantity)
#     except ValueError:
#         return "Ошибка ввода. Цена должна быть числом, а количество — целым числом."
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     inventory[name] = {
#         "price": price,
#         "quantity": quantity,
#         "created_at": timestamp,
#         "updated_at": timestamp
#     }
#     save_inventory(inventory)
#     log_action("Добавлен товар", name)
#     return "Товар добавлен."
#
# def remove_product(inventory, name):
#     if name in inventory:
#         del inventory[name]
#         save_inventory(inventory)
#         log_action("Удален товар", name)
#         return "Товар удален."
#     return "Товар не найден."
#
# def update_product(inventory, name, price=None, quantity=None):
#     if name not in inventory:
#         return "Товар не найден."
#     if price is not None:
#         try:
#             inventory[name]["price"] = float(price)
#         except ValueError:
#             return "Ошибка ввода. Цена должна быть числом."
#     if quantity is not None:
#         try:
#             inventory[name]["quantity"] = int(quantity)
#         except ValueError:
#             return "Ошибка ввода. Количество должно быть целым числом."
#     inventory[name]["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     save_inventory(inventory)
#     log_action("Обновлен товар", name)
#     return "Товар обновлен."
#
# def search_product(inventory, name):
#     return inventory.get(name, "Товар не найден.")
#
# def filter_by_price(inventory, price_limit):
#     try:
#         price_limit = float(price_limit)
#         filtered_inventory = {k: v for k, v in inventory.items() if v['price'] < price_limit}
#         return show_inventory(filtered_inventory)
#     except ValueError:
#         return "Ошибка ввода. Цена должна быть числом."
#
# def filter_by_quantity(inventory, quantity_limit):
#     try:
#         quantity_limit = int(quantity_limit)
#         filtered_inventory = {k: v for k, v in inventory.items() if v['quantity'] < quantity_limit}
#         return show_inventory(filtered_inventory)
#     except ValueError:
#         return "Ошибка ввода. Количество должно быть целым числом."
#
# def menu():
#     inventory = load_inventory()
#     while True:
#         print("\nМеню:")
#         print("1. Показать список товаров.")
#         print("2. Добавить товар.")
#         print("3. Удалить товар.")
#         print("4. Обновить название товара, стоимость или количество.")
#         print("5. Найти товар по названию.")
#         print("6. Вывести список товаров меньше определенной стоимости.")
#         print("7. Вывести список товаров меньше определенного количества.")
#         print("0. Выход.")
#
#         choice = input("Выберите пункт меню: ")
#
#         if choice == "1":
#             print(show_inventory(inventory))
#         elif choice == "2":
#             name = input("Введите название товара: ")
#             price = input("Введите цену товара: ")
#             quantity = input("Введите количество товара: ")
#             print(add_product(inventory, name, price, quantity))
#         elif choice == "3":
#             name = input("Введите название товара для удаления: ")
#             print(remove_product(inventory, name))
#         elif choice == "4":
#             name = input("Введите название товара для обновления: ")
#             price = input("Введите новую цену (или оставьте пустым): ")
#             quantity = input("Введите новое количество (или оставьте пустым): ")
#             print(update_product(inventory, name, price if price else None, quantity if quantity else None))
#         elif choice == "5":
#             name = input("Введите название товара для поиска: ")
#             print(search_product(inventory, name))
#         elif choice == "6":
#             price_limit = input("Введите максимальную стоимость: ")
#             print(filter_by_price(inventory, price_limit))
#         elif choice == "7":
#             quantity_limit = input("Введите максимальное количество: ")
#             print(filter_by_quantity(inventory, quantity_limit))
#         elif choice == "0":
#             save_inventory(inventory)
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор, попробуйте снова.")
#
# if __name__ == "__main__":
#     menu()
