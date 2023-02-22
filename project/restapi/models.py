from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    class Meta:
        verbose_name = u"Комната"
        verbose_name_plural = u"Комнаты"
    name_room = models.TextField(verbose_name='Название комнаты')

    def __str__(self):
        return f'{self.name_room} {self.pk}'


class Message(models.Model):
    class Meta:
        verbose_name = u"Сообщение"
        verbose_name_plural = u"Сообщения"

    messageUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    messageText = models.TextField(verbose_name='Сообщение')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната')

    def __str__(self):
        return f'{self.messageUser} : {self.messageText}'


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to='images/', default=None)