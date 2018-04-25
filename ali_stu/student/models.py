from django.db import models

# Create your models here.


class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    stu_name = models.CharField(max_length=10)
    stu_sex = models.BooleanField()
    stu_birth = models.DateField()
    stu_tel = models.CharField(max_length=11)
    stu_create_time = models.DateField(auto_now_add=True)
    stu_operate_time = models.DateField(auto_now=True)
    stu_g_id = models.IntegerField()

    class Meta:
        db_table = 'stu_info'


class Grades(models.Model):
    g_id = models.AutoField(primary_key=True)
    g_name = models.CharField(max_length=20)
    g_des = models.CharField(max_length=30)

    class Meta:
        db_table = 'grades'

