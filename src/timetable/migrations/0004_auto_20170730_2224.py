# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-30 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20170730_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='title',
            field=models.CharField(choices=[(0, 'понедельник'), (1, 'вторник'), (2, 'среда'), (3, 'четверг'), (4, 'пятница'), (5, 'суббота'), (6, 'воскресенье')], max_length=12),
        ),
    ]
