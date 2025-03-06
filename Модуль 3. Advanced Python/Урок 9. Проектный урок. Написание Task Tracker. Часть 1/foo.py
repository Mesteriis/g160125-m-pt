import json
from datetime import datetime, timezone
from pathlib import Path

ROOT_DIR = Path(__file__).parent


class Task:
    def __init__(
            self,
            id: int,
            name: str,
            description: str,
            is_done: bool,
            created_at: float = datetime.now(tz=timezone.utc)
    ):
        self.id = id
        self.name = name
        self.description = description
        self.is_done = is_done
        self.created_at = created_at if isinstance(created_at, datetime) else datetime.fromtimestamp(created_at)

    def __eq__(self, other):
        if not isinstance(other, Task):
            return ValueError("Not a Task object")
        return self.id == other.id

    def __str__(self):
        return f"{self.id} - Task: {self.name}, {'complete' if self.is_done else 'incomplete'} {self.created_at.isoformat()}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_done': self.is_done,
            'created_at': self.created_at.timestamp(),
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            id=d['id'],
            name=d['name'],
            description=d['description'],
            is_done=d['is_done'],
            created_at=d['created_at'],
        )


class Manager:
    def __init__(self):
        self.tasks = []
        self.last_id = 0
        self.settings = self.load_settings()
        self.load_tasks_from_file()


    def load_tasks_from_file(self):
        path = Path(self.settings.get('path_db',  ROOT_DIR / 'tasks.json'))
        if not path.exists():
            return []
        with open(path, 'r') as f:
            tasks = json.load(f)
        self.tasks = [Task.from_dict(task) for task in tasks]
        self.tasks.sort(key=lambda task: task.id)
        self.last_id = self.tasks[-1].id if self.tasks else 0

    def save_tasks_to_file(self):
        path = self.settings.get('path_db',  ROOT_DIR / 'tasks.json')
        with open(path, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def __delete__(self):
        self.save_tasks_to_file()


    def add_task(self) -> Task | None:
        try:
            self.last_id += 1
            data = {
                "id": self.last_id,
                "name": input("Enter task name: "),
                "description": input("Enter task description: "),
                "is_done": False,
                "created_at": datetime.now(tz=timezone.utc).timestamp()
            }
            return Task.from_dict(data)
        except:
            return None

    def del_task(self, task: Task | None) -> Task | None:
        if task is None:
            return None
        self.tasks.remove(task)
        return task

    def find_task(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def mark_task(self, task: Task | None) -> Task | None:
        if task is None:
            return None
        task.is_done = not task.is_done
        return task

    def show_tasks(self):
        for task in self.tasks:
            print(task)


    @staticmethod
    def load_settings() -> dict:
        path = ROOT_DIR / 'settings.json'
        if not path.exists():
            return {
                'path_db': ROOT_DIR / 'tasks.json'
            }
        else:
            with open(path, 'r') as f:
                return json.load(f)


def main():
    manager = Manager()
    while True:
        print("1. Add task")
        print("2. Delete task")
        print("3. Mark task")
        print("4. Show tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = manager.add_task()
            if task is not None:
                manager.tasks.append(task)
        elif choice == '2':
            task_id = int(input("Enter task id: "))
            task = manager.find_task(task_id)
            manager.del_task(task)
        elif choice == '3':
            task_id = int(input("Enter task id: "))
            task = manager.find_task(task_id)
            manager.mark_task(task)
        elif choice == '4':
            manager.show_tasks()
        elif choice == '5':
            manager.save_tasks_to_file()
            break
        else:
            print("Invalid choice")
        print()

if __name__ == '__main__':
    main()