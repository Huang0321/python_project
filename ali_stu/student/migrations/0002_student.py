# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stu_id', models.AutoField(primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=10)),
                ('stu_sex', models.BooleanField()),
                ('stu_birth', models.DateField()),
                ('stu_tel', models.CharField(max_length=11)),
                ('stu_create_time', models.DateField(auto_now_add=True)),
                ('stu_operate_time', models.DateField(auto_now=True)),
                ('stu_g_id', models.IntegerField()),
            ],
            options={
                'db_table': 'stu_info',
            },
        ),
    ]
