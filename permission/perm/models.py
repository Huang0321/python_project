from django.db import models

# Create your models here.


class User(models.Model):
    u_name = models.CharField(max_length=10)
    u_sex = models.BooleanField()
    u_birth = models.DateField()
    u_create_time = models.DateField(auto_now_add=True)
    u_operate_time = models.DateField(auto_now=True)
    role = models.ForeignKey('Role')

    class Meta:
        db_table = 'user'


class Role(models.Model):
    r_name = models.CharField(max_length=10)
    p = models.ManyToManyField('Permission')

    class Meta:
        db_table = 'role'


class Permission(models.Model):
    p_name = models.CharField(max_length=10)
