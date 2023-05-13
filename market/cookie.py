from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def login_views(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "login.html", context={"message": "Wrong username or password"})

        login(request, user)
        return HttpResponseRedirect("/audi")

    return render(request, "login.html")


def logout_views(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect("/audi")
