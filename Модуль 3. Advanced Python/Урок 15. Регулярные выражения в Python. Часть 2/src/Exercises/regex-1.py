# # Загрузите текст из файла regex-1.txt
# # Найти первое слово строки.
# # Найти последнее слово строки.
# # Найти все знаки препинания.
# # Найти последнее слово строки без завершающего символа знака препинания.
# # Найдите все номера кредитных карт в тексте. Номер кредитной карты — это 16-значное число, разделенное пробелами или
# # дефисами каждые 4 цифры, но не 16 цифр подряд без разделителей.
#
# import re
#
#
# def main():
#     pass
#
#
# if __name__ == '__main__':
#     main()

import re


def main():
    # Открытие файла
    with open('regex-1.txt', 'r') as file:
        text = file.read()

    # 1. Найти первое слово строки
    first_word = re.search(r'\S+', text)
    if first_word:
        print(f"Первое слово строки: {first_word.group()}")

    # 2. Найти последнее слово строки
    last_word = re.search(r'\S+\s*$', text)
    if last_word:
        print(f"Последнее слово строки: {last_word.group().strip()}")

    # 3. Найти все знаки препинания
    punctuation = re.findall(r'[.,!?;:]', text)
    print(f"Знаки препинания: {punctuation}")

    # 4. Найти последнее слово без завершающего знака препинания
    last_word_without_punctuation = re.search(r'(\S+)[.,!?;:]*\s*$', text)
    if last_word_without_punctuation:
        print(f"Последнее слово без знаков препинания: {last_word_without_punctuation.group(1)}")

    # 5. Найти все номера кредитных карт
    credit_card_numbers = re.findall(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b', text)
    print(f"Номера кредитных карт: {credit_card_numbers}")


if __name__ == '__main__':
    main()
