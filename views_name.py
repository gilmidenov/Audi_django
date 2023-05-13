from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def name(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        name = request.POST.get("name", "")
        age = int(request.POST.get("age", "0"))
        return render(request, "name.html", {"name": name, "age": age})
    return render(request, "name.html")
