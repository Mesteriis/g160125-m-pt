import asyncio


async def hello():
    print("Привет!")
    await asyncio.sleep(2)  # иди дальше, я посплю 2 секунды
    print("Пока!")

def some_function():
    print("Это обычная функция, которая не ждет ничего.")

# Корутина - не сама функция, а то, что возвращается функция с await
print(type(hello()))
print(type(some_function))
