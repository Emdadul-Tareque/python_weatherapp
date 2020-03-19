from django.http import HttpRequest
from django.shortcuts import render
from weather_Status import get_weather


def index(request: HttpRequest):
    cites = ["Dhaka", "Chittagong", "London", "Berlin"]

    context = {
        'cites': [get_weather(city) for city in cites]
    }

    return render(request, 'index.html', context)
