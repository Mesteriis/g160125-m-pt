# # Тема: Словари
# #
# # Продемонстрируйте в режиме live-coding и объясните:
# # - Создание словарей
# from collections.abc import tuple_iterator
#
# dict_1 = {
#     'name': 'John',
#     'age': 25,
#     'city': 'New York'
# }
# personal= {
#     128361826378126532456:{
#         'name': 'John',
#         'age': 25,
#         'city': 'New York'
#     }
# }
# dict_2 = dict(
#     name='John',
#     age=25,
#     city='New York'
# )
# # - Примеры их использования
# # print(dict_1['name'])
# # print(dict_1.get('name'))
# #
# # dict_1['name'] = 'Jack'
# # print(dict_1)
# #
# # del dict_1['name']
# # print(dict_1)
# # - Основные методы словарей
# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items())
#
# dict_1.update({'name': 'John', 'age': 25})
# print(dict_1)
#
# dict_1.clear()
# print(dict_1)
# # - Генератор словарей
#
# keys = ['name', 'age', 'city']
# values = ['John', 25, 'New York']
#
# dict_3 = {keys[i]: values[i] for i in range(len(keys))}
# dict_3 = {key: value for key, value in zip(keys, values)}
# print(dict_3)
#
#






# Тема: Кортежи и множества
#
# Продемонстрируйте в режиме live-coding и объясните:
# - Создание кортежей и множеств
tuple_1 = (1, 2, 3)
tuple_2 = tuple([1, 2, 3])

set_1 = {1, 2, 3}
set_2 = set([2,3,4,5])
print(set_1)
print(set_2)
# - Примеры их использования
for item in tuple_1:
    print(item)

for item in set_1:
    print(item)

print(set_1 - set_2)
print(set_2 - set_1)
print(set_1 | set_2)
print(set_1 & set_2)
print(set_1 ^ set_2)
# - Основные методы кортежей и множеств
print(tuple_1.count(1))
print(tuple_1.index(2))

set_1.add(4)
print(set_1)
set_1.remove(4)
print(set_1)

# - Генератор множеств
list_gen= [x for x in range(10)]
set_gen = {x for x in range(10)}


