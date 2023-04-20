from core.models.base_model import BaseModel
from core.models import student, teacher
from django.db import models
from .notification import Notification
import datetime
from django.urls import reverse

class Classes(BaseModel):
    """Class Model."""
    
    name = models.CharField(max_length=255)
    teacher_class = models.ManyToManyField(teacher.Teacher, related_name='teacher_class')
    student_class = models.ManyToManyField(student.Student, related_name='student_class')
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class_detail', args=[str(self.id)])

    def get_students_for_today(self):
        today = datetime.now().date()
        students_for_today = self.student_class.filter(attendance__date=today, attendance__status='P')
        return students_for_today

    def send_notification_to_students(self, message):
        for student in self.student_class.all():
            Notification.objects.create(user=student.user, message=message, class_attendance=self)
