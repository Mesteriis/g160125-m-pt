# Проект: Управление инвентарем в интернет-магазине
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

inventory = [
    {'product': "Laptop", 'price': 10, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 20, 'count': 10}
]

while True:
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
            for product in inventory:
                print(f"Product: {product['product']}, Price: {product['price']}, Count: {product['count']}")
        case "2":
            product = input("Enter product name: ")
            price = int(input("Enter product price: "))
            count = int(input("Enter product count: "))
            inventory.append({'product': product.title(), 'price': price, 'count': count})
        case "3":
            product = input("Enter product name: ")
            for item in inventory:
                if item['product'].lower() == product.lower():
                    inventory.remove(item)
        case "4":
            product = input("Enter product name: ")
            for item in inventory:
                if item['product'].lower() == product.lower():
                    new_product = input(f"Enter new product name or {item['product']}: ")
                    if new_product:
                        item['product'] = new_product.title()
                    new_price = input(f"Enter new product price or {item['price']}: ")
                    if new_price:
                        item['price'] = int(new_price)
                    new_count = input(f"Enter new product count or {item['count']}: ")
                    if new_count:
                        item['count'] = int(new_count)
        case "5":
            product = input("Enter product name: ")
            for item in inventory:
                if item['product'].lower() == product.lower():
                    print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")
        case "6":
            price = int(input("Enter price: "))
            for item in inventory:
                if item['price'] <= price:
                    print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")
        case "7":
            count = int(input("Enter count: "))
            for item in inventory:
                if item['count'] <= count:
                    print(f"Product: {item['product']}, Price: {item['price']}, Count: {item['count']}")
        case "8":
            break
        case _:
            print("Invalid input")
