# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
# 2. Прочитайте весь контент файла и выведите его на экран.
# 3. Прочитайте первые 10 символов файла и выведите их на экран.
# 4. Прочитайте одну строку из файла и выведите ее на экран.
# 5. Прочитайте все строки файла и выведите их на экран.
# file_d = open("./text_files/data.txt")
# content = file_d.read()
# file_d.seek(0)
# partial_content = file_d.read(10)
# file_d.seek(0)
# one_line = file_d.readline()
# file_d.seek(0)
# all_lines = file_d.readlines()
# print(content)
# print(partial_content)
# print(one_line)
# print(all_lines)
# file_d.close()
# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
# 2. Запишите в файл строку "Hello, World!".
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# 4. Закройте файл.
# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
# file_o = open("./text_files/output.txt", "w")
# file_o.write("Hello , World!\n")
# lines_to_append = ["This is line 1\n", "This is line 2\n"]
# file_o.writelines(lines_to_append)
# file_o.close()
#
# file_o = open("./text_files/output.txt", "r")
# all_file = file_o.read()
# print(all_file)
# file_o.close()

# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
# file_l = open("./text_files/log.txt", "w")
# file_l.write("New log entry\n")
# lines_to_append = ["Log entry 1\n", "Log entry 2\n"]
# file_l.writelines(lines_to_append)
# file_l.close()
#
# file_l = open("./text_files/log.txt", "r")
# printend_file = file_l.read()
# print(printend_file)
# file_l.close()

# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.
# file_p = open("./text_files/pointer_example.txt", 'w')
# file_p.close()
# file_p = open("./text_files/pointer_example.txt", 'r+')
# file_p.write("Python File Handling\n")
# file_p.seek(0)
# file_p.read()
# file_p.seek(7)
# file_p.read(5)
# file_p.seek(0, 2)
# file_p.write("End of file\n")
# file_p.seek(0)
# all_file = file_p.read()
# print(all_file)

