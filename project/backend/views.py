from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User


from .permissions import IsOwnerProfileOrReadOnly


from rest_framework import viewsets

from .serializers import MessageSerializer, userProfileSerializer, RoomSerializer, ImageSerializer
from .models import Message, Room, userProfile


class UserProfileListCreateView(ListCreateAPIView):
    """Создание Пользователя RESTAPI"""
    queryset = User.objects.all()
    serializer_class = userProfileSerializer
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(user=user)


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
            'auth': str(request.auth),
            'name': str(request.user.first_name)# None
        }
        return Response(content)


class ImageViewSet(RetrieveUpdateDestroyAPIView):
    # http_method_names = ['get', 'put']
    queryset = userProfile.objects.all()
    serializer_class = ImageSerializer
    pagination_class = None

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

# @api_view(['POST'])
# def uploadImage(request):
#     data = request.data
#
#     obj_id = data['obj_id']
#     obj= userProfile.objects.get(id=obj_id)
#
#     obj.image = request.FILES.get('image')
#     obj.save()
#
#     return Response('Image was uploaded')