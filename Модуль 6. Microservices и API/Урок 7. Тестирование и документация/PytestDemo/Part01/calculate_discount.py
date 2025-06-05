def calculate_discount(price: float, discount: int) -> float:
    """
    Вычисляет цену со скидкой.

    Args:
        price: Исходная цена.
        discount: Процент скидки (целое число).

    Returns:
        Цена со скидкой.
    """
    if discount < 0 or discount > 100:
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100.")
    return price * (1 - discount / 100)
