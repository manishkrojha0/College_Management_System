from rest_framework import serializers
from core.models.classes import Classes
from core.models.student import Student
from core.models.teacher import Teacher
from core.models.user_address import UserAddress
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, teacher):
        """Get full name of student."""
        teacher_obj = Teacher.objects.get(teacher)
        if not teacher_obj:
            return ""
        first_name = teacher_obj.first_name
        middle_name = teacher_obj.middle_name
        last_name = teacher_obj.last_name
        full_name = first_name + " " + last_name if not middle_name else first_name + " "+ middle_name + " "  + last_name
        return full_name

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'emp_id']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, student):
        """Get full name of student."""
        student_obj = Student.objects.get(student)
        first_name = student_obj.first_name
        middle_name = student_obj.middle_name
        last_name = student_obj.last_name
        full_name = first_name + " " + last_name if not middle_name else first_name + " "+ middle_name + " "  + last_name
        return full_name

    class Meta:
        model = Student
        fields = ['id', 'user', 'roll_no', 'full_name']

class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=True)
    students = StudentSerializer(many=True)

    class Meta:
        model = Classes
        fields = ['id', 'name', 'teacher', 'student']
