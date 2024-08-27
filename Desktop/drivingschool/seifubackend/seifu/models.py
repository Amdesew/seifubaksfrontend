from django.db import models

class NewStudent(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    wanted_licence = models.CharField(max_length=15)

class StudentResult(models.Model):
    full_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)
    result = models.CharField(max_length=3)