import math


def is_prime(number: int) -> bool:
    """
    Является ли число простым
    """
    for divider in range(2, int(math.sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True

