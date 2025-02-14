# Тема: Обработка исключений (try/except/else/finally)
# Продемонстрируйте использование блоков try, except, else и finally.
# Покажите обработку исключений при чтении и записи файла.


try:
    # with open('./some_dir/some_file.txt', 'r') as file:
    #     content = file.read()
    raise IOError('Permission error')
except FileNotFoundError as e:
    print(f'Ошибка File not found: {e}')
except PermissionError as e:
    print(f'Ошибка Permission: {e}')
except IOError as e:
    print(f'Ошибка input-putput: {e}')
else:
    print(content)
finally:
    print('Операция завершена')









# Тема: Расространение исключения. Возбуждение исключения.
# Покажите в режиме live-coding и объясните:
# - Иерархию исключений
# - Распространение исключения
# - Возбуждение исключение через raise


def foo_1():
    try:
        foo_2()
    except ValueError as error:
        print(f'Ошибка: {error} in foo 1')

def foo_2():
    foo_3()

def foo_3():
    raise ValueError('Ошибка в foo_3')

try:
    foo_1()
except ValueError as e:
    print(f'Ошибка: {e}')