from rest_framework import serializers

from .models import Message, Room, userProfile
from django.contrib.auth.models import User
from django.core.files import File
import base64


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


class ImageSerializer(serializers.ModelSerializer):

    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = userProfile
        fields = '__all__'

    def get_base64_image(self, obj):
        f = open(obj.avatar.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data