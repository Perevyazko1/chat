from rest_framework import serializers

from .models import Message, Room, userProfile
from django.contrib.auth.models import User


class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'user', 'first_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('name_room',)