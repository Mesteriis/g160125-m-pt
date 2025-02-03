# Тема: Вложенные циклы: for вложенный в for, for вложенный в while.
# Покажите и объясните использования вложенных циклов в формате live-coding.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in matrix:
    for item in row:
        print(item, end=' ')
    print()


basket = [
    ['apple', 10, 17.50],
    ['banana', 5, 12.00],
    ['orange', 7, 25.00],
]

for fruit in basket:
    for item in fruit:
        print(item, end=' ')
    print()




# Тема: Генераторы списков (List comprehension). Вложенные циклы и вложенные генераторы списков.
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

even_numbers = []
for x in range(10):
    if x % 2 == 0:
        even_numbers.append(x)

matrix = [[x for x in range(3)] for y in range(3)]

print(matrix)

# Продемонстрируйте и объясните использование генераторов списков.
# В том числе использование вложенных генераторов списков.









# Тема: Итератор и итерируемые объекты. Функции iter и next. Сравнение iter и next с циклом for и функцией range.
# Продемонстрируйте создание итератора и использование функций iter и next.


numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
