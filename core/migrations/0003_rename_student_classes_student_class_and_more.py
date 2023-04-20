# Generated by Django 4.2 on 2023-04-20 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_classes_end_time_classes_start_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classes',
            old_name='student',
            new_name='student_class',
        ),
        migrations.RenameField(
            model_name='classes',
            old_name='teacher',
            new_name='teacher_class',
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('message', models.TextField(null=True)),
                ('read', models.BooleanField(default=False, null=True)),
                ('class_attendance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.classes')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('', 'Select Attendence'), ('present', 'Present'), ('absent', 'Absent')], max_length=10)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.classes')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.student')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher')),
            ],
            options={
                'unique_together': {('date', 'class_id', 'student_id', 'teacher_id')},
            },
        ),
    ]