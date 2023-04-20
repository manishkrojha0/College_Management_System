# core/urls.py

from django.urls import path
from core.views.notifications_view import mark_notification_as_read

urlpatterns = [

    path('notifications/<int:notification_id>/mark-as-read/', mark_notification_as_read, name='mark_notification_as_read'),
    
]
