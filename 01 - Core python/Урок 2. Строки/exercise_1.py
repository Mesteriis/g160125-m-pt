# Темы: Операции над строками, Индексы и срезы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Объедините строки "Hello" и "London" без пробела. Ожидаемый результат: "HelloLondon"
str1 = "Hello"
str2 = "London"
result = str1 + str2
print (result)

# 2. Выведите последний символ строки "Programming". Ожидаемый результат: "g"
str1 = "Programming"
print (str1[-1])

# 3. Дублируйте строку "Hi" три раза. Ожидаемый результат: "HiHiHi"
str1 = "hi"
print (str1 * 3)

# 4. Определите длину строки "Artificial Intelligence".
str1 = "Artificial Intelligence"
print (len (str1))

# 5. Объедините строки "Good" и "Morning" с запятой между ними. Ожидаемый результат: "Good,Morning"
str1 = "Good"
str2 = "Morning"
result = str1 + ", " + str2
print (result)
# 6. Создайте срез строки "Natural Language Processing" со значением "nguag".
str1 = "Natural Language Processing"
substr1 = str1[10:15]
print (substr1)

# 7. Объедините строки "Data" и "Science" с дефисом между ними. Ожидаемый результат: "Data-Science"
str1="Data"
str2="Science"
result = str1 + "-" + str2
print(result)
# 8. Объедините строки "AI" и "ML" с двоеточием между ними. Ожидаемый результат: "AI:ML"
str1="AI"
str2="ML"
result = str1 + ":" + str2
print(result)

# 9. Дублируйте строку "Test" шесть раз. Ожидаемый результат: "TestTestTestTestTestTest"
str1 = "Test"
print (str1 * 6)

# 10. Выведите первый символ строки "Python". Ожидаемый результат: "P"
str1 = "Python"
print (str1[0])

# 11. Создайте срез строки "Hello, Anna!" от 0 до 5. Ожидаемый результат: "Hello"
str1 = "Hello, Anna!"
print (str1[0:5])

# 12. Определите длину строки "Natural Language Processing".
str1 = "Natural Language Processing"
substr1 = len(str1)
print (substr1)

# 13. Выведите второй символ строки "Лето". Ожидаемый результат: "е"
print("Лето"[1])

# 14. Выведите предпоследний символ строки "Machine Learning". Ожидаемый результат: "n"
print("Machine Learning"[14])


# 15. Дублируйте строку "Yes" четыре раза. Ожидаемый результат: "YesYesYesYes"
print("Yes"*4)

# 16. Создайте срез строки "Deep Learning" со значением "ep Le".
print("Deep Learning"[2:7])

# 17. Выведите третий символ строки "Computer Vision". Ожидаемый результат: "m"
print("Computer Vision"[2])

# 18. Определите длину строки "Deep Learning". Ожидаемый результат: 13
s="Deep Learning"
len(s)
print (len (s))

# 19. Объедините строки "Python" и "Rocks" с пробелом между ними. Ожидаемый результат: "Python Rocks"
s1="Python"
s2="Rocks"
print(s1+ " "+s2)
# 20. Создайте срез строки "Data Science" со значением "cien".
print("Data Science"[6:10])


