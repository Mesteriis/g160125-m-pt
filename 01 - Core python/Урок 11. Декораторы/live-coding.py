# Тема: Декораторы
#
# Продемонстрируйте создание и использование декораторов на примерах.
# Объясните механизм работы декоратора, передачу аргументов.
#
# Например, напишите декоратор timeit, который замеряет и выводит время выполнения декорируемой функции.
# В качестве декорируемых функций используйте две функции, одна из которых генерит четные числа от 0 до 10 000
# через цикл for и метод append. А другая генерит эти же цифры через генератор списков.

def time_off(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        print(f'Выполняется функция {func.__name__} c аргументами {args} и {kwargs}')
        result = func(*args, **kwargs)
        print(f'Время выполнения функции {func.__name__}: {time.time() - start} секунд')
        return result
    return wrapper

def logit(func):
    def wrapper(*args, **kwargs):
        print(f'Выполняется функция {func.__name__} c аргументами {args} и {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper

@logit
@logit
@time_off
def even_numbers():
    even_numbers = []
    for i in range(10_000_000):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

@time_off
def ogg_numbers():
    return [i for i in range(10_000_000) if i % 2 != 0]

# even_numbers()
# ogg_numbers()

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(30)
def say_hello(name):
    print(f'Hello, {name}')


say_hello('Vasya')