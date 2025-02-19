# Тема: Модуль os
import os
# Задача 1: Создание и удаление директории
# Напишите программу, которая создает новую директорию с именем "test_directory", выводит список всех директорий
# в текущем каталоге, а затем удаляет созданную директорию.

# os.mkdir('test_directory')
# current_directory = os.getcwd()
# print(current_directory)
# print(os.listdir(current_directory))
# os.rmdir("test_directory")
# Задача 2: Переименование файла
# Напишите программу, которая создает файл с именем "temp_file.txt", записывает в него строку "Temporary content",
# затем переименовывает файл в "renamed_file.txt" и выводит список всех файлов в текущем каталоге.
# with open("temp_file.txt", "w") as file:
#     file.write("Temporary content")
# # os.rename("temp_file.txt", "renamed_file.txt")
# print(os.listdir("."))

# Задача 3: Проверка существования файла
# Напишите программу, которая проверяет существование файла с именем "example.txt" в текущем каталоге.
# Если файл существует, программа должна вывести его размер в байтах. Если файл не существует,
# программа должна вывести сообщение "Файл не найден".
# with open("example.txt", "w") as file:
#     file.write("Hello, World")
# exists = os.path.exists('example.txt')
# print(exists)
# if exists == True:
#     info = os.stat('example.txt')
#     print(info)
# else:
#     print("Файл не найден")
# Задача 4: Сравнение размеров файлов
# Напишите программу, которая принимает два имени файлов в текущем каталоге, сравнивает их размеры и выводит,
# какой из файлов больше. Если размеры файлов равны, программа должна вывести сообщение "Файлы имеют одинаковый размер".
# def file_sizes(file1, file2):
#     size1 = os.path.getsize(file1)
#     size2 = os.path.getsize(file2)
#
#     if size1 > size2:
#         print(f"Файл '{file1}' больше ({size1} байт) чем '{file2}' ({size2} байт).")
#     elif size2 > size1:
#         print(f"Файл '{file2}' больше ({size2} байт) чем '{file1}' ({size1} байт).")
#     else:
#         print("Файлы имеют одинаковый размер.")
#
# file1 = "example.txt"
# file2 = "renamed_file.txt"
#
# file_sizes(file1, file2)
