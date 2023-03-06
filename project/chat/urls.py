from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.Index.as_view()),
    path('token/', obtain_auth_token),
    path("<str:room_name>/", views.room, name="room"),
]