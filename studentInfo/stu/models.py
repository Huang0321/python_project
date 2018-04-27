from django.db import models

# Create your models here.


class Student(models.Model):
    stu_name = models.CharField(max_length=10)
    stu_sex = models.BooleanField()
    stu_birth = models.DateField()
    stu_height = models.CharField(max_length=5)
    stu_tel = models.CharField(max_length=11)
    stu_email = models.CharField(max_length=20)
    stu_grade = models.CharField(max_length=20)
    stu_interest = models.CharField(max_length=20)

    class Meta:
        db_table = 'student'

