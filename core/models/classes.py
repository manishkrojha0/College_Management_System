from core.models.base_model import BaseModel
from core.models import student, teacher
from django.db import models

class Classes(BaseModel):
    """Class Model."""
    
    name = models.CharField(max_length=255)
    teacher = models.ManyToManyField(teacher.Teacher, related_name='teacher_class')
    student = models.ManyToManyField(student.Student, related_name='student_class')
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
