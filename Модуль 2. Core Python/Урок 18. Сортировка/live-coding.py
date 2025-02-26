# Тема: Сортировка с использованием sort и sorted
# Покажите в режиме live-coding и объясните:
# - Как выполняется сортировка через sort и sorted;
# - Как выполнять сортировку по ключу.
from icecream import ic as print


numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  # [1, 2, 5, 5, 6, 9]
numbers = [5, 2, 9, 1, 5, 6]
order_numbers = sorted(numbers)
print(order_numbers)  # [1, 2, 5, 5, 6, 9]

personal =[
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23}
]

personal.sort(key=lambda x: x["age"])
print(personal)  # [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
order_personal = sorted(personal, key=lambda x: x["age"])
print(order_personal)  # [{'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]

data = [(3, 5), (1, 7), (4, 2), (6, 3)]
data.sort(key=lambda x: x[0] + x[1])
data.sort(key=sum)
print(data)  # [(1, 7), (4, 2), (3, 5), (6, 3)]

data = [(3, 5), (1, 7), (4, 2), (6, 3)]
order_data = sorted(data, key=lambda x: x[0] + x[1])
order_data = sorted(data, key=sum)
print(order_data)  # [(1, 7), (4, 2), (3, 5), (6, 3)]








# Тема: Cортировка с all, any, isinstance
# Покажите в режиме live-coding и объясните:
# - Как использовать isinstance, all и any при сортировке.

data = [3, 'a', 5, 'b', 2]
sorter_data = sorted(filter(lambda x: isinstance(x, int), data))
print(sorter_data)  # [2, 3, 5]

numbers = [1, 2, 3, 4, 5]
print(all(num > 0 for num in numbers))  # True
ll = [num > 3 for num in numbers]
print(ll)
print(all(num > 3 for num in numbers))  # False
print(any(num > 3 for num in numbers))  # True