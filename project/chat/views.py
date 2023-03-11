from django.shortcuts import render


def auth(request):
    """Авторизация вход и создание чата"""
    return render(request, "index.html")


def room(request, room_name):
    """Переписка в чате"""
    return render(request, "room.html", {
        "room_name": room_name
    })


def registration(request):
    """Регистрация вход и создание чата"""
    return render(request, "registration.html")
