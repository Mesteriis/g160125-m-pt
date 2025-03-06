import json
import datetime

FILENAME = "tasks.json"

def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "ok" if task["done"] else "not ok"
            print(f"{index}. {status} {task['text']} (Добавлено: {task['created_at']})")

def add_task(tasks):
    text = input("Введите новую задачу: ").strip()
    if text:
        tasks.append({
            "text": text,
            "done": False,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

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

def toggle_task_status(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Введите номер задачи для изменения статуса: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = not tasks[index]["done"]
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
        print("4. Отметить выполненной/невыполненной")
        print("5. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            toggle_task_status(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Сохранено в tasks.json. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")

if __name__ == "__main__":
    main()
