# Тема: Интеграционная практика.
import json
import os
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






import time
from datetime import datetime
from json import JSONDecodeError
map_count_call = {}
DB = 'inventory.json'
DB_COPY = 'inventory_copy.json'
def retry_on_error(func):
    global map_count_call
    if func.__name__ not in map_count_call:
        map_count_call[func.__name__] = 0
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (FileNotFoundError, IOError, JSONDecodeError) as e:
            time.sleep(10)
        except Exception as e:
            print(f"Ошибка: {e}")
            map_count_call[func.__name__] += 1
            if map_count_call[func.__name__] == 3:
                print(f"Превышено количество попыток вызова функции {func.__name__}")
                exit(1)
            return wrapper(*args, **kwargs)
        else:
            map_count_call[func.__name__] = 0
    return wrapper

def log_it(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'a') as file:
            file.write(f"{datetime.now()} Вызвана функция {func.__name__}. Результат: {result}\n")
        return result
    return wrapper

@retry_on_error
def save_inventory(inventory):
    with open(DB, 'w') as file:
        for el in inventory:
            if 'created_at' in el:
                el['created_at'] = el['created_at'].isoformat()
            else:
                el['created_at'] = datetime.now().isoformat()
        json.dump(inventory, file)

@retry_on_error
def load_inventory():
    # try:1
    with open(DB) as file:
        data = json.load(file)
        for el in data:
            if 'created_at' in el:
                el['created_at'] = datetime.fromisoformat(el['created_at'])
            else:
                el['created_at'] = datetime.now()
        return data
    # except (FileNotFoundError, IOError, JSONDecodeError) as e:
    #     print(f"Ошибка: {e}")
    #     return []


def show_inventory(inventory):
    for product in inventory:
        print_product(product)
@log_it
def add_product(inventory):
    product = input("Enter product name: ")
    try:
        price = int(input("Enter product price: "))
        count = int(input("Enter product count: "))
    except ValueError as e:
        print(f"Ошибка: {e}")
        return add_product(inventory)
    inventory.append({'product': product.title(), 'price': price, 'count': count, "created_at": datetime.now()})
    return inventory
@log_it
def remove_product(inventory):
    product = input("Enter product name: ")
    for item in inventory:
        if item['product'].lower() == product.lower():
            inventory.remove(item)
    return inventory
@log_it
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
    print(f"Product: {product['product']} Price: {product['price']} Count: {product['count']} Created at: {product['created_at']}")

def find_product_min_count(inventory):
    try:
        count = int(input("Enter count: "))
    except ValueError as e:
        print(f"Ошибка: {e}")
        return find_product_min_count(inventory)
    for item in inventory:
        if item['count'] <= count:
            print_product(item)

def copy_file(origin_path, new_path):
    def read_file_by_cunck(file, size=1024):
        while True:
            data = file.read(size)
            if not data:
                break
            yield data
    def write_file_by_cunck(file, data):
        for chunk in data:
            file.write(chunk)
    for el in read_file_by_cunck(open(origin_path, 'rb')):
        with open(new_path, 'wb') as file:
            write_file_by_cunck(file, el)


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
            if os.path.exists(DB_COPY):
                os.unlink(DB_COPY)
            with open(DB, 'r') as file:
                with open(DB_COPY, 'w') as file_copy:
                    file_copy.write(file.read())
            break
        case _:
            print("Invalid input")









