# Тема: Чтение и запись данных в файл.
import json

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.

# file_data = open("./text_files/data.txt", "r")
# content = file_data.read()                                      #1,2
# # print(content)
#
# file_data.seek(0)
# first_part_content = file_data.read(10)                         #3
# # print(first_part_content)
#
# file_data.seek(0)
# str_content = file_data.readline()                              #4
# # print(str_content)
#
# file_data.seek(0)
# all_content = file_data.read()                                  #5
# # print(all_content)

# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.

# file_output = open("./text_files/output.txt", "a")                  #1
# file_output.write("Hello world!\n")                                   #2
#
# str_add = ["This is line 1\n", "This is line 2\n"]                  #3
# file_output.writelines(str_add)
#
# file_output.close()                                                 #4
#
# file_output = open("./text_files/output.txt", "r")                  #5
# all_content = file_output.read()
# print(all_content)

# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
# file_log = open("./text_files/log.txt", "a")                        #1
#
# file_log.write("New log entry\n")                                   #2
#
# add_strings = ["Log entry 1\n", "Log entry 2\n"]                    #3
# file_log.writelines(add_strings)
#
# file_log.close()                                                    #4
#
# file_log = open("./text_files/log.txt", "r")
# all_content = file_log.read()                                       #5
# print(all_content)

# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.

# file_pointer = open("./text_files/pointer_example.txt", "a+")        #1
#
# file_pointer.write("Python File Handling\n")                        #2
#
# file_pointer.seek(0)
# file_pointer.readline()                                             #3
#
# file_pointer.seek(7)
# file_pointer.read(5)                                                #4
#
# file_pointer.seek(0,2)
# file_pointer.write("End of file\n")                                 #5
#
# file_pointer.seek(0)
# all_data = file_pointer.read()
# print(all_data)                                                     #6

# Тема: Менеджер контекста и JSON

# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.
users = {
    'name': "Ivan",
    'age': 35,                                              #1
    'city': "Berlin"
}
with open("./text_files/user.json", "w") as file:                #2
    json.dump(users, file)

with open("./text_files/user.json") as file:
    data = json.load(file)                                          #3
    # print(data)

# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.
with open("./text_files/user.json", "r") as file:
    json.load(file)                                                 #1
    users["age"] = 29                                               #2

with open("./text_files/user.json", "w") as file:
    json.dump(users, file)

with open("./text_files/user.json") as file:
    correct = json.load(file)
    # print(correct)                                                  #3


# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
with open("./text_files/user.json") as file:
    data = json.load(file)
    users = [users]
    new_user = {"name": "Vasyl", "age": 40, "city": "Dresden"}                #1
    users.append(new_user)

with open("./text_files/user.json", "w") as file:                              #2
    json.dump(users, file)

with open("./text_files/user.json") as file:
    new_file = json.load(file)                                                  #3
    print(new_file)

# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
with open("./text_files/user.json", "r") as file:
    delete_user = json.load(file)                                   #1
    delete_user.pop()

with open("./text_files/user.json", "w") as file:                   #2
    json.dump(delete_user, file)

with open("./text_files/user.json") as file:
    delete_user = json.load(file)                                   #3
    print(delete_user)

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
import  json
inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]


def save_inventory(inventory):

    file = open("inventory.json", "w")
    json.dump(inventory, file)
    file.close()

def load_inventory(inventory):

    file = open("inventory.json", "r")
    inventory = json.load(file)
    file.close()
    return inventory



def show_inventory(inventory):
    for product in inventory:
        print_product(product)

def add_product(inventory):
    product = input("Enter product name: ")
    price = int(input("Enter product price: "))
    count = int(input("Enter product count: "))
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
            new_product = input(f"Enter new product name or {item['product']}: ")
            if new_product:
                item['product'] = new_product.title()
            new_price = input(f"Enter new product price or {item['price']}: ")
            if new_price:
                item['price'] = int(new_price) * 0.1
            new_count = input(f"Enter new product count or {item['count']}: ")
            if new_count:
                item['count'] = int(new_count)
    return inventory

def find_product(inventory):
    product = input("Enter product name: ")
    for item in inventory:
        if item['product'].lower() == product.lower():
            print_product(item)

def find_product_min_cost(inventory):
    price = int(input("Enter price: "))
    for item in inventory:
        if item['price'] <= price:
            print_product(item)

def print_product(product):
    print(f"Product: {product['product']} Price: {product['price']} Count: {product['count']}")

def find_product_min_count(inventory):
    count = int(input("Enter count: "))
    for item in inventory:
        if item['count'] <= count:
            print_product(item)

while True:
    inventory = load_inventory(inventory)
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