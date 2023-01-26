from django.contrib import admin
from .models import Course, Teacher, Message, Qoshilish

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    ordering = ['-date']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'science', 'date']
    ordering = ['-date']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'date']
    ordering = ['-date']


@admin.register(Qoshilish)
class QoshilishAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'date']
    ordering = ['-date']
