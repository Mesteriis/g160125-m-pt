# # Импортировать библиотеку Re.
# # Загрузить текст из файла live-coding/regex-2.txt.
# # Найти все телефонные номера в формате (123) 456-7890 или 123-456-7890.
# # Найти все даты в формате DD/MM/YYYY или DD-MM-YYYY.
# # Найти все email-адреса.
# # Найти все email-адреса, содержащие символ подчеркивания.
# # Найти все слова, содержащие не менее одной цифры.
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


def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def find_phone_numbers(text):
    pattern = re.compile(r'\(?\d{3}\)?[ -]?\d{3}-\d{4}')
    return pattern.findall(text)


def find_dates(text):
    pattern = re.compile(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b')
    return pattern.findall(text)


def find_emails(text):
    pattern = re.compile(r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}')
    return pattern.findall(text)


def find_emails_with_underscore(text):
    pattern = re.compile(r'[\w.-]*_[\w.-]*@[\w.-]+\.[a-zA-Z]{2,}')
    return pattern.findall(text)


def find_words_with_digits(text):
    pattern = re.compile(r'\b\w*\d+\w*\b')
    return pattern.findall(text)


def main():
    filename = 'regex-2.txt'
    text = load_text(filename)

    print("Phone Numbers:", find_phone_numbers(text))
    print("Dates:", find_dates(text))
    print("Emails:", find_emails(text))
    print("Emails with underscore:", find_emails_with_underscore(text))
    print("Words with digits:", find_words_with_digits(text))


if __name__ == '__main__':
    main()
