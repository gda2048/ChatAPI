from rest_framework.routers import DefaultRouter

from chat_api.views import MessageViewSet

message_router = DefaultRouter()
message_router.register(r'messages', MessageViewSet, basename='messages')
