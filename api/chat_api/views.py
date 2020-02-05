from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import permissions, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from chat_api.serializers import MessageSerializer
from chat_api.models import Message


class IsMessageAvailable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Check if message is available for the user.
        """
        if request.method in ['GET', 'DELETE']:
            return request.user in [obj.sender, obj.receiver]
        if request.method == 'PUT':
            return request.user == obj.receiver
        return request.user == obj.sender


class MessageViewSet(mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    Message related APIs.

    list: Returns messages got by the user or ?is_read=False is specified only unread got messages.
    retrieve: Returns message by its id to the sender or receiver.
    create: Create new message.
    delete: Deletes created message by its id.
    """
    serializer_class = MessageSerializer

    def get_queryset(self):
        is_read = self.request.query_params.get('is_read')
        if is_read == 'False':
            return Message.objects.filter(receiver=self.request.user, is_read=False)
        return Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))

    permission_classes = [permissions.IsAuthenticated, IsMessageAvailable]

    @action(detail=True, methods=['put'], serializer_class=Serializer)
    def read(self, request, pk=None):
        message = self.get_object()
        message.is_read = True
        message.save()
        return Response(MessageSerializer(message).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], serializer_class=MessageSerializer,
            url_path='create/(?P<username>[^/.]+)')
    def create_user(self, request, username, pk=None):
        """
        Create a new message to other existed user or to the sender.
        """
        try:
            receiver = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(data={"errors": ["User is not found"]},
                            status=status.HTTP_404_NOT_FOUND)
        serialized = MessageSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save(receiver=receiver, sender=request.user)
        return Response(serialized.data, status=status.HTTP_200_OK)
