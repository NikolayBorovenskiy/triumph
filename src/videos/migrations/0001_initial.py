# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 02:42
from __future__ import unicode_literals

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=core.utils.upload_location)),
            ],
            options={
                'verbose_name_plural': 'Видеогалерия',
                'ordering': ['-date_created', '-date_updated'],
            },
        ),
    ]