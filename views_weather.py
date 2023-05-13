import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def show_weather(request:HttpRequest) -> HttpResponse:
    temperature = random.randint(-40, 40)
    return render(request, "weather.html", {"temperature": temperature})
