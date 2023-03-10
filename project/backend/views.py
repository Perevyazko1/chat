from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


from .permissions import IsOwnerProfileOrReadOnly


from rest_framework import viewsets

from .serializers import MessageSerializer, userProfileSerializer, RoomSerializer
from .models import Message, Room, userProfile


class UserProfileListCreateView(ListCreateAPIView):
    """Создание Пользователя RESTAPI"""
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    """Просмотр Пользователя RESTAPI"""
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]


class MessageViewSet(ListCreateAPIView):
    """Создание Сообщения RESTAPI"""
    queryset = Message.objects.all().order_by('dateCreation')
    serializer_class = MessageSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    """Создание Комнаты RESTAPI"""
    queryset = Room.objects.all().order_by('name_room')
    serializer_class = RoomSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


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
