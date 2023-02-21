from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'create_room', views.RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]