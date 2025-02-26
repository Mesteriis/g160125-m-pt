# Тема: Упаковка аргументов с помощью *args, **kwargs и распаковка через * и **

# 1. Напишите функцию sum_all, которая принимает произвольное количество числовых аргументов
# с помощью *args и возвращает их сумму.

#def sum_all(*args):
#    return sum(args)

#print(sum_all(1, 2, 3, 4, 5))
#print(sum_all(10, 20, 30))


# 2. Напишите функцию combine_lists, которая принимает несколько списков в качестве аргументов с помощью *args
# и возвращает один объединённый список.

#def combine_lists(*args):
#    combined = []
#    for lst in args:
#        combined.extend(lst)
#    return combined

#list1 = [1, 2, 3]
#list2 = [4, 5, 6]
#list3 = [7, 8, 9]

#result = combine_lists(list1, list2, list3)
#print(result)

# 3. Напишите функцию print_details, которая принимает два аргумента name и age.
# Затем создайте словарь с ключами name и age, распакуйте его и передайте в функцию print_details.

#def print_details(name, age):
#    print(f"Name: {name}, Age: {age}")

#person = {"name": "Alice", "age": 30}

#print_details(**person)

# 4. Напишите функцию filter_numbers, которая принимает произвольное количество числовых аргументов с помощью *args
# и возвращает список только тех чисел, которые больше 10.

#def filter_numbers(*args):
#    return [num for num in args if num > 10]

#print(filter_numbers(5, 15, 8, 20, 3, 11))

# Тема: Глобальные и локальные переменные. Вложенные функции и замыкания.

# 1. Напишите функцию increment_global, которая увеличивает значение глобальной переменной counter на 1 каждый раз,
# когда она вызывается.
# increment_global()
# print(counter)  # Вывод: 1
# increment_global()
# print(counter)  # Вывод: 2

#counter = 0

#def increment_global():
#    global counter
#    counter += 1
#increment_global()
#print(counter)
##increment_global()
#print(counter)


# 2. Напишите функцию outer, которая содержит внутреннюю функцию inner. Внутренняя функция должна увеличивать
# значение переменной count, объявленной во внешней функции, на 1 каждый раз при её вызове.
# counter = outer()
# print(counter())  # Вывод: 1
# print(counter())  # Вывод: 2

#def outer():
#    count = 0

#    def inner():
#        nonlocal count
#        count += 1
#        return count

#    return inner

#counter = outer()
#print(counter())
#print(counter())

# 3. Напишите функцию make_multiplier, которая принимает аргумент factor. Внутри этой функции создайте и
# верните функцию multiplier, которая умножает свой аргумент на factor.
# mult_by_2 = make_multiplier(2)
# print(mult_by_2(5))  # Вывод: 10
# mult_by_3 = make_multiplier(3)
# print(mult_by_3(5))  # Вывод: 15

#def make_multiplier(factor):
#    def multiplier(x):
#        return x * factor
#    return multiplier

#mult_by_2 = make_multiplier(2)
#print(mult_by_2(5))

#mult_by_3 = make_multiplier(3)
#print(mult_by_3(5))


# 4. Напишите функцию make_prefixer, которая принимает строку prefix и возвращает внутреннюю функцию prefixer.
# Внутренняя функция должна добавлять prefix к любому переданному ей аргументу.
# add_hello = make_prefixer("Hello, ")
# print(add_hello("Alice"))  # Вывод: Hello, Alice
# print(add_hello("Bob"))    # Вывод: Hello, Bob

#def make_prefixer(prefix):
#    def prefixer(name):
#        return prefix + name
#    return prefixer

#add_hello = make_prefixer("Hello, ")
#print(add_hello("Alice"))
#print(add_hello("Bob"))

# Тема: Дополнительная практика

# 1. Напишите функцию create_user, которая принимает параметры username, email
# и произвольное количество дополнительных данных с помощью **kwargs.
# Функция должна возвращать словарь с информацией о пользователе.

#def create_user(username, email, **kwargs):
#    user_info = {
#        'username': username,
#        'email': email
#    }
#    user_info.update(kwargs)
#    return user_info

# 2. Напишите функцию make_replacer, которая принимает два аргумента old и new. Внутри этой функции создайте
# и верните функцию replacer, которая заменяет все вхождения old на new в переданной ей строке.
# replace_a_with_o = make_replacer("a", "o")
# print(replace_a_with_o("banana"))  # Вывод: bonono
# print(replace_a_with_o("apple"))   # Вывод: opple

#def make_replacer(old, new):
#    def replacer(s):
#        return s.replace(old, new)
#    return replacer

#replace_a_with_o = make_replacer("a", "o")
#print(replace_a_with_o("banana"))
#print(replace_a_with_o("apple"))


# 3. Напишите функцию make_suffixer, которая принимает строку suffix и возвращает внутреннюю функцию suffixer.
# Внутренняя функция должна добавлять suffix к любому переданному ей аргументу.
# add_exclamation = make_suffixer("!")
# print(add_exclamation("Hello"))  # Вывод: Hello!
# print(add_exclamation("Wow"))    # Вывод: Wow!

#def make_suffixer(suffix):
#    def suffixer(word):
#        return word + suffix
#    return suffixer

#add_exclamation = make_suffixer("!")
#print(add_exclamation("Hello"))
#print(add_exclamation("Wow"))

# 4. Напишите функцию make_case_changer, которая принимает аргумент case (значения могут быть "upper" или "lower").
# Внутри этой функции создайте и верните функцию case_changer, которая изменяет регистр строки в зависимости от
# переданного аргумента (если передан аргумент с заглавными буквами, то делаете их строчными, если со строчными,
# то делает их заглавными).
# to_upper = make_case_changer("upper")
# print(to_upper("hello"))  # Вывод: HELLO
# to_lower = make_case_changer("lower")
# print(to_lower("WORLD"))  # Вывод: world

#def make_case_changer(case):
#    def case_changer(word):
#        if case == "upper":
#            return word.upper()
#        elif case == "lower":
#            return word.lower()
#        else:
#            raise ValueError("Invalid case argument. Use 'upper' or 'lower'.")
#    return case_changer

#to_upper = make_case_changer("upper")
#print(to_upper("hello"))

#to_lower = make_case_changer("lower")
#print(to_lower("WORLD"))


# 5. Напишите функцию make_trimmer, которая принимает аргумент length. Внутри этой функции создайте и
# верните функцию trimmer, которая обрезает строку до заданной длины.
# trim_to_3 = make_trimmer(3)
# print(trim_to_3("Hello"))  # Вывод: Hel
# print(trim_to_3("World"))  # Вывод: Wor

#def make_trimmer(length):
#    def trimmer(string):
#        return string[:length]
#    return trimmer

#trim_to_3 = make_trimmer(3)
#print(trim_to_3("Hello"))
#print(trim_to_3("World"))