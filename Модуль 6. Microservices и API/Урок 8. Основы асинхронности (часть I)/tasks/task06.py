import asyncio
import aiohttp
import time

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            data = await response.text()
            return url, data
    except Exception as e:
        return url, f"Error: {e}"

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in pending:
            task.cancel()
        await asyncio.gather(*pending, return_exceptions=True)
        return list(done)[0].result()

if __name__ == "__main__":
    urls = [
        "https://www.yandex.com",
        "https://www.google.com",
        "https://www.python.org",
    ]

    start_time = time.time()
    url, content = asyncio.run(main(urls))
    end_time = time.time()

    print(f"Первым ответил: {url}, получено {len(content)} байт")
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")