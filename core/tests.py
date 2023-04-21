from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models.teacher import Teacher
from core.models.student import Student 
from core.models.classes import Classes
from core.models.user_address import UserAddress
from core.serializers import  TeacherSerializer, StudentSerializer, ClassesSerializer, UserAddressSerializer


class TeacherAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create(username='admin', password='password', is_staff=True)
        self.teacher_data = {
            'user': {
                'username': 'teacher',
                'email': 'teacher@example.com',
                'password': 'password'
            },
            'name': 'John Doe',
            'subject': 'Math',
            'experience': 5,
            'first_name': 'John',
            'dob': '2000-09-25',
            'gender': 'MALE',
            'contact': '9876543210'
        }
        self.client.force_login(self.admin)

    def test_create_teacher(self):
        url = reverse('teacher-list')
        response = self.client.post(url, self.teacher_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teacher.objects.count(), 1)
        self.assertEqual(Teacher.objects.get().name, 'John Doe')
