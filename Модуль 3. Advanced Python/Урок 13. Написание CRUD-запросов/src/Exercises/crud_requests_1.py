# Через библиотеку requests выполнить GET запрос к корневому адресу.
# Выполнить GET запрос к серверу – получить список заданий.
# Выполнить POST запрос к серверу – добавить в список два задания (разных).
# Выполнить GET запрос к серверу – получить задание с номером 2.
# Выполнить GET запрос к серверу – получить список заданий.
# Выполнить PUT запрос к серверу – изменить одно из заданий.
# Выполнить GET запрос к серверу – получить список заданий.
from http.client import responses

# Смотрите на документацию к API по адресу http://127.0.0.1:8085/docs

# import requests
# import lorem
#
# def get_root(address: str) -> (int, str):
#     response = requests.get(address)
#     return response.status_code, response.text
#
# def get_task_list(root_address:str) -> (int, str):
#     response = requests.get(root_address + "/todo")
#     return response.status_code, response.json()
#
# def add_newt_ask(root_address:str, task_id:int, task_name:str)->(int, str):
#     data = {
#         "id":task_id,
#         "item":task_name
#     }
#
#     response = requests.post(root_address+"todo", json=data)
#     return response.status_code, response.text
#
# def update_task(root_address:str, task_id: int, new_text: str):
#     data={
#         "item":new_text
#     }
#     response=requests.put(root_address+"/todo/"+str(task_id), json=data)
#     return response.status_code, response.text
#
# def main():
#     root_address="http://127.0.0.1:8085/"
#     response=get_root(address=root_address)
#     print(response[0])
#     print(response[1])
#     response=get_task_list(root_address=root_address)
#     print(response[0])
#
#     for item in response[1]["todos"]:
#         print(item)
#
#     for i in range(3):
#         text=lorem.sentence()
#         print(f"adding new task")
#         response=add_newt_ask(root_address=root_address, task_id=i, task_name=text)
#         print(response[0])
#         print(response[1])
#
#     response=get_task_list(root_address=root_address)
#     print(response[0])
#
#     for item in response[1]["todos"]:
#         print(item)
#
#     response=update_task(root_address=root_address, task_id=2, new_text="new text")
#
#     print(response[0])
#     print(response[1])
#
#
# if __name__ == '__main__':
#     main()

import requests

BASE_URL = "http://127.0.0.1:8085"

# 1. Выполнить GET запрос к корневому адресу
response = requests.get(BASE_URL)
print("GET /", response.status_code, response.json())

# 2. Получить список заданий
response = requests.get(f"{BASE_URL}/tasks")
print("GET /tasks", response.status_code, response.json())

# 3. Добавить два задания
task1 = {"title": "Купить продукты", "description": "Купить молоко и хлеб"}
task2 = {"title": "Позвонить другу", "description": "Узнать, как у него дела"}

response1 = requests.post(f"{BASE_URL}/tasks", json=task1)
print("POST /tasks", response1.status_code, response1.json())

response2 = requests.post(f"{BASE_URL}/tasks", json=task2)
print("POST /tasks", response2.status_code, response2.json())

# 4. Получить задание с номером 2
response = requests.get(f"{BASE_URL}/tasks/2")
print("GET /tasks/2", response.status_code, response.json())

# 5. Получить список заданий после добавления
response = requests.get(f"{BASE_URL}/tasks")
print("GET /tasks", response.status_code, response.json())

# 6. Изменить одно из заданий (например, задание с ID 1)
updated_task = {"title": "Купить продукты и овощи", "description": "Молоко, хлеб, помидоры, огурцы"}
response = requests.put(f"{BASE_URL}/tasks/1", json=updated_task)
print("PUT /tasks/1", response.status_code, response.json())

# 7. Получить список заданий после изменения
response = requests.get(f"{BASE_URL}/tasks")
print("GET /tasks", response.status_code, response.json())
