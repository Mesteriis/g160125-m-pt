# Продемонстрируйте и объясните в режиме live-coding работу рекурсивных функций

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

data = {
    1: 1,
    2: 22,
    3: {
            1: 1,
            2: 23,
            3: {
                1: 1,
                2: 24,
                3: {
                    1: 1,
                    2: 25,
                    3: {
                        1: 1,
                        2: 26,
                }
            }
            },
            5: [
        1, 2, 3, {
            1: 1,
            2: 2,
            3: 6,

        }
    ],
        },
    4: [
        1, 2, 3,
    ],
}

def recursive_find_keys_two(data: dict) -> list:
    answer = []
    for key, value in data.items():
        if type(value) == dict:
            answer.extend(recursive_find_keys_two(value))
        elif key == 2:
            answer.append(value)
    return answer

print(recursive_find_keys_two(data))