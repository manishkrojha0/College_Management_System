# core/urls.py

from django.urls import path
from core.views.notifications_view import mark_notification_as_read
from core.views.teacher_view import TeacherListView, TeacherDetailView
from core.views.student_view import StudentDetailView, StudentListView
from core.views.classes_view import ClassDetailView, ClassListView


urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),
    path('notifications/<int:notification_id>/mark-as-read/', mark_notification_as_read, name='mark_notification_as_read'),
]
