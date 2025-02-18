# Тема: map, filter, zip
# Покажите в режиме live-coding и объясните:
# - Использование функций map, filter, zip

# def square(x):
#     return x * x
#
# def is_even(x):
#     return x % 2 == 0
#
# numbers = [1, 2, 3, 4, 5]
#
# squared_numbers = map(square, numbers)
# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))
#
# for number, squared_number in zip(numbers, squared_numbers):
#     print(f"{number} -> {squared_number}")
#






# Тема: map, filter, zip для итераторов, генераторов и файлов с лямбда функциями
# Покажите в режиме live-coding и объясните:
# - Использование lambda-функций в map, filter, zip
# - Использование map, filter, zip при работе с генераторами, файлами





numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda x: x*x, numbers)
print(list(squared_numbers))
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

str_numbers = ['1', '2', '3', "4", "5"]

numbers = map(lambda x: int(x), str_numbers)
print(list(numbers))

def one_lines():
    with open('text_files/data.txt', 'r') as file:
        for el in file:
            yield el.strip()

lines = one_lines()
filtered_lines = filter(lambda x: 'Python' in x, lines)
print(list(filtered_lines))









