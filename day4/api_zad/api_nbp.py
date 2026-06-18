import asyncio
import aiohttp
import time


# https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/

# url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/"


async def fetch(url, session, index):
    async with session.get(url, ssl=False) as response:
        text = await response.text()
        print(f"Text: {text}")


async def measure_aiohttp():
    url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/"

    tasks = []
    overall_st = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        for i in range(100):
            tasks.append(fetch(url, session, i + 1))

        statuses = await asyncio.gather(*tasks)

    overall_et = time.perf_counter() - overall_st
    print(f"Overall time for requests: {overall_et}")
    return statuses


# uruchomienie funkcji asynchronicznej
asyncio.run(measure_aiohttp())
