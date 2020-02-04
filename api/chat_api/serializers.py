from django.contrib.auth.models import User
from rest_framework import serializers

from chat_api.models import Message


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the default User model.
    """

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'date_joined',
                  'last_login')
        read_only_fields = ('username', 'email', 'date_joined', 'last_login')


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Messages.
    """
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ("pk", "sender", "receiver", "message", 'subject', 'is_read', 'creation_date')
        read_only_fields = ('sender', 'creation_date', 'is_read')
