# Темы: Спецсимволы и экранирование символов, Форматирование строк и F-строки
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Вставьте символ новой строки в строку "Hello World".
# Ожидаемый результат:
# Hello
# World

# print("Hello\nworld")

# 2. Вставьте символ обратного слэша в строку "This is a backslash: ".
# Ожидаемый результат: "This is a backslash: \"

# print("This is a backslash:\\")

# 3. Экранируйте кавычки в строке "He said, "Hello!"".
# Ожидаемый результат: He said, "Hello!"

# print('He said, "Hello!" ')

# 4. Экранируйте одинарные кавычки в строке "It's a sunny day".
# Ожидаемый результат: It's a sunny day

# print("'It's a sunny day'")

# 5. Вставьте символ новой строки в строку "Python Programming".
# Ожидаемый результат:
# Python
# Programming

# print("Python\nProgramming")

# 6. Экранируйте кавычки в строке "She said, 'Hi!'".
# Ожидаемый результат: She said, 'Hi!'
# print("She said, 'Hi!'")

# 7. Экранируйте обратный слэш в строке "Path to file: C:\\".
# Ожидаемый результат: Path to file: C:\\
# print("Path to file: C:\\\\")

# 8. Используйте метод `format()` для строки "This is a ... course for ... learners." с переменными course="Python"
# и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
# course="Python"
# level="beginner"
# formated = "This is a {} course for {} leaners.".format(course, level)
# print(formated)

# 9. Используйте F-строку для строки "This is a ... course for ... learners." с переменными
# course="Python" и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."
# course="Python"
# level="beginner"
# result = f"This is a {course} course for {level} learners."
# print(result)
# 10. Используйте метод `format()` для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
# topic="Machine Learning"
# str1 = "Welcome to the {} workshop.".format(topic)
# print(str1)
# 11. Используйте F-строку для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."
# topic="Machine Learning"
# str1 = f"Welcome to the {topic} workshop."
# print(str1)
# 12. Придумайте название переменной и поместите в нее строку "machine learning",
# затем преобразуйте первые буквы слов в заглавный регистр, чтобы получилось "Machine Learning".
# Затем создайте переменную со строкой "Course: ". Используйте метод `format()`, чтобы показать в консоле
# "Course: Machine Learning"
# machin_lern = "machine learning".title()
# result = "Course: " + "" + "{}".format(machin_lern)              #combo
# print(result)
# 13. Объедините строки "Data" и "Science" с пробелом между ними, дублируйте результат три раза, и используйте F-строку
# для строки "Field: ...". Ожидаемый результат: "Field: Data ScienceData ScienceData Science"
# str1 = "Data"
# str2 = "Science"
# str3 = (str1 + " " + str2) * 3
# result = f"Field: {str3}"
# print(result)
# 14. Выведите третий символ строки "Information", затем используйте метод `format()` для строки "Third character: ...".
# Ожидаемый результат: "Third character: f"
# str1 = "Information"
# substr1 = str1[2]                                                       #3rd
# print(substr1)
# print("Third character: {}".format(substr1))

# 15. Определите длину строки "Neural Networks", умножьте её на 2, и используйте F-строку для строки "Length: ".
# Ожидаемый результат: "Length: 28"
# str1 = "Neural\nNetworks"
# length = (len(str1) * 2) - 2                            # - 2 Space
# print(f"Length: {length}")

# 16. Преобразуйте строку "Deep Learning" в заглавный регистр, найдите индекс подстроки "LEARNING", и выведите символ
# на этом индексе. Ожидаемый результат: "L"
# str1 = "Deep Learning".upper()
# substr = str1[5:13]                         #cut LEARNING
# substr2 = substr[0]                         #cut L
# print(substr2)
# 20. Определите длину строки "Starta", затем преобразуйте её в строку и добавьте к строке " has length of ",
# используя метод `format()`. Ожидаемый результат: "Starta has length of 6"
# str1 = "Starta"
# length = len("Starta")
# result = str1 + " has length of {}".format(length)
# print(result)
