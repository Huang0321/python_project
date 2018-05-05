
from django.db import models

# Create your models here.


class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'students'


class StudentInfo(models.Model):
    i_addr= models.CharField(max_length=30)
    i_unage = models.ImageField(upload_to='upload', null=True)
    s = models.ForeignKey(Student, null=True)

    class Meta:
        db_table = 'student_info'


class Visit(models.Model):

    v_url = models.CharField(max_length=30)
    v_times = models.IntegerField()

    class Meta:
        db_table = 'visit_times'
