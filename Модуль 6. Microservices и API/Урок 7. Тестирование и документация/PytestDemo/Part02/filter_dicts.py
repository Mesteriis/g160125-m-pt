def filter_dicts(data: list, key: str, value: any) -> list:
    """Фильтрует список словарей по заданному ключу и значению."""
    return [item for item in data if item.get(key) == value]
