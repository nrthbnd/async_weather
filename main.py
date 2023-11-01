import asyncio
import os
import time

from aiohttp import ClientSession
from dotenv import load_dotenv

from cities import cities

load_dotenv()


async def get_weather(city):
    async with ClientSession() as session:
        url = os.getenv('API_URL')
        params = {'q': city, 'APPID': os.getenv('APP_ID')}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            print(f'{city}: {weather_json["weather"][0]["main"]}')


async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))

    for task in tasks:
        await task


print(time.strftime('%X'))

asyncio.run(main(cities))

print(time.strftime('%X'))
