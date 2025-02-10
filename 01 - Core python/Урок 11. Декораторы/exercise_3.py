# Дополнительная практика
#
#
# 1. Создайте декоратор to_upper, который преобразует строковый результат функции в верхний регистр.
#
def to_upper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@to_upper
def get_greeting(name):
    return f"Привет, {name}"
#
print(get_greeting("Алиса"))
# # Вывод: ПРИВЕТ, АЛИСА


# 2. Создайте декоратор limit_calls, который ограничивает количество вызовов функции заданным числом.
# Если функция вызывается больше разрешенного числа раз, выводите сообщение об ошибке.
#
counts = {}
def limit_calls(n):
    def decorator(func):
        global counts
        if func.__name__ not in counts:
            counts[func.__name__] = {
                'counter': 0,
                'limit': n
            }
        def wrapper(*args, **kwargs):
            if counts[func.__name__]['counter'] < counts[func.__name__]['limit']:
                counts[func.__name__]['counter'] += 1
                return func(*args, **kwargs)
            else:
                print(f"Ошибка: функция {func.__name__} может быть вызвана не более {counts[func.__name__]['limit']} раз")
        return wrapper
    return decorator

@limit_calls(3)
def say_hello(name):
    print(f"Привет, {name}!")

say_hello("Алиса")
# Вывод: Привет, Алиса!
say_hello("Боб")
# Вывод: Привет, Боб!
say_hello("Чарли")
# Вывод: Привет, Чарли!
say_hello("Дейв")
# Вывод: Ошибка: функция say_hello может быть вызвана не более 3 раз