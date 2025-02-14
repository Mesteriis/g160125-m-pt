# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.

file_d = open('./text_files/data.txt')
content = file_d.read()
print(content)
file_d.seek(0)
partial_content = file_d.read(10)
print(partial_content)
file_d.seek(0)
one_line = file_d.readline()
print(one_line)
file_d.seek(0)
all_lines = file_d.readlines()
print(all_lines)
file_d.seek(0)
file_d.close()

# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.

file_d = open ('./homework_files/output.txt', 'w')
file_d.write("Hello, World!\n")
# print(file_d)
file_d.close()
file_d = open ('./homework_files/output.txt')
file_d_content = file_d.read()
print(file_d_content)
file_d_new_lines = ["This is Line 1\n", "This is Line 2\n"]
print(file_d_new_lines)
file_d.close()
# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
file_l = open ('./homework_files/log.txt', 'w')
file_l.write ("New log entry\n")
lines_to_append = ["Log entry 1\n", "Log entry 2\n"]
file_l.writelines(lines_to_append)
file_l.close()
file_l = open('./homework_files/log.txt')
file_l_content = file_l.read()
print(file_l_content)
file_l.close()



# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.
file_p = open("./homework_files/pointer_example.txt", 'w')
file_p.close()
file_p = open("./homework_files/pointer_example.txt", 'r+')
file_p.write("Python File Handling\n")
file_p.seek(0)
# file_p.read()
file_p_first_line = file_p.readline()
print(file_p_first_line)
file_p.seek(7)
part_content = file_p.read(5)
print(part_content)
file_p.seek(0, 2)
file_p.write("End of file\n")
file_p.seek(0)
full_file_p_content = file_p.read()
print(full_file_p_content)




# Тема: Менеджер контекста и JSON

# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.
import json
data = {
    "name": "Igor",
    "age": 42,
    "City": "Chicago"
}
with open("./homework_files/user.json", "w") as j_file:#
    json.dump(data, j_file,indent=4)
with open("./homework_files/user.json", "r") as j_file:
    datar = json.load(j_file)
    print(datar)



# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON
# с использованием менеджера контекста.
with open("./homework_files/user.json", "r") as j_file:
    data = json.load(j_file)
    data ["age"] = 29
with open("./homework_files/user.json", "w") as j_file:
    json.dump(data, j_file)
with open("./homework_files/user.json", "r") as j_file:
    print (json.load(j_file))


# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
with open("./homework_files/user.json", "r") as file:
    users = json.load(file)
    users = [users]
    print(users)
    new_user = {
    "name": "Billie",
    "age": 64,
    "City": "Jean"
}
    users.append(new_user)
with open("./homework_files/user.json", "w") as file:
    json.dump(users, file, indent=4)
with open("./homework_files/user.json", "r") as file:
    print(json.load(file))


# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
with open("./homework_files/user.json", "r") as file:
    content = json.load(file)
    print(content)
    content_to_del = content.pop()
    print(content_to_del)
with open("./homework_files/user.json", "w") as file:
    json.dump(content_to_del, file)
with open("./homework_files/user.json", "r") as file:
    print(json.load(file))




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

# inventory = [
#     {'product': "Laptop", 'price': 10, 'count': 13},
#     {'product': "Mouse", 'price': 50, 'count': 1},
#     {'product': "Keyboard", 'price': 30, 'count': 33},
#     {'product': "Monitor", 'price': 20, 'count': 10}
# ]
def save_inventory(inventory):
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file)

def load_inventory():
    with open('inventory.json') as file:
        return json.load(file)

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

