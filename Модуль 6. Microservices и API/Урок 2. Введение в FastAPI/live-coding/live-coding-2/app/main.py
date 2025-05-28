# Импортируем класс FastAPI для создания приложения и класс HTTPException для выброса HTTP-ошибок
from fastapi import FastAPI, HTTPException

# pydantic обеспечивает валидацию данных и удобную работу с JSON-схемами
from pydantic import BaseModel


# Создаём экземпляр FastAPI-приложения — это будет наша «точка входа» для обработки запросов
app = FastAPI()


# Описываем модель данных для задачи (Task), наследуясь от BaseModel из pydantic.
# Эта модель автоматически выполняет валидацию входящих данных при запросах
class Task(BaseModel):
    # Обязательное поле 'title' типа строка
    title: str
    # Необязательное поле 'description' (может быть None или строкой)
    description: str | None = None


# Используем словарь как простое хранилище для задач (вместо БД).
# Ключом будет ID задачи, значением — объект Task
tasks_db = {}


# Обработчик для создания новой задачи.
# Метод POST означает добавление ресурса.
@app.post("/tasks")
def create_task(task: Task):
    # Генерируем ID, как длину словаря + 1 (простой способ, не для продакшена)
    task_id = len(tasks_db) + 1
    # Сохраняем Task в "базе" (словарь)
    tasks_db[task_id] = task
    # Возвращаем ответ, включающий ID задачи и её данные
    return {"task_id": task_id, "task": task}


# Обработчик для получения списка всех задач.
# Метод GET означает чтение ресурса.
@app.get("/tasks")
def get_tasks():
    # Возвращаем весь словарь со всеми задачами
    return {"tasks": tasks_db}


# Обработчик для получения задачи по её ID
# {task_id} в маршруте означает, что часть URL подставится в параметр функции
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Если ключа (ID задачи) нет в словаре, выбрасываем HTTP-ошибку 404 (Not Found)
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    # Возвращаем найденную задачу
    return {"task_id": task_id, "task": tasks_db[task_id]}


# Обработчик для обновления задачи по её ID
# Метод PUT означает полное обновление ресурса
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    # Проверяем, существует ли задача в "базе"
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    # Перезаписываем данные задачи на новые, пришедшие в теле запроса
    tasks_db[task_id] = task
    # Возвращаем сообщение об успехе и обновлённую задачу
    return {"message": "Task updated successfully", "task": tasks_db[task_id]}


# Обработчик для удаления задачи по её ID
# Метод DELETE означает удаление ресурса
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Если задачи с таким ID не существует — HTTP-ошибка 404
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    # Удаляем запись из словаря
    del tasks_db[task_id]
    # Возвращаем сообщение об успешном удалении
    return {"message": "Task deleted successfully"}
