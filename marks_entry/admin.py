# admin.py
from django.contrib import admin
from .models import Student, Question, Marks

admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Marks)
