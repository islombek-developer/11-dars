import asyncio
import httpx
import time
start = time.perf_counter()
text_urls = [
    'https://uz.wikipedia.org/wiki/Arslon',
    'https://bank.uz/currency#RUB',
    'https://www.bbc.com/news'
]
try:
    async def fetch(url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.text

    async def main():
        tasks = [fetch(url) for url in text_urls]
        results = await asyncio.gather(*tasks)
        for result in results:

            print(result)
except Exception as e:
    print(f'{e} qandaydir hatolik')
asyncio.run(main())
end = time.perf_counter()
print(f'{end-start} tugadi')