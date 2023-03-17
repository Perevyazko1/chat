from django.urls import path

from .views import auth, registration,profile, room


urlpatterns = {
    path('', auth),
    path('registration/', registration),
    path('myprofile/', profile),
    path("room/<str:room_name>/", room, name="room"),
}