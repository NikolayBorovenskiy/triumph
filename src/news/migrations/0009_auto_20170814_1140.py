# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-14 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20170123_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True, unique=True),
        ),
    ]
