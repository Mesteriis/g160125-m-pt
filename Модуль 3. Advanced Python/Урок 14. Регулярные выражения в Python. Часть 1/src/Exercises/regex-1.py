# # Импортировать библиотеку Re.
# # Загрузить текст из файла live-coding/regex-1.txt.
# # Найти в тексте название «Париж».
# # Найти все слова на английском языке.
# # Найти в тексте все имена на английском языке (с большой буквы).
# # Найти все пустые строки.
# # Найти все последовательности из двух или более заглавных букв.
# # Найти все слова из двух или более заглавных букв.
#
# import re
#
#
# def main():
#     # your code here
#     pass
#
#
# if __name__ == '__main__':
#     main()

import re


def main():
    # Загрузим текст из файла
    with open('regex-1.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Найдем название «Париж»
    paris_match = re.search(r'Париж', text)
    if paris_match:
        print(f'Найдено название: {paris_match.group()}')

    # Найдем все слова на английском языке
    english_words = re.findall(r'\b[a-zA-Z]+\b', text)
    print(f'Все слова на английском языке: {english_words}')

    # Найдем все имена на английском языке (с большой буквы)
    names = re.findall(r'\b[A-Z][a-zA-Z]*\b', text)
    print(f'Все имена на английском языке: {names}')

    # Найдем все пустые строки
    empty_lines = re.findall(r'^\s*$', text, re.MULTILINE)
    print(f'Все пустые строки: {empty_lines}')

    # Найдем все последовательности из двух или более заглавных букв
    capital_sequence = re.findall(r'[A-Z]{2,}', text)
    print(f'Последовательности из двух или более заглавных букв: {capital_sequence}')

    # Найдем все слова из двух или более заглавных букв
    capital_words = re.findall(r'\b[A-Z]{2,}\b', text)
    print(f'Слова из двух или более заглавных букв: {capital_words}')


if __name__ == '__main__':
    main()
