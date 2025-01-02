from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class Question(models.Model):
    question_id = models.CharField(max_length = 100)

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    marks = models.IntegerField(null = True)
