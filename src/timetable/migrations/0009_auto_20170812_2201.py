# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-12 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_event_additional_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='additional_info',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Дополнительная информация'),
        ),
    ]
