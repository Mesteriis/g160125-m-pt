# ДАННЫЕ И ПЕРЕМЕННЫЕ
# Продемонстрируйте работу переменных и разных типов данных. Объясните механизм работы кода.
# - Переменные с разным типом данных: строками, целыми и дробными числами
integer = 7
integer_1 = 73476438745446735
integer_2 = 7_000_000_000

string = "П'риве'т"
string_1 = 'П"риве"т'
string_2 = """
sad,jhfj,shdgf
sdakfhglhdjsfgduisa
djh,asgfsadgfluyh
sdkjhgafjlhsadgf
"""

float = 7.0
float_1 = 7.2
float_2 = 7.3
# - Вывод типа данных через print(type())
print(type(integer))
print(type(integer_1))
print(type(integer_2))

print(type(string))
print(type(string_1))
print(type(string_2))

print(type(float))
print(type(float_1))
print(type(float_2))
# - Обращение к несуществующим переменным или объявленным ниже
# a + 1 <--- NameError: name 'a' is not defined
# - Переприсвание, каскадное присваивание, множественное присваивание
a, b = 1, 2

c = a
b = a
a = c

a,b = b,a
# - Наименования переменных


a = 1








# ЧИСЛА И ОПЕРАЦИИ НАД НИМИ
# Продемонстрируйте работу с числами и арифметическими операциями.
# Объясните механизм работы кода.
# - Разные типы чисел: int, float
a = 5
b = 3
# - Выполнение арифметических операций +, -, *, /, //, %, **
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
# - Сокращенная запись +=, -=, *=, /+ и т.д.
i = 1
i += 10
i -= 1
i *= 2
i /= 2
print(i)
# - Применение встроенных математических функций
a = 10
b = 20
print(max(a, b))
print(min(a, b))
print(abs(a - b))
print(pow(a, b))
# - Округление чисел
a = 3.14159
print(round(a))
print(round(a, 2))







# ФУНКЦИИ PRINT(), INPUT()
# Продемонстрируйте работу:
# - print()

# - input()
a = "1"
a = input("Введите число: ")
print(a)

# - sep=
# - end=
# - строки и переменные в print(), input()
#
# Объясните механизм работы кода.
