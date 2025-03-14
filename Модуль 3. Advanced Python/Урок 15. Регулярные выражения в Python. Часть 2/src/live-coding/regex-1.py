# Импортировать библиотеку Re.
# Загрузить текст из файла live-coding/regex-1.txt.
# Найти первое слово строки.
# Найти последнее слово строки.
# Найти все знаки препинания.
# Найти последнее слово строки без завершающего символа знака препинания.
# Найдите все номера кредитных карт в тексте. Номер кредитной карты — это 16-значное число, разделенное пробелами или
# дефисами каждые 4 цифры, но не 16 цифр подряд без разделителей.

import re


def main():
    # Загрузить текст из файла live-coding/regex-1.txt.
    with open('regex-1.txt', 'r') as file:
        text = file.read()
    print(text, '\n')

    print('Найти первое слово строки:')
    match = re.findall(r'^\w{1,}', text, re.MULTILINE)
    for n, m in enumerate(match):
        print(f'{n}: {m}')

    # Найти последнее слово строки
    print('\nНайти последнее слово строки:')
    match = re.findall(r'\w{1,}\W$', text, re.MULTILINE)
    for n, m in enumerate(match):
        print(f'{n}: {m}')

    # Найти все знаки препинания
    print('Найти все знаки препинания:')
    match = re.findall(r'[^\w\s]', text, re.MULTILINE)
    for n, m in enumerate(match):
        print(f'{n}: {m}')

    # Найти последнее слово строки без завершающего символа знака препинания
    print('\nНайти последнее слово строки без завершающего символа знака препинания:')
    match = re.findall(r'\b\w+\b(?=\s*[^\w\s]?$)', text, re.MULTILINE)
    for n, m in enumerate(match):
        print(f'{n}: {m}')

    # Найти последнее слово строки без завершающего символа знака препинания
    print('\nНайдите все номера кредитных карт в тексте:')
    match = re.findall(r'\b\d{4}[-|\s]\d{4}[-|\s]\d{4}[-|\s]\d{4}\b', text, re.MULTILINE)
    for n, m in enumerate(match):
        print(f'{n}: {m}')


if __name__ == '__main__':
    main()
