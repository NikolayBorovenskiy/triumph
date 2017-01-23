# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 12:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_created', '-date_updated']},
        ),
        migrations.RemoveField(
            model_name='news',
            name='photo',
        ),
        migrations.AddField(
            model_name='news',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=news.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 1, 2, 12, 16, 23, 464619), unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]