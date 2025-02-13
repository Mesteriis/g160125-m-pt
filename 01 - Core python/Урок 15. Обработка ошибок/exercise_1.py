# Тема: Обработка исключений (try/except/else/finally)

# # Задача 1: Деление чисел
# # Напишите функцию, которая принимает два числа в качестве аргументов и возвращает результат их деления.
# # Обработайте исключения для случаев, когда:
# # - деление на ноль
# # - ввод не числовых значений.
# # def divide_numbers():
# #     try:
# #         a = float(input("Введите первое число: "))
# #         b = float(input("Введите второе число: "))
# #         result = a / b
# #         print(f"Результат: {result}")
# #     except ZeroDivisionError:
# #         print("Ошибка: Деление на ноль невозможно.")
# #     except ValueError:
# #         print("Ошибка: Введите числовые значения.")
# # divide_numbers()
# #
#
# # Задача 2: Обработка пользовательского ввода
# # Напишите программу, которая запрашивает у пользователя ввод числа и выводит его квадрат.
# # Обработайте исключения для случаев, когда ввод не является числом.
# # def divide_numbers():
# #     try:
# #         a = float(input("Введите первое число: "))
# #         result = a * a
# #         print(f"Результат: {result}")
# #     except ValueError:
# #         print("Ошибка: Введите числовые значения.")
# # divide_numbers()
#
#
# # Задача 3. Вернитесь к задачам предыдущего урока из файла exercise_1 и добавьте в решение обработку возможных ошибок,
# # которые могут случиться при работе с файлами (FileNotFoundError, PermissionError, IOError).
# # Проверьте, что ошибки обрабатываются на примере FileNotFoundError.
# try:
# file_d = open('./text_files/data.txt')
# content = file_d.read()
# file_d.seek(0)
# part_content = file_d.read(10)
# file_d.seek(0)
# str_content = file_d.readline()
# file_d.seek(0)
# all_str_content = file_d.readlines()
# print(all_str_content)
# file_d.close()
#
# except FileNotFoundError:
# print("File not found")
# except PermissionError:
# print("No access to file")
# except IOError:
# print("Incorrect input")