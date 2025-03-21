# # Импортировать библиотеку Re.
# # Загрузить текст из файла live-coding/regex-2.txt.
# # Найдите все хэштеги в тексте. Хэштег — это слово, начинающееся с символа #, за которым следуют буквы и/или цифры,
# # но не цифра в начале.
# # Найдите все IPv4-адреса в тексте. IPv4-адрес состоит из четырех чисел от 0 до 255, разделенных точками.
# # Замените несколько пробелов и табуляций на один пробел. Выводите только обработанные строки.
# # Проверьте возраст пользователей и для пользователей младше 18 лет выведите предупреждение. Считаем что в тексте
# # обязательно сначала встречается имя потом ip адрес и затем дата рождения. Имя может состоять из имени и фамилии,
# # а может только из имени.
#
# import re
#
#
# def main():
#     # Загрузить текст из файла live-coding/regex-2.txt.
#     with open('regex-2.txt', 'r') as file:
#         text = file.read()
#     print(text, '\n')
#
#
#
#
# if __name__ == '__main__':
#     main()


import re


def find_hashtags(text):
    return re.findall(r'#[A-Za-z]+\w*', text)


def find_ipv4_addresses(text):
    ipv4_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\b'
    return re.findall(ipv4_pattern, text)


def clean_whitespace(text):
    return re.sub(r'[ \t]+', ' ', text)


def check_age(text):
    pattern = re.findall(
        r'(\b[A-Za-z]+(?:\s[A-Za-z]+)?\b)\s(\b(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\b)\s(\d{4})',
        text)
    for name, ip, birth_year in pattern:
        age = 2025 - int(birth_year)
        if age < 18:
            print(f'⚠️ {name} (IP: {ip}) младше 18 лет!')

    print("Найденные хэштеги:", hashtags)
    print("Найденные IPv4-адреса:", ipv4_addresses)

    check_age(text)

def main():
    with open('regex-2.txt', 'r') as file:
        text = file.read()

    hashtags = find_hashtags(text)
    ipv4_addresses = find_ipv4_addresses(text)
    cleaned_text = clean_whitespace(text)

    print('Найдите все хэштеги в тексте:')
    match = re.findall(r'#[^\d](?=\w*[A-Za-z])\w+\b', text, re.MULTILINE)
    for n, m in enumerate(match):
        print(f'{n}: {m}')

    print('\nНайдите все все IPv4-адреса в тексте:')
    match = re.findall(r'\b\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\b', text, re.MULTILINE)
    for i, m in enumerate(match):
        res = []
        for n in m.split('.'):
            if int(n) > 255:
                break
            else:
                res.append(n)
        if len(res) == 4:
            print(str(i) + ': ' + '.'.join(res))

    print('\nЗамените несколько пробелов и табуляций на один пробел:')
    for line in text.split('\n'):
        if re.findall(r'\s{2,}', line):
            print(re.sub(r'\s{2,}', ' ', line))

    # Alternative solution with generator:
    print('\nAlternative solution:')
    [print(re.sub(r'\s{2,}', ' ', line)) for line in text.split('\n') if re.findall(r'\s{2,}', line)]

    # Проверьте возраст пользователей и для пользователей младше 18 лет выведите предупреждение. Считаем что в тексте
    # обязательно сначала встречается имя потом ip адрес и затем дата рождения. Имя может состоять из имени и фамилии,
    # а может только из имени.
    # 1. Ищем имя - одно или два слова с заглавной буквы не являющиеся началом строки
    pattern = r'(?<!^)\b[A-Z][a-z]*(?:\s+[A-Z][a-z]*)?\b'
    # 2. Ищем ip адрес - это мы уже умеем
    # 3. Ищем дату - это мы уже умеем
    # 4. Вычисляем возраст - это просто
    # 5. Проверяем по положению в строке взаимное расположение имени, ip-адреса и даты
    # 6. Проверяем окончание одного шаблона и начала следующего

    print("Обработанный текст:")
    print(cleaned_text, '\n')

if __name__ == '__main__':
    main()