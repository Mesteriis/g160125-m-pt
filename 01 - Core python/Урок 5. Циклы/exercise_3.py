# Проект: Управление библиотекой
#
# Описание:
# Разработайте программу для управления библиотекой. Программа должна позволять добавлять книги в библиотеку,
# удалять книги, искать книги по автору и выводить список всех книг с их авторами и статусами (в наличии или выдана).
#
# Требования: Реализуйте работу всех пунктов меню.

OUT = "выдана"
IN = "в наличии"


library = [
    ["Война и мир", "Толстой", IN],
    ["Преступление и наказание", "Достоевский", OUT],
    ["Мастер и Маргарита", "Булгаков", IN]
]

while True:
    print("\nМеню")
    print("1. Показать список всех книг")
    print("2. Добавить книгу")
    print("3. Удалить книгу")
    print("4. Поменять статус книги")
    print("5. Показать книги определенного автора")
    print("6. Показать книги с определенным статусом")
    choice = input("Выберите действие, введя его номер: ")
    print()

    # Продолжите программу ниже.

    match choice:
        case "1":
            for book in library:
                print(f"{book[0]} - {book[1]} - {book[2]}")
        case "2":
            name = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            library.append([name, author, IN])
        case "3":
            name = input("Введите название книги: ")
            target_book = None
            for book in library:
                if book[0] == name:
                    target_book = book

            if target_book:
                answer = input("Вы уверены, что хотите удалить книгу? (да/нет): ")
                if answer == "да":
                    library.remove(target_book)
            else:
                print("Книга не найдена.")
        case "4":
            name = input("Введите название книги: ")
            target_book = None
            for book in library:
                if book[0] == name:
                    target_book = book

            if target_book:
                if target_book[2] == IN:
                    target_book[2] = OUT
                else:
                    target_book[2] = IN
            else:
                print("Книга не найдена.")
        case "5":
            author = input("Введите автора книги: ")
            for book in library:
                if book[1].lower() == author.lower():
                    print(f"{book[0]} - {book[1]} - {book[2]}")
        case "6":
            status = input(f"Введите статус книги ({IN}/{OUT}): ")

            for book in library:
                if book[2] == status:
                    print(f"{book[0]} - {book[1]} - {book[2]}")
        case _:
            print("Некорректный ввод. Попробуйте еще раз.")


#
# while True:
#     choice = input(
#         "Выберите действие:\n"
#         "1 - Показать все книги\n"
#         "2 - Добавить книгу\n"
#         "3 - Удалить книгу\n"
#         "4 - Изменить статус книги\n"
#         "5 - Найти книгу по автору\n"
#         "6 - Найти книгу по статусу\n"
#         "0 - Выход\n"
#         "Ваш выбор: "
#     )
#
#     if choice == "1":
#         for book in library:
#             print(f"{book[0]} - {book[1]} - {book[2]}")
#
#     elif choice == "2":
#         name = input("Введите название книги: ")
#         author = input("Введите автора книги: ")
#         library.append([name, author, IN])
#
#     elif choice == "3":
#         name = input("Введите название книги: ")
#         target_book = None
#         for book in library:
#             if book[0] == name:
#                 target_book = book
#                 break  # Прерываем цикл при первом совпадении
#
#         if target_book:
#             answer = input("Вы уверены, что хотите удалить книгу? (да/нет): ")
#             if answer.lower() == "да":
#                 library.remove(target_book)
#         else:
#             print("Книга не найдена.")
#
#     elif choice == "4":
#         name = input("Введите название книги: ")
#         target_book = None
#         for book in library:
#             if book[0] == name:
#                 target_book = book
#                 break  # Прерываем цикл при первом совпадении
#
#         if target_book:
#             target_book[2] = OUT if target_book[2] == IN else IN
#         else:
#             print("Книга не найдена.")
#
#     elif choice == "5":
#         author = input("Введите автора книги: ").strip().lower()
#         found = False
#         for book in library:
#             if book[1].strip().lower() == author:
#                 print(f"{book[0]} - {book[1]} - {book[2]}")
#                 found = True
#         if not found:
#             print("Книги данного автора не найдены.")
#
#     elif choice == "6":
#         status = input(f"Введите статус книги ({IN}/{OUT}): ").strip()
#         found = False
#         for book in library:
#             if book[2] == status:
#                 print(f"{book[0]} - {book[1]} - {book[2]}")
#                 found = True
#         if not found:
#             print("Книг с таким статусом не найдено.")
#
#     elif choice == "0":
#         print("Выход из программы.")
#         break
#
#     else:
#         print("Некорректный ввод. Попробуйте еще раз.")