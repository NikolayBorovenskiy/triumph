# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-21 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0007_style_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='group',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Группа'),
        ),
    ]