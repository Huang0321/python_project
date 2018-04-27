from django.db import models

# Create your models here.


class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'students'


class StudentInfo(models.Model):
    i_addr= models.CharField(max_length=30)
    s = models.ForeignKey(Student, null=True)

    class Meta:
        db_table = 'student_info'