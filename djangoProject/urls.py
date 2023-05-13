from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path
from market.cookie import logout_views, login_views
from views_weather import show_weather
from views_name import name
from market.views import show_audi, show_name, audi_purchase, audi_payment


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('weather', show_weather),
    path('audi', show_audi),
    path('buy_car/<int:id_>', audi_purchase),
    path('payment/<int:id_>', audi_payment),
    path('name', name),
    path('Database', show_name),
    path('login', login_views),
    path('logout', logout_views),

]
