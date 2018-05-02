# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0003_studentinfo_i_unage'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorStatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vis_num', models.IntegerField(default=0, max_length=10)),
            ],
            options={
                'db_table': 'vis_static',
            },
        ),
    ]
