# Тема: Интеграционная практика. Мини-проект
import json

# Проект: Перепишите проект из уроков 7-8 с записью, чтением, обновлением и удалением товаров в файле.
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




