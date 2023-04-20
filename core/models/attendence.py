from django.db import models
from django.utils import timezone
from core.models.teacher import Teacher
from core.models.student import Student
from core.models.classes import Classes
from core.utils.constants import STATUS_CHOICES
from .base_model import BaseModel


class Attendance(BaseModel):

    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'class_id', 'student_id', 'teacher_id') # created the unique primary key of these pairs.
