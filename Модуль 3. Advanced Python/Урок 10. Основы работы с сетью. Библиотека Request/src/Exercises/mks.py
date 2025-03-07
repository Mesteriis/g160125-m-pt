# Выполнить запрос и получить текущие координаты МКС и состав экипажа
# вывести результаты в понятном для человека виде
# сайт с информацией http://api.open-notify.org

import requests

coords_url = "http://api.open-notify.org/iss-now.json"
response = requests.get(coords_url)
coords_data = response.json()

latitude = coords_data['iss_position']['latitude']
longitude = coords_data['iss_position']['longitude']

crew_url = "http://api.open-notify.org/astros.json"
response = requests.get(crew_url)
crew_data = response.json()

iss_crew = [astronaut['name'] for astronaut in crew_data['people'] if astronaut['craft'] == 'ISS']

print("Текущие координаты МКС:")
print(f"  Широта: {latitude}°")
print(f"  Долгота: {longitude}°")
print()

print("Состав экипажа на борту МКС:")
if iss_crew:
    for i, name in enumerate(iss_crew, start=1):
        print(f"  {i}. {name}")
else:
    print("Не удалось получить данные об экипаже.")

