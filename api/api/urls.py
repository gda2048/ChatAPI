"""api URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Chat API')

urlpatterns = [
    re_path(r'^$', schema_view, name='api'),
    path('admin/', admin.site.urls),
]
