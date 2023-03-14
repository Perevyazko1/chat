from django.urls import path

from .views import auth, registration,profile


urlpatterns = {
    path('auth/', auth),
    path('registration/', registration),
    path('myprofile/', profile),
    # path("<str:room_name>/", views.room, name="room"),
}