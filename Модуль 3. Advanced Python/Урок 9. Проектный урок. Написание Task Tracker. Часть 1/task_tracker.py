FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Введите новую задачу: ").strip()
    if task:
        tasks.append(task)

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
        else:
            print("Такой задачи нет.")
    except ValueError:
        print("Ошибка: введите число.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Сохранено. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")

if __name__ == "__main__":
    main()
