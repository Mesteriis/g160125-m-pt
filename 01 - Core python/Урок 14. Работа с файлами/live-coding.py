# Продемонстрируйте в режиме live-coding и объясните:
# - работу функции open в различных режимах;
# - чтение и запись данных в файл;
# - работу указателей.
import json

from icecream import ic as print
# file = open('./text_files/test.txt', 'w')
# file.write('Hello, world!\n')
# file.close()

#
# file = open('./text_files/test.txt', 'a')
# file.write('Hello, world!\n')
# file.close()
#
# file = open('./text_files/test.txt', 'r')
# print(file.tell())
# print(file.read())
# print(file.tell())
# file.seek(5)
# print(file.tell())
# print(file.read(3))
# print(file.tell())
# file.close()




# Продемонстрируйте в режиме live-coding и объясните:
# - работу менеджера контекста;
# - чтение и запись данных в json-формате.

with open('test.json') as file:
    data = file.read()
    data_obj = json.loads(data)
    print(data_obj)

with open('test.json') as file:
    data_ = json.load(file)
    for el in data_:
        print(el)
        print(el['key'])