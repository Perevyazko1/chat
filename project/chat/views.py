from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class Index(APIView):
    """Авторизация и передача токена"""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


def auth(request):
    """Авторизация вход и создание чата"""
    return render(request, "index.html")


def room(request, room_name):
    """Переписка в чате"""
    return render(request, "room.html", {
        "room_name": room_name
    })
