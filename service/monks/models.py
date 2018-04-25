from django.db import models


# Create your models here.


class Monks(models.Model):
    monk_id = models.AutoField(primary_key=True)
    monk_name = models.CharField(max_length=10)
    monk_sex = models.BooleanField()
    monk_tel = models.CharField(max_length=11)
    monk_birth = models.DateField()
    monk_delete_date = models.BooleanField(default=0)
    monk_create_time = models.DateField(auto_now_add=True)
    monk_operate_time = models.DateField(auto_now=True)

    class meta:
        db_table = "monk_info"
