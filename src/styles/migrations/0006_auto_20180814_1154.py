# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-14 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0005_style_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Подзаголовок'),
        ),
    ]