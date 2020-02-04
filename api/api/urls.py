"""api URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view
from chat_api.urls import message_router

schema_view = get_swagger_view(title='Chat API')

admin.site.site_header = 'Chat API'
admin.site.site_title = 'Chat API'
admin.site.index_title = 'Welcome to Chat API'

urlpatterns = [
    re_path(r'^$', schema_view, name='api'),
    path('admin/', admin.site.urls),
] + message_router.urls
