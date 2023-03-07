from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,TokenAuthentication


class Index(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        return render(request, "index.html")

def index(request):
    return render(request, "index.html")
# class Index(APIView):
#     # permission_classes = (IsAuthenticated,)
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     def post(self, request):
#         print(f'юзер{request.user}')
#         content = {'message': 'Hello, World!'}
#         return Response(content)

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})