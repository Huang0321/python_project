
from django.db import models

# Create your models here.


class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_tel = models.CharField(max_length=11)
    s_yuwen = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    S_operate_time = models.DateTimeField(null=True, auto_now=True)
    STATUS = [
        ('NONE', '正常'),
        ('NEXT_SCH', '留级'),
        ('DROP_SCH', '退学'),
        ('LEAVE_SCH', '休学')
    ]
    s_status = models.CharField(choices=STATUS, max_length=10, null=True)
    s_delete = models.BooleanField(default=0)

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
