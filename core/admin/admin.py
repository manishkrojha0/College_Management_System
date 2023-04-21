# myapp/admin.py
from django.contrib import admin
from core.models.teacher import Teacher
from core.models.student import Student
from core.models.classes import Classes
from core.models.user_address import UserAddress
from core.models.attendence import Attendance
from core.models.notification import Notification
from django.contrib.admin.models import LogEntry


from core.models.users import Users

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'action_time', 'content_type', 'object_id', 'object_repr', 'change_message')
    search_fields = ['object_repr', 'change_message']
    list_filter = ('action_time', 'content_type')

    def user(self, obj):
        if obj.user:
            return obj.user.username
        return ''
    user.short_description = 'Users'

admin.site.register(LogEntry, LogEntryAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'created', 'modified', 'user_address')

admin.site.register(Teacher, TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'created', 'modified', 'user_address')

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time')

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'landmark', 'pincode')

class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('date', 'status')
    list_filter = ('student_id__roll_no', 'teacher_id__emp_id')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'class_attendance', 'read')
    list_filter = ['read']

admin.site.register(Student, StudentAdmin)
admin.site.register(Classes, ClassAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(Attendance, AttendenceAdmin)
admin.site.register(Notification, NotificationAdmin)
