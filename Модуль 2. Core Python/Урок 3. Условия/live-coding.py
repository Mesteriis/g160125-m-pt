# Продемонстрируйте работу булевых переменных и операторов сравнения.
# Продемонстрируйте работу условных операторов if и if-else.





# Продемонстрируйте и объясните работу:
# - Вложенных условий
# - Конструкции if-elif-else

a = 100

if a > 100:
    print('a > 100')
elif a == 100:
    print('a == 100')
else:
    print('a < 100')

if a > 100:
    print('a > 100')
else:
    if a == 100:
        print('a == 100')
    else:
        print('a < 100')

if a > 100:
    print('a > 100')

if a == 100:
    print('a == 100')

if a < 100:
    print('a < 100')

# - Тернарного условного оператора

result = True if a > 100 else False

result = None
if a > 100:
    result = True
else:
    result = False



# Логические операторы: and, or, not
