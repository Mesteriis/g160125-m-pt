# Что исправлено и улучшено?
# Используется sys.exit(0) при выходе вместо break для корректного завершения программы.
# Добавлена обработка ошибок в методах add_task, del_task, mark_task. Теперь если ввод неверный (например, текст вместо числа), программа не падает.
# Используется next(..., None) в find_task, что делает код более читаемым.
# Вывод tasks.json отформатирован (indent=4), чтобы файл был читаемым.
# Метод mark_task принимает task_id, а не объект. Это удобнее при работе с ID.
# Обновлён created_at в Task: теперь корректно работает и с datetime, и с float.
# Используется strip() для очистки ввода в add_task, чтобы не было пустых пробелов.

import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Optional

ROOT_DIR = Path(__file__).parent


class Task:
    def __init__(
            self,
            id: int,
            name: str,
            description: str,
            is_done: bool,
            created_at: float | datetime = None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.is_done = is_done
        self.created_at = (
            datetime.now(tz=timezone.utc) if created_at is None
            else datetime.fromtimestamp(created_at) if isinstance(created_at, (int, float))
            else created_at
        )

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Task) and self.id == other.id

    def __str__(self) -> str:
        status = "complete" if self.is_done else "incomplete"
        return f"{self.id} - Task: {self.name}, {status}, {self.created_at.isoformat()}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_done": self.is_done,
            "created_at": self.created_at.timestamp(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            is_done=data["is_done"],
            created_at=data["created_at"],
        )


class Manager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.last_id = 0
        self.settings = self.load_settings()
        self.load_tasks_from_file()

    def load_tasks_from_file(self) -> None:
        path = Path(self.settings.get("path_db", ROOT_DIR / "tasks.json"))
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                tasks = json.load(f)
            self.tasks = [Task.from_dict(task) for task in tasks]
            self.tasks.sort(key=lambda task: task.id)
            self.last_id = self.tasks[-1].id if self.tasks else 0

    def save_tasks_to_file(self) -> None:
        path = Path(self.settings.get("path_db", ROOT_DIR / "tasks.json"))
        with open(path, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self) -> Optional[Task]:
        try:
            self.last_id += 1
            data = {
                "id": self.last_id,
                "name": input("Enter task name: ").strip(),
                "description": input("Enter task description: ").strip(),
                "is_done": False,
                "created_at": datetime.now(tz=timezone.utc).timestamp(),
            }
            task = Task.from_dict(data)
            self.tasks.append(task)
            self.save_tasks_to_file()
            return task
        except Exception as e:
            print(f"Error adding task: {e}")
            return None

    def del_task(self, task_id: int) -> Optional[Task]:
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks_to_file()
            print(f"Task {task_id} deleted.")
            return task
        print(f"Task {task_id} not found.")
        return None

    def find_task(self, task_id: int) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)

    def mark_task(self, task_id: int) -> Optional[Task]:
        task = self.find_task(task_id)
        if task:
            task.is_done = not task.is_done
            self.save_tasks_to_file()
            print(f"Task {task_id} marked as {'complete' if task.is_done else 'incomplete'}.")
            return task
        print(f"Task {task_id} not found.")
        return None

    def show_tasks(self) -> None:
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    @staticmethod
    def load_settings() -> dict:
        path = ROOT_DIR / "settings.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"path_db": str(ROOT_DIR / "tasks.json")}


def main() -> None:
    manager = Manager()

    while True:
        print("\n1. Add task")
        print("2. Delete task")
        print("3. Mark task as done/undone")
        print("4. Show tasks")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            try:
                task_id = int(input("Enter task id: ").strip())
                manager.del_task(task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == "3":
            try:
                task_id = int(input("Enter task id: ").strip())
                manager.mark_task(task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == "4":
            manager.show_tasks()
        elif choice == "5":
            manager.save_tasks_to_file()
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
