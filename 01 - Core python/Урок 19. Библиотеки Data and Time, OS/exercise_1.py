# Тема: Модуль datetime
from datetime import datetime

# Задача 1: Определение текущей даты и времени
# Напишите программу, которая выводит текущие дату и время в формате "YYYY-MM-DD HH:MM:SS".
# Пример: 2024-06-11 14:35:45


# Задача 2: Вычисление возраста
# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.

# bt = input("Enter your birth date in format 'YYYY-MM-DD': ")
# bt = datetime.strptime(bt, "%Y-%m-%d")
# now = datetime.now()
# age = now.year - bt.year
# if now.month < bt.month or (now.month == bt.month and now.day < bt.day):
#     age -= 1
# print(f"Your age is {age}")
#

# Задача 3: Расчет дней до следующего мероприятия
# Напишите программу, которая принимает дату следующего мероприятия в формате "YYYY-MM-DD" и выводит количество дней,
# оставшихся до этой даты.


# Задача 4: Определение дня недели
# Напишите программу, которая принимает дату в формате "YYYY-MM-DD" и выводит день недели для этой даты.

date = input("Enter date in format 'YYYY-MM-DD': ")
date = datetime.strptime(date, "%Y-%m-%d")
print(date.strftime("%A"))


# Задача 5: Сравнение двух дат
# Напишите программу, которая принимает две даты в формате "YYYY-MM-DD" и определяет, какая из них позже.
