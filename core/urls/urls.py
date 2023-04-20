# core/urls.py

from django.urls import path
from core.views.notifications_view import mark_notification_as_read
from . import views

urlpatterns = [
    path('teachers/', views.TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('classes/', views.ClassListView.as_view(), name='class-list'),
    path('classes/<int:pk>/', views.ClassDetailView.as_view(), name='class-detail'),
    path('notifications/<int:notification_id>/mark-as-read/', mark_notification_as_read, name='mark_notification_as_read'),
]
