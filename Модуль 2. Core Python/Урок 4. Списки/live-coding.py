# Тема 1. Продемонстрируйте и объясните в режиме live-coding:
# - создание списка,
names = ['John', 'Paul', 'George', 'Ringo']
# - доступ к элементам списка,
print(names[0])
print(names[1])
print(names[2])

# - изменение значения элемента списка,
names[0] = 'John Lennon'
print(names)
# - получение среза,
print(names[1:3])
# - создание и работу с вложенными списками.
names.append(['Pete', 'Stuart'])
print(names)
names = ['John', 'Paul', 'George', 'Ringo', ['Pete', 'Stuart']]
print(names[4][0])
names[4][0] = 'Pete Best'
print(names)










# Тема 2. Продемонстрируйте и объясните в режиме live-coding:
# - Использование различных методов списков.
list_item = [1, 2, 3, 4, 5]
list_item.append(6)
print(list_item)
list_item.extend([7, 8])
print(list_item)
list_item.insert(1, 1.5)
print(list_item)
list_item.remove(1.5)
print(list_item)
print(list_item.pop())
print(list_item)
list_item.clear()
print(list_item)
# - Сравнение списков
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
print(list_1 == list_2)
print(list_1 is list_2)
list_3 = list_1
print(list_1 is list_3)
print(list_1, list_3)
list_1[0] = 100
print(list_1, list_3)

# - Изменяемость списков и неизменяемость строк
