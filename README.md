# async_weather
Project for learning asyncio

### Описание проекта
Проект для изучения библиотеки asyncio и aiohttp позволяет узнать
погоду в городах из списка cities с использованием сервиса
openweathermap.org.
Код в файле `main.py` асинхронно получает информацию о погоде для каждого города из списка и выводит результат в консоль.
Для сравнения скорости выполнения в файле `main_requests.py` реализована аналогичная задача с использованием библиотеки requests.
