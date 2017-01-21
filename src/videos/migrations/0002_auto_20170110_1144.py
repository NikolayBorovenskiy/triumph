# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 11:44
from __future__ import unicode_literals

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, help_text='Поддерживаемый формат видео video/mp4', null=True, upload_to=core.utils.upload_location),
        ),
    ]
