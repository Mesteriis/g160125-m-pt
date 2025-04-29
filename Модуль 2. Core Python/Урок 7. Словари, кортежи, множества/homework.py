# Тема: словари

# Задача 1: Анализ данных о сотрудниках
# У вас есть словарь, содержащий информацию о сотрудниках компании.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите имена всех сотрудников.
# 2. Найдите и выведите общую сумму зарплат всех сотрудников.
# 3. Добавьте нового сотрудника "David" с возрастом 28, отделом "IT" и зарплатой 6500.
# 4. Обновите зарплату "Alice" до 5500.
# 5. Удалите сотрудника "Charlie".
# 6. Выведите данные о каждом сотруднике в формате:
# "Имя: {name}, Возраст: {age}, Отдел: {department}, Зарплата: {salary}"
#

# employees = {
#     "Alice": {"age": 30, "department": "HR", "salary": 5000},
#     "Bob": {"age": 25, "department": "IT", "salary": 6000},
#     "Charlie": {"age": 35, "department": "Finance", "salary": 7000}
# }

# 1. Вывести имена всех сотрудников
#print("Имена сотрудников:", ", ".join(employees.keys()))

# 2. Найти и вывести общую сумму зарплат всех сотрудников
#total_salary = sum(emp["salary"] for emp in employees.values())
#print("Общая сумма зарплат:", total_salary)

# 3. Добавить нового сотрудника "David"
#employees["David"] = {"age": 28, "department": "IT", "salary": 6500}

# 4. Обновить зарплату "Alice"
#employees["Alice"]["salary"] = 5500

# 5. Удалить сотрудника "Charlie"
#del employees["Charlie"]

# 6. Вывести данные о каждом сотруднике
#for name, info in employees.items():
#    print(f"Имя: {name}, Возраст: {info['age']}, Отдел: {info['department']}, Зарплата: {info['salary']}")

# Задача 2: Управление запасами товаров
# У вас есть словарь, содержащий информацию о запасах товаров в магазине.
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите названия всех товаров.
# 2. Увеличьте количество "Apples" на 10.
# 3. Измените цену "Bananas" на 1.5.
# 4. Удалите товар "Cherries".
# 5. Добавьте новый товар "Dates" с количеством 15 и ценой 4.
# 6. Выведите общую стоимость всех товаров (количество * цена для каждого товара и сумма этих значений).
#
#inventory = {
#     "Apples": {"quantity": 50, "price": 2},
#     "Bananas": {"quantity": 30, "price": 1},
#     "Cherries": {"quantity": 20, "price": 3},
#}

# 1. Вывести названия всех товаров
#print("Товары в магазине:", list(inventory.keys()))

# 2. Увеличить количество "Apples" на 10
#inventory["Apples"]["quantity"] += 10

# 3. Изменить цену "Bananas" на 1.5
#inventory["Bananas"]["price"] = 1.5

# 4. Удалить товар "Cherries"
#del inventory["Cherries"]

# 5. Добавить новый товар "Dates" с количеством 15 и ценой 4
#inventory["Dates"] = {"quantity": 15, "price": 4}

# 6. Вывести общую стоимость всех товаров
#total_value = sum(item["quantity"] * item["price"] for item in inventory.values())
#print("Общая стоимость товаров:", total_value)


# Тема: кортежи и множества.

# Задача 1: Обработка данных о координатах
# У вас есть список координат, каждая из которых представлена кортежем (x, y).
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите все координаты.
# 2. Найдите сумму всех координат по оси x и по оси y.
# 3. Добавьте новую координату (70, 80).
# 4. Замените первую координату на (15, 25).
# 5. Выведите все координаты, отсортированные по оси x.
#
# Исходный список координат
#coordinates = [(10, 20), (30, 40), (50, 60)]

# 1. Вывод всех координат
#print("Координаты:", coordinates)

# 2. Вычисление суммы координат по осям x и y
#sum_x = sum(x for x, y in coordinates)
#sum_y = sum(y for x, y in coordinates)
#print("Сумма координат по x:", sum_x)
#print("Сумма координат по y:", sum_y)

# 3. Добавление новой координаты
#coordinates.append((70, 80))

# 4. Замена первой координаты
#coordinates[0] = (15, 25)

# 5. Сортировка по оси x
#coordinates.sort(key=lambda coord: coord[0])
#print("Отсортированные координаты:", coordinates)


# Задача 2: Обработка данных о продуктах
# У вас есть список продуктов, каждый из которых представлен кортежем (название, цена).
# Необходимо провести различные операции с этими данными.
#
# Задание:
# 1. Выведите все продукты.
# 2. Найдите суммарную стоимость всех продуктов.
# 3. Добавьте новый продукт "Date" с ценой 4.
# 4. Замените цену "Apple" на 2.5.
# 5. Выведите все продукты, отсортированные по цене.
#
#products = [("Apple", 2), ("Banana", 1), ("Cherry", 3)]
# 1. Вывести все продукты
#print("Все продукты:")
#for name, price in products:
#    print(f"{name}: {price}")

# 2. Найти суммарную стоимость всех продуктов
#total_cost = sum(price for _, price in products)
#print("\nСуммарная стоимость всех продуктов:", total_cost)

# 3. Добавить новый продукт "Date" с ценой 4
#products.append(("Date", 4))

# 4. Заменить цену "Apple" на 2.5
#products = [(name, 2.5) if name == "Apple" else (name, price) for name, price in products]

# 5. Вывести все продукты, отсортированные по цене
#products_sorted = sorted(products, key=lambda x: x[1])
#print("\nПродукты, отсортированные по цене:")
#for name, price in products_sorted:
#    print(f"{name}: {price}")


# Задача 3: Управление группами пользователей
# У вас есть множество пользователей, и вам необходимо выполнить различные операции с этими данными.
#
# Задание:
# 1. Выведите всех пользователей.
# 2. Добавьте нового пользователя "David".
# 3. Удалите пользователя "Bob".
# 4. Проверьте, есть ли пользователь "Alice" в множестве.
# 5. Выведите количество пользователей.
#
#users = {"Alice", "Bob", "Charlie"}
# 1. Вывод всех пользователей
#print("Все пользователи:", users)

# 2. Добавление нового пользователя "David"
#users.add("David")
#print("После добавления David:", users)

# 3. Удаление пользователя "Bob"
#users.discard("Bob")  # Используем discard, чтобы избежать ошибки, если "Bob" нет в множестве
#print("После удаления Bob:", users)

# 4. Проверка наличия "Alice" в множестве
#???
#print("Alice в множестве?", ...?)

# 5. Вывод количества пользователей
#print("Количество пользователей:", len(users))


# Задача 4: Управление наборами данных
# У вас есть два множества, представляющих различные наборы данных.
# Необходимо провести различные операции с этими множествами.
#
# Задание:
# 1. Выведите элементы обоих множеств.
# 2. Найдите объединение двух множеств.
# 3. Найдите пересечение двух множеств.
# 4. Найдите разность множеств `set1` и `set2`.
# 5. Проверьте, является ли `set2` подмножеством `set1`.
#
#set1 = {1, 2, 3, 4, 5}
#set2 = {4, 5, 6, 7, 8}
# 1. Вывод элементов множеств
#print("Множество set1:", set1)
#print("Множество set2:", set2)

# 2. Объединение множеств
#union_set = set1 | set2
#print("Объединение множеств:", union_set)

# 3. Пересечение множеств
#intersection_set = set1 & set2
#print("Пересечение множеств:", intersection_set)

# 4. Разность множеств (set1 - set2)
#difference_set = set1 - set2
#print("Разность set1 и set2:", difference_set)

# 5. Проверка, является ли set2 подмножеством set1
#is_subset = set2.issubset(set1)
#print("Является ли set2 подмножеством set1:", is_subset)


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

#inventory = [
#    {'product': "Laptop", 'price': 1000, 'count': 13},
#    {'product': "Mouse", 'price': 50, 'count': 1},
#    {'product': "Keyboard", 'price': 30, 'count': 33},
#    {'product': "Monitor", 'price': 200, 'count': 10}
#]


#def show_inventory():
#    for item in inventory:
#        print(f"{item['product']}: ${item['price']}, {item['count']} шт.")


#def add_product():
#    name = input("Введите название товара: ")
#    price = float(input("Введите цену товара: "))
#    count = int(input("Введите количество товара: "))
#    inventory.append({'product': name, 'price': price, 'count': count})
#    print("Товар добавлен!")


#def remove_product():
#    name = input("Введите название товара для удаления: ")
#    global inventory
#    inventory = [item for item in inventory if item['product'].lower() != name.lower()]
#    print("Товар удален!")


#def update_product():
#    name = input("Введите название товара для обновления: ")
#    for item in inventory:
#        if item['product'].lower() == name.lower():
#            item['product'] = input("Введите новое название товара (или оставьте пустым): ") or item['product']
#            item['price'] = float(input("Введите новую цену товара (или оставьте пустым): ") or item['price'])
#            item['count'] = int(input("Введите новое количество товара (или оставьте пустым): ") or item['count'])
#            print("Товар обновлен!")
#            return
#    print("Товар не найден!")


#def find_product():
#    name = input("Введите название товара для поиска: ")
#    for item in inventory:
#        if item['product'].lower() == name.lower():
#            print(f"Найдено: {item['product']}: ${item['price']}, {item['count']} шт.")
#            return
#    print("Товар не найден!")


#def filter_by_price():
#    max_price = float(input("Введите максимальную стоимость: "))
#    filtered = [item for item in inventory if item['price'] < max_price]
#    for item in filtered:
#        print(f"{item['product']}: ${item['price']}, {item['count']} шт.")


#def filter_by_count():
#    max_count = int(input("Введите максимальное количество: "))
#    filtered = [item for item in inventory if item['count'] < max_count]
#    for item in filtered:
#        print(f"{item['product']}: ${item['price']}, {item['count']} шт.")


#def menu():
#    while True:
#        print("\nМеню:")
#        print("1. Показать список товаров")
#        print("2. Добавить товар")
#        print("3. Удалить товар")
#        print("4. Обновить товар")
#        print("5. Найти товар по названию")
#        print("6. Вывести товары дешевле заданной стоимости")
#        print("7. Вывести товары с количеством ниже заданного")
#        print("8. Выход")

#        choice = input("Выберите действие: ")
#        if choice == '1':
#            show_inventory()
#        elif choice == '2':
#            add_product()
#        elif choice == '3':
#            remove_product()
#        elif choice == '4':
#            update_product()
#        elif choice == '5':
#            find_product()
#        elif choice == '6':
#            filter_by_price()
#        elif choice == '7':
#            filter_by_count()
#        elif choice == '8':
#            print("Выход из программы.")
#            break
#        else:
#            print("Неверный ввод, попробуйте снова.")


#menu()

