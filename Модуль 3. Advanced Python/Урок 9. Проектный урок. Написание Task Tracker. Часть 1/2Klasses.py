import json
import datetime

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=2)

    def add_task(self, text):
        self.tasks.append({
            "text": text,
            "done": False,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def toggle_task_status(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            return True
        return False

class App:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def show_tasks(self):
        tasks = self.task_manager.tasks
        if not tasks:
            print("Список задач пуст.")
        else:
            for index, task in enumerate(tasks, start=1):
                status = "GOOD!" if task["done"] else "not good"
                print(f"{index}. {status} {task['text']} (Добавлено: {task['created_at']})")

    def run(self):
        while True:
            print("\n1. Показать задачи")
            print("2. Добавить задачу")
            print("3. Удалить задачу")
            print("4. Отметить выполненной/невыполненной")
            print("5. Выйти")

            choice = input("Выберите действие: ").strip()

            if choice == "1":
                self.show_tasks()
            elif choice == "2":
                text = input("Введите новую задачу: ").strip()
                if text:
                    self.task_manager.add_task(text)
            elif choice == "3":
                self.show_tasks()
                try:
                    index = int(input("Введите номер задачи для удаления: ")) - 1
                    if not self.task_manager.delete_task(index):
                        print("Такой задачи нет.")
                except ValueError:
                    print("Ошибка: введите число.")
            elif choice == "4":
                self.show_tasks()
                try:
                    index = int(input("Введите номер задачи для изменения статуса: ")) - 1
                    if not self.task_manager.toggle_task_status(index):
                        print("Такой задачи нет.")
                except ValueError:
                    print("Ошибка: введите число.")
            elif choice == "5":
                self.task_manager.save_tasks()
                print("Сохранено. До свидания!")
                break
            else:
                print("Неверный выбор, попробуйте ещё раз.")

def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            config = json.load(file)
            return config.get("tasks_file", "tasks.json")
    except (FileNotFoundError, json.JSONDecodeError):
        return "tasks.json"

if __name__ == "__main__":
    tasks_file = load_config()
    manager = TaskManager(tasks_file)
    app = App(manager)
    app.run()
