name = "Daniel"
surname = "Dagner"
full_name = name + " " + surname
print("Полное имя:", full_name)

print("Первый символ имени:", name[0])
print("Последний символ имени:", name[-1])


surname_repeated = surname * 5
result = name + " " + surname_repeated
print("Результат дублирования фамилии:", result)

text = "Я Учусь На Python"
lower_text = text.lower()
count_ya = lower_text.count("я")
print("Текст в нижнем регистре:", lower_text)
print("Количество букв 'я':", count_ya)
.
text_replace = "Python это круто!"
updated_text = text_replace.replace("Python", "Программирование")
print("Обновленный текст:", updated_text)

text_to_split = "Я люблю, писать, код"
split_list = text_to_split.split(", ")
print("Список после разделения:", split_list)

text_with_spaces = "   Лишние пробелы убраны   "
trimmed_text = text_with_spaces.strip()
print("Текст без пробелов:", trimmed_text)

name = "Daniel"
topic = "Python"
formatted_string = "Привет, меня зовут {name}. Я изучаю {topic}.".format(name=name, topic=topic)
print("Форматированная строка:", formatted_string)

topic_upper = "Deep learning".upper()
f_string = f"Тема: {topic_upper}."
print("Результат F-строки:", f_string)

user_input = input("Введите строку: ")
if "Python" in user_input:
    print("Вы любите Python!")
else:
    print("Попробуйте изучить Python, это интересно!")