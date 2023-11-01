# Реализация без использования асинхронных библиотек.
import os
import time

import requests
from dotenv import load_dotenv

from cities import cities

load_dotenv()


def get_weather(city):
    url = os.getenv('API_URL')
    params = {'q': city, 'APPID': os.getenv('APP_ID')}

    weather_json = requests.get(url=url, params=params).json()
    print(f'{city}: {weather_json["weather"][0]["main"]}')


def main(cities_):
    for city in cities_:
        get_weather(city)


print(time.strftime('%X'))

main(cities)

print(time.strftime('%X'))
