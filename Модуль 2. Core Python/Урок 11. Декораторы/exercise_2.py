# Дополнительная практика


# 1. Создайте декоратор requires_auth, который проверяет наличие определенного флага authenticated и выполняет
# функцию только если этот флаг установлен в True.
#
# authenticated = False
authenticated = False
def requires_auth(func):
    def wrapper():
        if authenticated:
            return func()
        else:
            print("Доступ запрещен: пользователь не аутентифицирован")
    return wrapper

@requires_auth
def secret_function():
    print("Секретная информация")

secret_function()
# Вывод: Доступ запрещен: пользователь не аутентифицирован
authenticated = True
secret_function()
# Вывод: Секретная информация


# 2. Создайте декоратор call_counter, который отслеживает количество вызовов декорируемой функции и
# выводит это количество при каждом вызове.
#
func_name = {}
def call_counter(func):
    global func_name
    if func.__name__ not in func_name:
        func_name[func.__name__] = 0
    def wrapper(*args, **kwargs):
        func_name[func.__name__] += 1
        print(f"Функция {func.__name__} вызвана {func_name[func.__name__]} раз(а)")
        return func(*args, **kwargs)
    return wrapper

@call_counter
def greet(name):
    print(f"Привет, {name}!")
#
greet("Алиса")
# # Вывод:
# # Функция greet вызвана 1 раз(а)
# # Привет, Алиса!
#
greet("Боб")
# # Вывод:
# # Функция greet вызвана 2 раз(а)
# # Привет, Боб!


