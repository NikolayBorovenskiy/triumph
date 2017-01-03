# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контент')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
