def my_max(numbers: list[int | float]) -> int | float:
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number
