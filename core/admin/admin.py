# myapp/admin.py
from django.contrib import admin
from core.models.teacher import Teacher
from core.models.student import Student
from core.models.classes import Classes
from core.models.user_address import UserAddress

print("hiii")

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'emp_id', 'created', 'modified', 'user_address')

admin.site.register(Teacher, TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_no', 'created', 'modified', 'user_address')

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'landmark', 'pincode')


admin.site.register(Student, StudentAdmin)
admin.site.register(Classes, ClassAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
