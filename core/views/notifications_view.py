# core/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from core.models.notification import Notification

def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    notification.read = True
    notification.save()
    return JsonResponse({'success': True})
