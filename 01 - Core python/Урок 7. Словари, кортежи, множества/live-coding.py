# Тема: Словари
#
# Продемонстрируйте в режиме live-coding и объясните:
# - Создание словарей
dict_1 = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}
personal= {
    128361826378126532456:{
        'name': 'John',
        'age': 25,
        'city': 'New York'
    }
}
dict_2 = dict(
    name='John',
    age=25,
    city='New York'
)
# - Примеры их использования
# print(dict_1['name'])
# print(dict_1.get('name'))
#
# dict_1['name'] = 'Jack'
# print(dict_1)
#
# del dict_1['name']
# print(dict_1)
# - Основные методы словарей
print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

dict_1.update({'name': 'John', 'age': 25})
print(dict_1)

dict_1.clear()
print(dict_1)
# - Генератор словарей

keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']

dict_3 = {keys[i]: values[i] for i in range(len(keys))}
dict_3 = {key: value for key, value in zip(keys, values)}
print(dict_3)








# Тема: Кортежи и множества
#
# Продемонстрируйте в режиме live-coding и объясните:
# - Создание кортежей и множеств
# - Примеры их использования
# - Основные методы кортежей и множеств
# - Генератор множеств
