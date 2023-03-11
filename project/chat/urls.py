from django.urls import path

from . import views


urlpatterns = {
    path('', views.auth),
    path('registration/', views.registration),
    # path("<str:room_name>/", views.room, name="room"),
}