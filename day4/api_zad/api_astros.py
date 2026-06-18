# { "name":"John", "age":30, "city":"New York"}
# REST API
# Do komunikacji wykorzystywane są standardowe metody HTTP
# :GET: Pobieranie danych (np. lista użytkowników).
# POST: Tworzenie nowego zasobu (np. rejestracja konta).
# PUT / PATCH: Aktualizacja zasobu (całości lub części).
# DELETE: Usuwanie zasobu.
# https://github.com/public-apis/public-apis
from typing import List

import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx - ok
# 3xx warningi, przekierowania
# 4xx - 404 - brak strony, 400 Bad Request
# 5xx - błedy po stronie serwera

print(response.text)

response_data = response.json()
print(response_data)

# klucze ze słownika
for i in response_data:
    print(i)
# people
# number
# message

from pydantic import BaseModel


class Astronaut(BaseModel):
    name: str
    craft: str


class AstroData(BaseModel):
    message: str
    people: List[Astronaut]
    number: int
    # number: str


data = AstroData(**response.json())
print(data)

for astronaut in data.people:
    print(f"Name: {astronaut.name}, craft: {astronaut.craft} ")
# Name: Oleg Kononenko, craft: ISS
# Name: Nikolai Chub, craft: ISS
# Name: Tracy Caldwell Dyson, craft: ISS
# Name: Matthew Dominick, craft: ISS
# Name: Michael Barratt, craft: ISS
# Name: Jeanette Epps, craft: ISS
# Name: Alexander Grebenkin, craft: ISS
# Name: Butch Wilmore, craft: ISS
# Name: Sunita Williams, craft: ISS
# Name: Li Guangsu, craft: Tiangong
# Name: Li Cong, craft: Tiangong
# Name: Ye Guangfu, craft: Tiangong
