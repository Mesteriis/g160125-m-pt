# Тема: Чтение и запись данных в файл.

# Задание 1: Чтение данных из файла
# 1. Откройте файл `data.txt` для чтения.
file_d = open('./text_files/data.txt')
# 2. Прочитайте весь контент файла и выведите его на экран.
#content = file_d.read()
# print(content)
# 3. Прочитайте первые 10 символов файла и выведите их на экран.

# part_content = file_d.read(10)
# print(part_content)
# 4. Прочитайте одну строку из файла и выведите ее на экран.
str_content = file_d.readline()
print(str_content)
file_d.seek(0)
# 5. Прочитайте все строки файла и выведите их на экран.
all_str_content = file_d.readlines()
print(all_str_content)
file_d.close()

# Задание 2: Запись данных в файл
# 1. Откройте (создайте) файл `output.txt` для записи.
file_o = open('./text_files/output.txt', 'w')
# 2. Запишите в файл строку "Hello, World!".
file_o.write("Hello, World.\n")
# 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
file_o.append = ["live 1\n", "line2\n"]

# 4. Закройте файл.

# 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
# file_o.close()
# content_o = file_o.read()
# print(content_o)
# file_o.close()
# задание 2 рабочий код:
file_o = open('./text_files/output.txt', 'w')
file_o.write("Hello, World!.\n")
lines_to_append = ["This is line 1\n", "This is line 2\n"]
file_o.writelines(lines_to_append)
file_o.close()

file_o = open('./text_files/output.txt')
content = file_o.read()
print(content)
file_o.close()

# Задание 3: Добавление данных в файл
# 1. Откройте (создайте) файл `log.txt` для добавления данных.
# 2. Добавьте строку "New log entry\n" в конец файла.
# 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# 4. Закройте файл.
# 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
file_l = open('./text_files/log.txt', 'w')

line_to_append = ["New log entry\n"]
file_l.writelines(line_to_append)

lines_to_append = ["Log entry 1\n", "Log entry 2\n"]
file_l.writelines(lines_to_append)

file_l.close()

file_l = open('./text_files/log.txt')
content = file_l.read()
print(content)
file_l.close()

# Задание 4: Работа с указателем
# 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# 2. Запишите в файл строку "Python File Handling\n".
# 3. Переместите указатель в начало файла и прочитайте первую строку.
# 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# 6. Переместите указатель в начало файла и прочитайте весь файл.
# Рабочий код от Даниэль
file_p = open("./text_files/pointer_example.txt", 'w')
file_p.close()
file_p = open("./text_files/pointer_example.txt", 'r+')
file_p.write("Python File Handling\n")
file_p.write("Python File Handling 2\n")
file_p.seek(0)
file_p.read()
file_p.seek(7)
file_p.read(5)
file_p.seek(0, 2)
file_p.write("End of file\n")
file_p.seek(0)
all_file = file_p.read()
print(all_file)
