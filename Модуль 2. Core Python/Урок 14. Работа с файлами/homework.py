# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.

# file_r = open("data.txt")  # Режим чтения по умолчанию
# file_r = open("data.txt", "r")  # Явно указанный режим чтения
#
# file = open("data.txt", "r")
#
# content = file.read()
# print("Содержимое файла:\n", content)
#
# file.seek(0)
# partial_content = file.read(10)
# print("\nПервые 10 символов файла:", partial_content)
#
# file.seek(0)
# one_line = file.readline()
# print("\nПервая строка файла:", one_line.strip())
#
# file.seek(0)
# all_lines = file.readlines()
# print("\nСписок всех строк файла:")
# for line in all_lines:
#     print(line.strip())
#
# file.close()


# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.

# file_w = open("output.txt", "w")
#
# file_w.write("Hello, World!\n")
#
# lines = ["This is line 1\n", "This is line 2\n"]
# file_w.writelines(lines)
#
# file_w.close()
#
# file_r = open("output.txt", "r")
#
# content = file_r.read()
# print("Содержимое файла:\n", content)
#
# file_r.close()


# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.

# file_a = open("log.txt", "a")
#
# file_a.write("New log entry\n")
#
# log_lines = ["Log entry 1\n", "Log entry 2\n"]
# file_a.writelines(log_lines)
#
# file_a.close()
#
# file_r = open("log.txt", "r")
# content = file_r.read()
# print("Содержимое файла:\n", content)
#
# file_r.close()


# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.

# file = open("pointer_example.txt", "w+")
#
# file.write("Python File Handling\n")
#
# file.seek(0)
# first_line = file.readline()
# print("Первая строка:", first_line.strip())
#
# file.seek(7)
# five_chars = file.read(5)
# print("Символы с позиции 7:", five_chars)
#
# file.seek(0, 2)
# file.write("End of file\n")
#
# file.seek(0)
# full_content = file.read()
# print("Полное содержимое файла:\n", full_content)
#
# file.close()


# Тема: Менеджер контекста и JSON

# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.

# import json
#
# user_data = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }
#
# with open("user.json", "w", encoding="utf-8") as file:
#     json.dump(user_data, file, ensure_ascii=False, indent=4)
#
# with open("user.json", "r", encoding="utf-8") as file:
#     loaded_data = json.load(file)
#     print("Данные из файла:", loaded_data)


# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.

# import json
#
# with open("user.json", "r", encoding="utf-8") as file:
#     user_data = json.load(file)
#
# user_data["age"] = 29
#
# with open("user.json", "w", encoding="utf-8") as file:
#     json.dump(user_data, file, ensure_ascii=False, indent=4)
#
# print("Данные обновлены:", user_data)


# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.

# import json
#
# with open("users.json", "r", encoding="utf-8") as file:
#     users_data = json.load(file)
#
# new_user = {
#     "name": "Alice Smith",
#     "age": 25,
#     "city": "Los Angeles"
# }
# users_data.append(new_user)
#
# with open("users.json", "w", encoding="utf-8") as file:
#     json.dump(users_data, file, ensure_ascii=False, indent=4)
#
# print("Новый пользователь добавлен:", new_user)


# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.

# import json
#
# with open("users.json", "r", encoding="utf-8") as file:
#     users_data = json.load(file)
#
# user_to_remove = "Alice Smith"
# users_data = [user for user in users_data if user["name"] != user_to_remove]
#
# with open("users.json", "w", encoding="utf-8") as file:
#     json.dump(users_data, file, ensure_ascii=False, indent=4)
#
# print(f"Пользователь {user_to_remove} был удален.")


# Тема: Интеграционная практика. Мини-проект

# Проект: Перепишите проект из уроков 7-8 с записью, чтением, обновлением и удалением товаров в файле (через JSON).
# Используйте файл как базу данных проекта.
#
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
#
# def load_inventory():
#     try:
#         with open("inventory.json", "r", encoding="utf-8") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []  # Возвращаем пустой список, если файл не существует
#
#
# def save_inventory(inventory):
#     with open("inventory.json", "w", encoding="utf-8") as file:
#         json.dump(inventory, file, ensure_ascii=False, indent=4)
#
#
# def show_inventory(inventory):
#     if inventory:
#         print("\nСписок товаров:")
#         for idx, item in enumerate(inventory, 1):
#             print(f"{idx}. {item['product']} - Цена: {item['price']} - Количество: {item['count']}")
#     else:
#         print("\nТовары отсутствуют в базе.")
#
#
# def add_product(inventory):
#     product_name = input("Введите название товара: ")
#     price = float(input("Введите цену товара: "))
#     count = int(input("Введите количество товара: "))
#     inventory.append({"product": product_name, "price": price, "count": count})
#     save_inventory(inventory)
#     print(f"\nТовар '{product_name}' добавлен в инвентарь.")
#
#
# def remove_product(inventory):
#     product_name = input("Введите название товара для удаления: ")
#     inventory = [item for item in inventory if item['product'].lower() != product_name.lower()]
#     save_inventory(inventory)
#     print(f"\nТовар '{product_name}' удален из инвентаря.")
#
#
# def update_product(inventory):
#     product_name = input("Введите название товара для обновления: ")
#     for item in inventory:
#         if item['product'].lower() == product_name.lower():
#             print(f"\nТекущие данные: Название: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
#             item['product'] = input("Введите новое название товара: ")
#             item['price'] = float(input("Введите новую цену товара: "))
#             item['count'] = int(input("Введите новое количество товара: "))
#             save_inventory(inventory)
#             print(f"\nТовар '{item['product']}' обновлен.")
#             return
#     print("Товар не найден.")
#
#
# def search_product(inventory):
#     product_name = input("Введите название товара для поиска: ")
#     found_products = [item for item in inventory if product_name.lower() in item['product'].lower()]
#     if found_products:
#         print("\nНайденные товары:")
#         for item in found_products:
#             print(f"{item['product']} - Цена: {item['price']} - Количество: {item['count']}")
#     else:
#         print("Товары не найдены.")
#
#
# def filter_by_price(inventory):
#     price_limit = float(input("Введите цену для фильтрации товаров: "))
#     filtered_products = [item for item in inventory if item['price'] < price_limit]
#     if filtered_products:
#         print("\nТовары с ценой ниже заданной:")
#         for item in filtered_products:
#             print(f"{item['product']} - Цена: {item['price']} - Количество: {item['count']}")
#     else:
#         print("Товары не найдены.")
#
#
# def filter_by_count(inventory):
#     count_limit = int(input("Введите количество для фильтрации товаров: "))
#     filtered_products = [item for item in inventory if item['count'] < count_limit]
#     if filtered_products:
#         print("\nТовары с количеством ниже заданного:")
#         for item in filtered_products:
#             print(f"{item['product']} - Цена: {item['price']} - Количество: {item['count']}")
#     else:
#         print("Товары не найдены.")
#
#
# def main():
#     inventory = load_inventory()
#
#     while True:
#         print("\nМеню:")
#         print("1. Показать список товаров")
#         print("2. Добавить товар")
#         print("3. Удалить товар")
#         print("4. Обновить товар")
#         print("5. Найти товар по названию")
#         print("6. Вывести товары меньше определенной стоимости")
#         print("7. Вывести товары меньше определенного количества")
#         print("8. Выход")
#
#         choice = input("Выберите опцию: ")
#
#         if choice == "1":
#             show_inventory(inventory)
#         elif choice == "2":
#             add_product(inventory)
#         elif choice == "3":
#             remove_product(inventory)
#         elif choice == "4":
#             update_product(inventory)
#         elif choice == "5":
#             search_product(inventory)
#         elif choice == "6":
#             filter_by_price(inventory)
#         elif choice == "7":
#             filter_by_count(inventory)
#         elif choice == "8":
#             print("Выход из программы.")
#             break
#         else:
#             print("Некорректный выбор. Попробуйте снова.")
#
#
# if __name__ == "__main__":
#     main()
