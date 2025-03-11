import json
from icecream import ic as print

def dict_to_json(python_object: dict, file):
    json.dump(python_object, file)


def json_to_dict(file: str) -> dict:
    return json.load(file)


def main():
    # Пример объекта Python
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }

    # Преобразование объекта Python в строку JSON
    with open('data.json', 'w') as file:
        dict_to_json(data, file)

    with open('data.json', 'r') as file:
        python_object = json_to_dict(file)
        print(python_object)


if __name__ == '__main__':
    main()