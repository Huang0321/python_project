# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'grade',
            },
        ),
    ]
