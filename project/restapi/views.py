from rest_framework import viewsets

from .serializers import MessageSerializer, UserSerializer, RoomSerializer
from .models import Message, Room
from django.contrib.auth.models import User


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('dateCreation')
    serializer_class = MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('name_room')
    serializer_class = RoomSerializer