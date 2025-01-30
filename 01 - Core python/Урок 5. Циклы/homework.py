# Тема: Цикл while. Операторы break, continue, else.
# from itertools import count
# from random import choice

# Упражнение 1: Поиск числа
#
# Напишите программу, которая запрашивает у пользователя числа, пока он не введет число совпадающее
# с переменной num (num = любое число от 0 до 100).  Если введенное число меньше num, программа должна
# выводить сообщение "Слишком маленькое число" и продолжать запрашивать числа. Если число больше num,
# программа должна вывести сообщение "Вы ввели большее число" и продолжать запрашивать числа.
# Если пользователь угадал, то программа должна вывести "Вы угадали число" и завершиться.

# num = 50
# while True:
#     user_num = int(input("Enter your number: "))
#     if user_num < num:
#         print("Слишком маленькое число")
#     elif user_num > num:
#         print("Вы ввели большее число")
#     else:
#         print("Вы угадали число!")
#         break

# Упражнение 2: Проверка пароля
#
# Напишите программу, которая будет запрашивать у пользователя пароль до тех пор, пока не будет введен
# правильный пароль "python123", либо пока не закончатся попытки. Если введенный пароль содержит пробелы,
# программа должна выводить сообщение "Пароль не должен содержать пробелов" и продолжать запрашивать пароль.
# Если введен правильный пароль, программа должна выводить сообщение "Доступ разрешен" и завершаться.  1
# Если после трех неправильных попыток пароль не введен правильно, программа должна выводить сообщение
# "Превышено количество попыток" и завершаться.

# correct_pass = "python123"
# tryes = 0
# max_tryes = 3
# while tryes < max_tryes:
#     user_pass = input("Enter your password: ")
#     if " " in user_pass:
#         print("Password must be without <Space>")                                                                #Space
#     if user_pass == correct_pass:
#         print("Access GRANTED!")
#         break
#     tryes += 1
#     print(f"Wrong password! Tryes quantity::{tryes}")                                                            #tryes
# else:
#     print("Too many tryes!")
        

# Упражнение 3: Работа со списком покупок
#
# Напишите программу, которая будет запрашивать у пользователя элементы для списка покупок до тех пор,
# пока не будет введено слово "стоп", либо пока количество покупок не станет больше 6. Если введенное
# слово уже есть в списке, программа должна выводить сообщение "Этот элемент уже в списке" и продолжать
# запрашивать новые элементы. Если введено слово "стоп", программа должна выводить сообщение
# "Формирование списка завершено" и завершаться. Если количество покупок ставится больше 6,
# то программа должна вывести: “Превышен лимит покупок.” и завершиться.
# Перед завершением программа должна выводить итоговый список покупок и общее количество элементов в нем.

# user_purchases = []
# while True:
#     new_user_purchase = input("Enter your purchase: ")
#     user_purchases.append(new_user_purchase.split(", "))
#     products_quantity = len(user_purchases)
#     if new_user_purchase == "stop".lower():
#         print(f"Shoplist input completed! Products quantity: {products_quantity}")
#         break
#     if len(user_purchases) > 6:
#         print("Shoplist limit!")
#         break
#     print(f"Your shoplist: {user_purchases} Products quantity: {products_quantity}")

# Тема: Цикл for

# Упражнение 1: Подсчет гласных в строке
#
# Напишите программу, которая принимает строку от пользователя и подсчитывать количество гласных букв (a, e, i, o, u)
# в этой строке.Используйте цикл for и условие if.

# user_text = input("Enter your text: ").lower()
# g_letters = "aeiou"
# count = 0
# for letter in user_text:
#     if letter in g_letters:
#         count += 1
# print(count)

# Упражнение 2: Генерация и вывод последовательности чисел
#
# Напишите программу, которая генерит и выводит последовательность чисел от 1 до 20,
# но выводит "Fizz" вместо чисел, кратных 3, "Buzz" вместо чисел, кратных 5, и "FizzBuzz"
# вместо чисел, кратных как 3, так и 5. Используйте цикл for и функцию range.

# numbers = list(range(1, 21))
# for num in numbers:
#     if num % 3 ==0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")

# Проект 1: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.
#
# library = [["Война и мир", "Толстой", "в наличии"],
#            ["Преступление и наказание", "Достоевский", "выдана"],
#            ["Мастер и Маргарита", "Булгаков", "в наличии"]]
# IN = "в наличии"
# OUT = "выдана"
# while True:
#     print("\nМеню")
#     print("1. Показать список всех книг")
#     print("2. Добавить книгу")
#     print("3. Удалить книгу")
#     print("4. Поменять статус книги")
#     print("5. Показать книги определенного автора")
#     print("6. Показать книги с определенным статусом")
#     choice = input("Выберите действие, введя его номер: ")
#
#
#
#     if choice == "1":
#         print(library)
#     if choice == "2":
#         book_name = input("Введите название книги: ")
#         book_author = input("Введите автора: ")
#         book_status = IN
#         library.append([book_name, book_author, book_status])
#         print(f"{book_name} by {book_author} was added")
#     if choice == "3":
#         book_name = input("Введите название книги: ")
#         found_book = None
#         for book in library:
#             if book[0] == book_name:
#                 found_book = book
#         if found_book:
#             antwort = input('Вы уверены в удалении книги? да/нет: ').lower()
#             if antwort == "да":
#                 library.remove(found_book)
#                 print(f"Выбранная книга {found_book[0]} удалена!")
#             else:
#                 print("Книга не найдена!")
#     if choice == "4":
#         book_for_update = input("Выберите книгу: ")
#         book_found = False
#         for book in library:
#             if book[0] == book_for_update:
#                 book[2] = OUT if book[2] == IN else IN
#                 print(f"Статус {book[0]} {book[1]} был изменен.")
#                 found = True
#     if choice == "5":
#         book_author = input("Введите автора книги: ")
#         for book in library:
#             if book[1].lower() == book_author.lower():
#                 print(f"{book[0]} - {book[1]} - {book[2]}")
#     if choice == "6":
#         book_status = input(f"Введите статус книги: {IN} или {OUT}:  ")
#         for book in library:
#             if book[2] == book_status:
#                 print(f"{book[0]} - {book[1]} - {book[2]}")
#


# Проект 2: Анализ посещаемости на сайте
#
# Разработайте программу для анализа посещаемости на сайте. Программа должна позволять вводить количество посещений
# за каждый день недели, определять дни с наибольшей и наименьшей посещаемостью, рассчитывать среднюю посещаемость
# за неделю и выводить дни с посещаемостью выше среднего.
#
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
visits = []

while True:
    print("\nГлавное меню")
    print("1. Ввод количества посещений в день ")
    print("2. Рассчитать дни с наибольшей и наименьшей посещаемостью")
    print("3. Рассчитать среднюю посещаемость за неделю и вывести дни с посещаемостью выше среднего")

    task_number = input("Выберите действие, введя его номер: ")

    match task_number:

        case "1":
            for day in days:
                choose_day = int(input(f"Введите количество посещений за {day}: "))
                visits.append(choose_day)
        case "2":

            max_visits = max(visits)
            min_visits = min(visits)

            max_day = days[visits.index(max_visits)]
            min_day = days[visits.index(min_visits)]

            print(f"Наибольшая посещаемость: {max_visits} в день {max_day}")
            print(f"Наименьшая посещаемость: {min_visits} в день {min_day}")
        case "3":
            if visits:
                avarage_visits = sum(visits) / len(visits)
                print(avarage_visits)
            else:
                print("Нет данных")




