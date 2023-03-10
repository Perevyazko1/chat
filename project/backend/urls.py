from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserProfileListCreateView, userProfileDetailView, \
    RoomViewSet, MessageViewSet, Index

urlpatterns = [
    path("all-profiles", UserProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/<int:pk>", userProfileDetailView.as_view(),name="profile"),
    # path("send_message", MessageViewSet.as_view({'post': 'create'}), name="send_message"),
    path("list_message_room/<int:pk>", MessageViewSet.as_view(), name="list_message_room"),
    path("create_room", RoomViewSet.as_view({'post': 'create'}), name="create_room"),
    path("rooms_list", RoomViewSet.as_view({'get': 'list'}), name="rooms_list"),
    path('auth_api/', Index.as_view()),
    path('token/', obtain_auth_token),

]