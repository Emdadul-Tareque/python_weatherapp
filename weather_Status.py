import requests

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=ae3d727915c75c73ea4f88acf79810eb"


def get_weather(city_name):
    response = requests.get(url.format(city_name))
    data = response.json()

    return {'city': data["name"],
            'icon': data["weather"][0]["icon"],
            'weather': data["weather"][0]["description"],
            'temp': data["main"]["temp"]-273

             }


