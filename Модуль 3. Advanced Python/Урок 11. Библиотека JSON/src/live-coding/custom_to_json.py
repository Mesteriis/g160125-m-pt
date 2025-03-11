import json
from icecream import ic as print

class myclass:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.age} {self.score}"

    def __str__(self):
        return f"{self.name} {self.age} {self.score}"

    def __dict__(self):
        return {"name": self.name, "age": self.age, "score": self.score}

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(data['name'], data['age'], data['score'])

def main():
    obj = myclass("John", 30, 100)
    print(obj.__dict__())
    print(json.dumps(obj.__dict__()))


if __name__ == '__main__':
    main()
