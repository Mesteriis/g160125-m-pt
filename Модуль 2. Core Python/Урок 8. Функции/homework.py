# Задача 1: Анализ чисел
# Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
#
# numbers = [1, 2, 3, 4, 5, 6]
# Вывод функции: (21, 3.5, 3)

#def analyze_numbers(numbers):
#    if not numbers:
#        return (0, 0, 0)

#    total_sum = sum(numbers)
#    average = total_sum / len(numbers)
#    even_count = sum(1 for num in numbers if num % 2 == 0)

#    return (total_sum, average, even_count)

#numbers = [1, 2, 3, 4, 5, 6]
#result = analyze_numbers(numbers)
#print(result)

# Задача 2: Работа со строками
# Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
#
# strings = ["apple", "banana", "cherry", "date"]
# Вывод функции: ('banana', 'date', 3)

#def analyze_strings(strings):
#    if not strings:
#        return None, None, 0

#    longest = max(strings, key=len)
#    shortest = min(strings, key=len)
#    count_with_a = sum(1 for s in strings if 'a' in s)

#    return longest, shortest, count_with_a

#strings = ["apple", "banana", "cherry", "date"]
#print(analyze_strings(strings))

# Задача 3: Обработка словаря сотрудников
# Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
#
# employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# Вывод функции: (6000.0, 7000, 'Bob')

#def analyze_salaries(employees):
#    if not employees:
#        return (0, 0, None)  # Возвращаем значения по умолчанию для пустого словаря

#    total_salary = sum(employees.values())
#    avg_salary = total_salary / len(employees)
#    max_salary = max(employees.values())
#    max_salary_employee = max(employees, key=employees.get)

#    return (avg_salary, max_salary, max_salary_employee)

#employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
#print(analyze_salaries(employees))

# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])

#def filter_numbers(numbers):
#    even_numbers = [num for num in numbers if num % 2 == 0]
#    odd_numbers = [num for num in numbers if num % 2 != 0]
#    return even_numbers, odd_numbers

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#result = filter_numbers(numbers)
#print(result)

# Задача 5: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}

#def create_dict(keys, values):
#    return dict(zip(keys, values))

#keys = ["name", "age", "city"]
#values = ["Alice", 30, "New York"]
#result = create_dict(keys, values)
#print(result)

# Задача 6: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

#def count_characters(string):
#    char_count = {}
#    for char in string:
#        char_count[char] = char_count.get(char, 0) + 1
#    return char_count

#string = "hello world"
#result = count_characters(string)
#print(result)

# Задача 7: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)

#def sum_positive_negative(*args):
#    positive_sum = sum(x for x in args if x > 0)
#    negative_sum = sum(x for x in args if x < 0)
#    return positive_sum, negative_sum

#result = sum_positive_negative(1, -2, 3, -4, 5)
#print(result)

# Задача 8: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York

#def generate_string(**kwargs):
#    return ', '.join(f"{key}={value}" for key, value in kwargs.items())

#result = generate_string(name="Alice", age=30, city="New York")
#print(result)

# Проект: Перепишите проект из урока 7 в функциональном стиле.
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

def show_inventory(inventory):
    for item in inventory:
        print(f"Товар: {item['product']}, Цена: {item['price']}, Количество: {item['count']}")
    print()


def add_product(inventory):
    product = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    count = int(input("Введите количество товара: "))
    inventory.append({'product': product, 'price': price, 'count': count})
    print(f"Товар '{product}' добавлен!\n")


def remove_product(inventory):
    product_name = input("Введите название товара для удаления: ")
    inventory[:] = [item for item in inventory if item['product'] != product_name]
    print(f"Товар '{product_name}' удален!\n")


def update_product(inventory):
    product_name = input("Введите название товара для обновления: ")
    for item in inventory:
        if item['product'] == product_name:
            new_name = input(f"Введите новое название (оставьте пустым, чтобы не менять): ") or item['product']
            new_price = input(f"Введите новую цену (оставьте пустым, чтобы не менять): ")
            new_count = input(f"Введите новое количество (оставьте пустым, чтобы не менять): ")
            item['product'] = new_name
            item['price'] = float(new_price) if new_price else item['price']
            item['count'] = int(new_count) if new_count else item['count']
            print(f"Товар '{product_name}' обновлен!\n")
            return
    print(f"Товар '{product_name}' не найден!\n")


def find_product(inventory):
    product_name = input("Введите название товара для поиска: ")
    results = [item for item in inventory if item['product'] == product_name]
    if results:
        for item in results:
            print(f"Найден: {item}")
    else:
        print("Товар не найден!")
    print()


def filter_by_price(inventory):
    max_price = float(input("Введите максимальную цену: "))
    results = [item for item in inventory if item['price'] <= max_price]
    if results:
        for item in results:
            print(item)
    else:
        print("Нет товаров дешевле указанной цены.")
    print()


def filter_by_count(inventory):
    max_count = int(input("Введите максимальное количество: "))
    results = [item for item in inventory if item['count'] <= max_count]
    if results:
        for item in results:
            print(item)
    else:
        print("Нет товаров с таким количеством.")
    print()


# Создание тестового списка товаров
inventory = [
    {'product': "Laptop", 'price': 1000, 'count': 13},
    {'product': "Mouse", 'price': 50, 'count': 1},
    {'product': "Keyboard", 'price': 30, 'count': 33},
    {'product': "Monitor", 'price': 200, 'count': 10}
]

# Главное меню
while True:
    print("Меню:")
    print("1. Показать список товаров")
    print("2. Добавить товар")
    print("3. Удалить товар")
    print("4. Обновить товар")
    print("5. Найти товар по названию")
    print("6. Вывести список товаров дешевле определенной цены")
    print("7. Вывести список товаров с количеством меньше заданного")
    print("8. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        show_inventory(inventory)
    elif choice == "2":
        add_product(inventory)
    elif choice == "3":
        remove_product(inventory)
    elif choice == "4":
        update_product(inventory)
    elif choice == "5":
        find_product(inventory)
    elif choice == "6":
        filter_by_price(inventory)
    elif choice == "7":
        filter_by_count(inventory)
    elif choice == "8":
        print("Выход из программы.")
        break
    else:
        print("Некорректный ввод, попробуйте снова.\n")


