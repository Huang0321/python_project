# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-05 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0006_auto_20180505_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='S_operate_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
