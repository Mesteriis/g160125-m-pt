# Тема: Менеджер контекста и JSON
import json
# Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# 3. Прочитайте данные из файла `user.json` и выведите их на экран.
data = {
    "name": "John",
    "age": 30,
    "city": "NY"
}
with open ("./text_files/user.json", "w") as file:
    json.dump(data, file)
with open("./text_files/user.json") as file:
    data = json.load(file)
    print(data)
# Задача 2: Обновление данных в файле JSON
# 1. Прочитайте данные из файла `user.json`.
# 2. Обновите возраст пользователя на 29 лет.
# 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.
with open ("./text_files/user.json", "r") as file:
    data = json.load(file)
    data["age"] = 29
with open ("./text_files/user.json", "w") as file:
    json.dump(data, file)
with open ("./text_files/user.json") as file:
    correct = json.load(file)
    print(correct)
# Задача 3: Добавление нового пользователя в массив JSON
# 1. Прочитайте массив объектов из файла `users.json`
# (каждый объект содержит информацию о пользователе: имя, возраст, город).
# 2. Добавьте нового пользователя в массив.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
with open ("./text_files/user.json") as file:
    users = json.load(file)
    users = [users]
    new_user = {"name": "Daniel", "age": 26, "city": "l-hut"}
    users.append(new_user)
with open ("./text_files/user.json", "w") as file:
    json.dump(users, file)
with open ("./text_files/user.json") as file:
    new_file = json.load(file)
    print(new_file)

# Задача 4: Удаление пользователя из массива JSON
# 1. Прочитайте массив объектов из файла `users.json`.
# 2. Удалите одного из пользователей.
# 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
with open ("./text_files/user.json", "r") as file:
    uninstall_element = json.load(file)
    uninstall_element.pop()
with open ("./text_files/user.json", "w") as file:
    json.dump(uninstall_element, file)
with open ("./text_files/user.json") as file:
    new_file = json.load(file)
    print(uninstall_element)