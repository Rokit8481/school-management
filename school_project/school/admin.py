from django.contrib import admin
from .models import Subject, Teacher, Class, Student, Schedule

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Schedule)
