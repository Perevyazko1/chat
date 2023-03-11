from rest_framework import serializers

from .models import Message, Room, userProfile
from django.contrib.auth.models import User


class userProfileSerializer(serializers.ModelSerializer):
    # user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=User
        fields='__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('name_room',)