from django.contrib import admin
from chat_api.models import Message


@admin.register(Message)
class CurrencyAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('sender', 'receiver', 'subject')
