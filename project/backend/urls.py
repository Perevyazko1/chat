from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

from .views import UserProfileListCreateView, userProfileDetailView, \
    RoomViewSet, MessageViewSet, Index, ImageViewSet

# router = routers.DefaultRouter()
# router.register(r'avatar', ImageViewSet)
urlpatterns = [
    # path('', include(router.urls)),
    path(r"profile/", UserProfileListCreateView.as_view(),name="profile"),
    path("profile/<int:pk>", userProfileDetailView.as_view(),name="profile"),
    # path("send_message", MessageViewSet.as_view({'post': 'create'}), name="send_message"),
    path("list_message_room/<int:pk>", MessageViewSet.as_view(), name="list_message_room"),
    path("create_room", RoomViewSet.as_view({'post': 'create'}), name="create_room"),
    path("rooms_list", RoomViewSet.as_view({'get': 'list'}), name="rooms_list"),
    path('auth_api/', Index.as_view()),
    path('token/', obtain_auth_token),
    path(r'avatar/', ImageViewSet.as_view()),
    # path('upload/', uploadImage, name="image-upload"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#imp for what you want to achieve.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)