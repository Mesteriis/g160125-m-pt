# Тема: Основные методы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# # 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# # Ожидаемый результат: "HOW ARE YOU?"
# str1 = "hOw aRe yOu?"
# print(str1.upper())
#
# # 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".
# str1 = "Bananas are amazing!"
# print(str1.count('a'))
#
# # 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# # Ожидаемый результат: "python programming"
# str1 = "PYTHON PROGRAMMING"
# print(str1.lower())
#
# # 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# # Ожидаемый результат: "Discover new worlds   "
# str1 = "   Discover new worlds   "
# print(str1.lstrip())
#
# # 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# # Ожидаемый результат: "It was a sunny day."
# str1 = "It was a rainy day."
# print(str1.replace('rainy', 'sunny'))
#
# # 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".
# str1 = "Innovation drives progress."
# print(str1.find('innovation'))
#
# # 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# # Ожидаемый результат: "   Explore the universe"
# str1 = "   Explore the universe   "
# print(str1.rstrip())
#
# # 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".
# str1 = "The Milky Way galaxy is vast."
# print(str1.find('galaxy'))

# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]
# str1 = "Apple; Banana; Cherry; Date".split(" ")
# print(str1)

# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."
# str1 = "In the future, humans will rule the world."
# print(str1.replace("robots", "humans"))
# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"
# print("artificial intelligence".upper())
# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]
# print("Python is a versatile language".split())
# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"
# print("Learn Python".strip())