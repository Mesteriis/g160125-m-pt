# Тема: Итераторы и генераторы. Функции-генераторы. Выражения-генераторы

# Задание 1: Напишите функцию, которая создает итератор, возвращающий числа от 1 до заданного числа `n`.
# Обработайте исключение StopIteration
# def next_num():
#         for num in range(1, 12):
#             yield num
# num = next_num()
# while True:
#     try:
#         print(next(num))
#     except StopIteration:
#         print("Коллекция завершена")
#         break

# Задание 2: Напишите выражение-генератор, которое возвращает квадраты чисел от 0 до 10.
# Обработайте исключение StopIteration
# squares_gen = (x * x for x in range(10))
# def quadrat_num():
#     for x in range(10):
#         yield x * x
# gen = quadrat_num()
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         print("Коллекция завершена")
#         break

# Задание 3: Напишите функцию-генератор, которая принимает предложение и возвращает слова по одному.
# Обработайте исключение StopIteration
def one_word(sentence):
    for word in sentence.split():
        yield word

sentence = "Hello, world!"
word = one_word(sentence)
while True:
    try:
        print(next(word))
    except StopIteration:
        print("End of sentence")
        break