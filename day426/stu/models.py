from django.db import models

# Create your models here.
from grade.models import Grades


class Students(models.Model):
    s_name = models.CharField(max_length=10)
    g = models.ForeignKey(Grades)

    class Meta:
        db_table = 'students'

