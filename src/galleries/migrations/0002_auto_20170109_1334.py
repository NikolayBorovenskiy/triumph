# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
